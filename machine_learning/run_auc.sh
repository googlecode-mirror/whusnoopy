#!/bin/bash

./calc_auc/calcAuc \
        --root_dir="./" \
        --logtostderr \
        --instance_file="./data/instance_for_eval.txt" \
        --model_file="./output/model.txt" \
