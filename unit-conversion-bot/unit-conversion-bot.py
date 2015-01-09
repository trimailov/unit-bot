from collections import namedtuple
import re

import praw

import creds
from finder import Finder

r = praw.Reddit(user_agent=creds.USER_AGENT)
r.login(creds.USERNAME, creds.PASSWORD)
del creds.PASSWORD

def get_new_posts():
    submissions = r.get_subreddit('test_unitbot').get_new()

    for submission in submissions:
        selftext = submission.selftext
        if selftext:
            finder = Finder(selftext)
            submission.add_comment(finder.convert_units())

if __name__ == "__main__":
    get_new_posts()

