import praw

from unit_bot import creds
from unit_bot.finder import Finder


def scan_and_respond(reply=False, sub='test_unitbot'):
    r = praw.Reddit(user_agent=creds.USER_AGENT)
    r.login(creds.USERNAME, creds.PASSWORD, disable_warning=True)
    del creds.PASSWORD

    last_comment = ''
    while True:
        for comment in praw.helpers.comment_stream(r, sub):
            finder = Finder(comment.body)

            # if we found units to convert and comment is later than the
            # last one we replied to, then try to reply
            if finder.units and comment.id > last_comment and reply:
                last_comment = comment.id

                # in case we try to reply to unreplieable comment
                # e.g. comment got deleted, is to old or etc.
                # just ignore error then and pass on
                try:
                    comment.reply(finder.generate_conversion_message())
                except praw.errors.APIException:
                    pass
