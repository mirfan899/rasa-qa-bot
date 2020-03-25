import json
import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from bert_serving.client import BertClient

app = Flask(__name__)
CORS(app)

bc = BertClient()
faq_data = json.load(open("./data/nlu/knowledge_base.json", "r", encoding="utf-8"))
standard_questions_encoder = np.load("./data/standard_questions.npy")
standard_questions_encoder_len = np.load("./data/standard_questions_len.npy")


def get_most_similar_standard_question_id(query_question):
    query_vector = bc.encode([query_question])[0]
    score = np.sum((standard_questions_encoder * query_vector), axis=1) / (
            standard_questions_encoder_len * (np.sum(query_vector * query_vector) ** 0.5))
    top_id = np.argsort(score)[::-1][0]
    return top_id, score[top_id]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/score', methods=["POST"])
def score():
    """
    Get semantic score of the question from bert encodings.
    :param text:
    :return: score, idx
    """
    if request.method == "POST":
        text = request.json
        print(text)
        if text["question"]:
            idx, score = get_most_similar_standard_question_id(text["question"])
            # return jsonify({"success": 200})
            print(score, idx)
            return jsonify({"score": str(score), "index": str(idx)})
            # if idx >= 90:
            #     data = [answer for answer in faq_data if idx == answer["index"]]
            #     return jsonify(data)
            # else:
            #     return jsonify({"Error": "Sorry I did not get your question"})
            # return jsonify({"score": str(score), "id": str(idx)})
        else:
            return jsonify({"Error": "Sorry I did not get your question"})

    # return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=False)
