#!/usr/bin/env python
# encoding: utf-8
import json
import random
import glob
files = glob.glob("questions/*.json")

questions = []
for file_ in files:
    data = json.load(open(file_, encoding="utf-8"))
    for question in data:
        questions.append(question["question"])

print(len(questions))
md = open("data/nlu/faq.md", "a")
md.write("## intent:faq\n")
for question in questions:
    md.write("- " + question + "\n")
json.dump(questions, open("data/questions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
