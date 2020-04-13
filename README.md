### Clone the repo
```shell script
git clone sudo https://github.com/mirfan899/rasa-qa-bot.git
cd rasa-qa-bot
```

### Create virtualenvs
Run the shell script, which will create two virtualenvs. One for Rasa and second for BERT
```shell script
sudo ./setup.sh
```

### Services for Bert and rasa
Copy `systemctl` services files to proper location
```shell script
sudo cp rasa_run.service /etc/systemd/system/rasa.service
sudo cp bert_run.service /etc/systemd/system/bert.service
sudo cp rasa_actions.service /etc/systemd/system/actions.service
```

### Install SpaCy
We need to install SpaCy. 
```shell script
pip3 install spacy
```
## SpaCy model download and link
Install English model
```shell script
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en
```
### Train the Rasa model
```shell script
python -m rasa train
```

## Run Rasa server and BERT server
Enable the CORS for any web api. There is a shell script which and service which will run at as deamon process for
deployment. If you setting up this repository, you need to fix the paths in `systemctl` service files i.e. `rasa_run.service`, `rasa_actions.service`
`bert_run.service`
```shell script
sudo systemctl start rasa
sudo systemctl start actions
```

## Run flask app
For testing purpose run the flask app.
```shell script
export FLASK_APP=app.py && flask run
```

## Run bert server
```shell script
sudo systemctl start bert
```
to stop the server
```shell script
sudo systemctl stop bert
```

## Adding questions to Rasa bot.
If you want to add questions to Rasa NLU Bot use this file `data/nlu/qa.md`, there is a script which uses the json format for adding the question into model.
```shell script
python utils/add_more_questions.py
```
It will look for file with name `english_questions_answers.json` with format
```python
[
    {
        "q": "Question here",
        "a": "Answer here"
    },
    {
        "q": "Another Question here",
        "a": "Another Answer here"
    }
]
```
this script will merge two json files containing questions and answers.
```shell script
python utils/merge_json.py
```
