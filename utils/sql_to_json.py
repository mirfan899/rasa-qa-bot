import json

import mysql.connector
from polyglot.detect import Detector
import re
import pandas as pd

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    database='Questions')

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * from QUESTIONS_AND_ANSWERS")

# Fetch one result
# print(cur.description)
questions = []
answers = []
rows = cur.fetchall()
for row in rows:
    # using polyglot but it is not a good language predictor but free.
    q = " ".join(row[1].splitlines())
    a = " ".join(row[2].splitlines())
    q = re.sub("\r+", " ", q)
    a = re.sub("\n+", " ", a)
    q = re.sub("\s+", " ", q)
    a = re.sub("\s+", " ", a)
    q = Detector(q, quiet=True)
    a = Detector(a, quiet=True)
    if q.language.code == "en" and a.language.code == "en":
        questions.append(row[1].strip())
        answers.append(row[2].strip())

# Close connection
cnx.close()
js = []
for q, a in zip(questions, answers):
    js.append({"q": q, "a": a})

with open("english_questions_answers.json", encoding="utf8") as qa:
    json.dump(js, qa, indent=4)
# data = pd.DataFrame({"q": questions, "a": answers})
# data.dropna(inplace=True)
# data.drop_duplicates(inplace=True)
#
# data.to_json("english_questions_answers.json", orient="records")
