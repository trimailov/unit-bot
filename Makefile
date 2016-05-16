CTAGS=/usr/local/bin/ctags

all: env pip ctags

.PHONY: env
env:
	pyvenv env

.PHONY: pip-tools
pip-tools:
	env/bin/pip install pip-tools

.PHONY: pip
pip: pip-tools
	env/bin/pip-sync requirements.txt

.PHONY: pip-compile
pip-compile: pip-tools
	env/bin/pip-compile requirements.in

.PHONY: run
run: rm_cache
	env/bin/python unit_bot/bot.py

.PHONY: test
test:
	env/bin/py.test

.PHONY: watch-test
watch-test:
	env/bin/ptw

.PHONY: rm_cache
rm_cache:
	rm -rf __pycache__

.PHONY: tags
ctags:
	$(CTAGS) -R --exclude=.git

.PHONY: requirements
requirements:
	env/bin/pip freeze > requirements.txt

.PHONY: clean
clean:
	rm -rf __pycache__ env tags
