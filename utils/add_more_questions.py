# encoding: utf-8
import json
qa = json.load(open("english_questions_answers.json", encoding="utf-8"))
questions = []
for k, v in qa.items():
    if k is "q":
        print(v)
        questions.append(v)

md = open("data/nlu/qa.md", "a")
for question in questions:
    md.write("- " + question + "\n")
