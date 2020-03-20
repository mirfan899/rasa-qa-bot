# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import numpy as np


class ActionGetFAQAnswer(Action):

    def __init__(self):
        super(ActionGetFAQAnswer, self).__init__()
        self.faq_data = json.load(open("./data/nlu/faq.json", "rt", encoding="utf-8"))

    def name(self) -> Text:
        return "action_get_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        response = requests.post("http://127.0.0.1:5000/api/score", json={"question": question})
        score = float(response.json()["score"])
        most_similar_id = int(response.json()["index"])
        # most_similar_id, score = 100, 90
        if score >= 0.90:
            response = self.faq_data[most_similar_id]['a']

            dispatcher.utter_message(response)
            # dispatcher.utter_message(template="utter_helpful")
        else:
            dispatcher.utter_message(template="utter_not_helpful")
        return []