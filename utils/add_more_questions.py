# encoding: utf-8
import json
questions = json.load(open("../english_questions_answers.json", encoding="utf-8"))
questions = [question["q"] for question in questions]

md = open("../data/nlu/qa.md", "a")
for question in questions:
    md.write("- " + question + "\n")
