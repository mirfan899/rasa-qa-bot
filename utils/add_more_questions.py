# encoding: utf-8
import json
qa = json.load(open("english_questions_answers.json", encoding="utf-8"))
questions = []
for dic in qa:
    for k, v in dic.items():
        if k is "q":
            questions.append(v)

md = open("data/nlu/qa.md", "a")
for question in questions:
    md.write("- " + question + "\n")
