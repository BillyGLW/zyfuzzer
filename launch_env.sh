#!/bin/bash


function launch {
if [ -d "_env" ]; then
	echo "Env exist."
	source /_env/bin/activate
	python3 -m pip install -r requirements.txt
	sed -i 's/\r$//g' launch.sh

 else
 	rm -r _env
 	sudo apt-get install python3-venv
	python3 -m venv _env
fi
}
launch