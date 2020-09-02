

PROGNAME = zyfuzzer
VERSION  = $(shell grep 'VERSION = ' misc.py | cut -d '"' -f2)
PROGS   ?= dependencies install run
TESTPYTHON = python3
TESTRUN = -c 'print "TEST"'


all: $(PROGS)

dependencies:
	python -m venv _env

install:
	siemanko\\Scripts\\activate

version-check:
	(echo $(VERSION))

test:
	$(TESTPYTHON) $(TESTRUN)

clean:
	del siemanko
	y	
.PHONY:
	test clean