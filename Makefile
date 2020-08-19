
all: dependencies install test


dependencies:
	python -m venv siemanko

install:
	siemanko\\Scripts\\activate

test:
	dir

clean:
	del siemanko
	y	