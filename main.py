import sys

from unit_bot import bot


if __name__ == "__main__":
    # --debug: 'test_unitbot' subreddit, replying enabled
    # --no-reply: 'all' subreddit, replying disabled
    # no extra option: 'all' subreddit, replying enabled
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        bot.scan_and_respond(reply=True, sub='test_unitbot')
    elif len(sys.argv) == 2 and sys.argv[1] == "--no-reply":
        bot.scan_and_respond(reply=False, sub='all')
    else:
        bot.scan_and_respond(reply=True, sub='all')
