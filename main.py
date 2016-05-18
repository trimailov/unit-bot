import time

from unit_bot import bot


if __name__ == "__main__":
    while True:
        bot.get_new_posts()
        time.sleep(60)
