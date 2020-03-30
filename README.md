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