#!/bin/bash

source .bert/bin/activate
bert-serving-start -model_dir=bert_model/uncased_L-2_H-128_A-2 -num_worker=1 -max_seq_len=20
