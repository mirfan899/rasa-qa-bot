#!/bin/sh

cd
cd Documents/fiverr/rasa-faq-bot/
source .rasa/bin/activate
#
bert-serving-start -model_dir=bert/uncased_L-2_H-128_A-2 -num_worker=1 -max_seq_len=20
##nohup bert-serving-start -model_dir=bert_model/uncased_L-2_H-128_A-2 -num_worker=1 -max_seq_len=20 > /dev/null 2>&1 &
