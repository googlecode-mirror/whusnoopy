#!/bin/bash

filename=${1##*/}

wget -O $filename -o wget.log $1

echo 'Get html finish, start parse'

./extract_dospy $filename

echo 'parse finish'

