from bert_serving.client import BertClient
import numpy as np
import json


def encode_standard_question():
    bc = BertClient(check_length=False)
    data = json.load(open("./data/nlu/qa.json", "r", encoding="utf-8"))
    standard_questions = [each['q'] for each in data]
    print("Standard question size", len(standard_questions))
    print("Start to calculate encoder....")
    standard_questions_encoder = bc.encode_async(standard_questions)
    np.save("./data/standard_questions", standard_questions_encoder)
    standard_questions_encoder_len = np.sqrt(np.sum(standard_questions_encoder * standard_questions_encoder, axis=1))
    np.save("./data/standard_questions_len", standard_questions_encoder_len)


if __name__ == '__main__':
    encode_standard_question()
