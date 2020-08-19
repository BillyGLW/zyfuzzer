
all: dependencies install test


dependencies:
	python -m venv _env

install:
	siemanko\\Scripts\\activate

test:
	dir

clean:
	del siemanko
	y	