#!/bin/bash

source .bert/bin/activate
bert-serving-start -model_dir=bert/wwm_uncased_L-24_H-1024_A-16 -num_worker=1 -max_seq_len=20
