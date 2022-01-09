import json


with open("nsfwbot/database/main.json", "r", encoding="utf-8") as _file_all:
    _others = json.load(_file_all)
    other_settings = _others["OTHER"]


class BotMainDB:
    with open("nsfwbot/database/main.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    MESSAGE_PREFIX = embed["MESSAGE_PREFIX"]
    BOT_CREATOR_NAME = embed["BOT_CREATOR_NAME"]
    BOT_VERSION = embed["BOT_VERSION"]
    DEV_AND_OWNERS = embed["DEV_AND_OWNERS"]
