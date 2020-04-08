import mysql.connector
from textblob import TextBlob

# Usin service account of My Project on GCP
# path = "zippy-nexus-116320-1adad038b7e5.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
# from google.cloud import translate_v2 as translate
# translate_client = translate.Client()
# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="@pp!fy",
    database='Questions')

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * from QUESTIONS_AND_ANSWERS limit 10")

# Fetch one result
# print(cur.description)
questions = []
answers = []

# fetch 5 records
rows = cur.fetchmany(5)
for row in rows:
    questions.append(row[1])
    answers.append(row[2])

# fetch next 5 records
rows = cur.fetchmany(5)
for row in rows:
    questions.append(row[1])
    answers.append(row[2])


# Close connection
cnx.close()
for q, a in zip(questions, answers):
    # detector = Detector(q)
    # google language translate api for detecting language.
    b = TextBlob(q)
    print('Text: {}'.format(q))
    print("From TextBlob =================================================")
    print(b.detect_language())
    # print(detector.language)
    # print("Question: {}".format(q))
    # print("Answer: {}".format(a))

