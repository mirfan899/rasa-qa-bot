# encoding: utf-8
import json
qa = json.load(open("english_questions_answers.json", encoding="utf-8"))
questions = [question["q"].strip() for question in qa]

md = open("data/nlu/qa.md", "a")
for question in questions:
    md.write("- " + question + "\n")
