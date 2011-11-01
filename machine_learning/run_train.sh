#!/bin/bash

./train/trainModel \
        --root_dir="./" \
        --logtostderr \
        --instance_file="./data/instance_for_train.txt" \
        --model_file="./output/model.txt" \
