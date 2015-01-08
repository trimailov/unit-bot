import re

import praw

import creds

r = praw.Reddit(user_agent=creds.USER_AGENT)
r.login(creds.USERNAME, creds.PASSWORD)

del creds.PASSWORD

def get_new_posts():
    submissions = r.get_subreddit('test_unitbot').get_new()

    for submission in submissions:
        selftext = submission.selftext.encode('utf-8')
        if selftext:
            print(find_speed(selftext.decode('utf-8')))

def find_speed(text):
    """Find all units in given text

    >>> find_speed('Can we find speeds? 10kmh, .01 km/h')
    [('10', '', 'kmh', 'kmh', '', ''), ('.01', ' ', 'km/h', 'km/h', '', '')]
    >>> find_speed('Can we find speeds? 13.98 m/s')
    [('13.98', ' ', 'm/s', '', 'm/s', '')]
    >>> find_speed('Can we find speeds? 15mph, 62 mp/h')
    [('15', '', 'mph', '', '', 'mph'), ('62', ' ', 'mp/h', '', '', 'mp/h')]
    """
    NUMBER = "(\d+\.?\d*|\.\d+)"

    SPEED_KM = "(kmh|km/h)"
    SPEED_MTR = "(m/s)"
    SPEED_MILE = "(mph|mp/h)"

    REGEXP = "%s(\s)*(%s|%s|%s)" % (NUMBER, SPEED_KM, SPEED_MTR, SPEED_MILE)

    regexp = re.compile(REGEXP)
    finds = regexp.findall(text)

    if finds:
        return finds

if __name__ == "__main__":
    get_new_posts()

