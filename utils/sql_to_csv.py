import mysql.connector
import os
import pandas as pd
from google.cloud import translate_v2 as translate
# Usin service account of My Project on GCP
path = "filename.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path

translate_client = translate.Client()
# Connect to server
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
    q = translate_client.detect_language(row[1])
    a = translate_client.detect_language(row[2])
    if q["language"] == 'en' and a["language"] == 'en':
        questions.append(row[1])
        answers.append(row[2])

# Close connection
cnx.close()

data = pd.DataFrame({"questions": questions, "answers": answers})
print(data.head(5))
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

data.to_csv("english_questions_answers.csv", index=False)
