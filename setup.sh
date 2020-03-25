#!/bin/sh
## setup bert virtualenv
virtualenv -p python3.6 .bert
source .bert/bin/activate
pip3 install tensorflow==1.13.1
pip3 install bert-serving-client
pip3 install bert-serving-server
pip3 install Keras-Applications==1.0.8
pip3 install Keras-Preprocessing==1.1.0
pip3 install scipy
pip3 install numpy
pip3 install matplotlib==3.1.2
pip3 install protobuf==3.11.3
pip3 install scikit-learn==0.21.3

deactivate

virtualenv -p python3.6 .rasa
source .rasa/bin/activate
pip3 install tensorflow-gpu==2.1.0
pip3 install rasa==1.8.1
pip3 install rasa-x==0.26.1 --extra-index-url https://pypi.rasa.com/simple
pip3 install tensorflow-addons
pip3 install flask
pip3 install flask-cors


## get the bert model and save it in bert directory
cd bert
wget https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip
unzip wwm_uncased_L-24_H-1024_A-16.zip
cd ..

echo "Setup completed."