#!/bin/bash

export DEBUG="1"
./launch_env.sh


source /_env/bin/activate
python3 fuzzing_main.py

