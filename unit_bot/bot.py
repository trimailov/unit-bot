import time

import praw

from unit_bot import creds
from unit_bot.finder import Finder

r = praw.Reddit(user_agent=creds.USER_AGENT)
r.login(creds.USERNAME, creds.PASSWORD, disable_warning=True)
del creds.PASSWORD


def get_new_posts():
    submissions = r.get_subreddit('test_unitbot').get_new(limit=100)

    try:
        f = open('last_submission', 'r+')
    except IOError:
        f = open('last_submission', 'w+')
    last_submission = f.readline()

    for i, submission in enumerate(submissions):
        print(i, submission.id, last_submission)
        if i == 0:
            f.seek(0)
            f.truncate()
            f.write(submission.id)
            f.close()
        if submission.id <= last_submission:
            break

        selftext = submission.selftext
        if selftext:
            finder = Finder(selftext)
            submission.add_comment(finder.generate_conversion_message())
            print("Commented on {}".format(submission.short_link))
