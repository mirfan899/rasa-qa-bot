### Install spacy 
```shell script
pip3 install spacy
```
## SpaCy model download and link
```shell script
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en
```

## run rasa server
```shell script
python -m rasa run --enable-api --cors "*"
```

## run flask app
```shell script
export FLASK_APP=app.py && flask run
```

## run bert server
```shell script
./start_bert_service.sh
```
to stop the server
```shell script
./stop_bert_service.sh
```

GCS login
gcloud compute ssh virtuoso_irfan@rasa-qa-bot --zone us-central1-a

ip address of GCS server
http://35.184.237.131:5005/

Database dump
```shell script
mysqldump -u Onjoroge1 -h Onjoroge1.mysql.pythonanywhere-services.com 'Onjoroge1$Questions' > Questions.sql;
```

create database on local machine
```shell script
mysql -u root -p
create database Questions;
```

Dump remote db into local
```shell script
mysql -u root –p @pp!fy Questions < Questions.sql;
```
