# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

import requests
from bert_serving.client import BertClient
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import numpy as np


class ActionGetFAQAnswer(Action):

    def __init__(self):
        super(ActionGetFAQAnswer, self).__init__()
        self.bc = BertClient()
        self.standard_questions_encoder = np.load("./data/standard_questions.npy")
        self.standard_questions_encoder_len = np.load("./data/standard_questions_len.npy")
        self.faq_data = json.load(open("./data/nlu/qa.json", "rt", encoding="utf-8"))

    def get_most_similar_standard_question_id(self, query_question):
        query_vector = self.bc.encode([query_question])[0]
        score = np.sum((self.standard_questions_encoder * query_vector), axis=1) / (
                self.standard_questions_encoder_len * (np.sum(query_vector * query_vector) ** 0.5))
        top_id = np.argsort(score)[::-1][0]
        return top_id, score[top_id]

    def name(self) -> Text:
        return "action_get_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        # response = requests.post("http://127.0.0.1:5000/api/score", json={"question": question})
        # most_similar_id, score = self.get_most_similar_standard_question_id(query)
        most_similar_id, score = self.get_most_similar_standard_question_id(question)
        # score = float(response.json()["score"])
        # most_similar_id = int(response.json()["index"])
        # most_similar_id, score = 100, 90
        if score >= 0.70:
            response = self.faq_data[most_similar_id]['a']

            dispatcher.utter_message(response)
            # dispatcher.utter_message(template="utter_helpful")
        else:
            dispatcher.utter_message(template="utter_not_helpful")
        return []