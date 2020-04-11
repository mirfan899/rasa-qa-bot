import json
questions = json.load(open("english_questions_answers.json", encoding="utf-8"))

feedjson = json.load(open("data/nlu/qa.json", encoding='utf-8'))

for obj in questions:
    feedjson.append(obj)
json.dump(feedjson, open("data/nlu/qa.json", "w"), indent=4)