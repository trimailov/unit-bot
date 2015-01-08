CTAGS=/usr/local/bin/ctags

.PHONY: all
all: env ctags
	env/bin/pip install -r requirements.txt

.PHONY: env
env:
	pyvenv env

.PHONY: run
run: rm_cache
	env/bin/python unit-conversion-bot/unit-conversion-bot.py

.PHONY: doctest
doctest: rm_cache
	env/bin/python -m doctest -v unit-conversion-bot/unit-conversion-bot.py

.PHONY: rm_cache
rm_cache:
	rm -rf __pycache__

.PHONY: ctags
ctags:
	$(CTAGS) -R --exclude=.git

.PHONY: requirements
requirements:
	env/bin/pip freeze > requirements.txt

.PHONY: clean
clean:
	rm -rf __pycache__ env tags

