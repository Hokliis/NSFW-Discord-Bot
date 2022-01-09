import json

with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as _file_all:
    _others = json.load(_file_all)
    other_embeds = _others["OTHER"]


class PleaseWait:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as _file:
        _embed = json.load(_file)

    TITLE = _embed["PleaseWaitEmbed"]["TITLE"]
    DESCRIPTION = _embed["PleaseWaitEmbed"]["DESCRIPTION"]
    THUMBNAIL = _embed["PleaseWaitEmbed"]["THUMBNAIL"]
    FOOTER = _embed["PleaseWaitEmbed"]["FOOTER"]

    if _embed["PleaseWaitEmbed"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif _embed["PleaseWaitEmbed"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif _embed["PleaseWaitEmbed"]["COLOR"] == "blue":
        COLOR = 0x0000ff

    AUTHOR_NAME = _embed["PleaseWaitEmbed"]["AUTHOR_NAME"]
    AUTHOR_URL = _embed["PleaseWaitEmbed"]["AUTHOR_URL"]


class ErrorEmbeds:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as _file:
        _embed = json.load(_file)

    TITLE = _embed["ERROR"]["TITLE"]
    DESCRIPTION = _embed["ERROR"]["DESCRIPTION"]
    THUMBNAIL = _embed["ERROR"]["THUMBNAIL"]
    FIELD_NAME = _embed["ERROR"]["FIELD_NAME"]

    if _embed["ERROR"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif _embed["ERROR"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif _embed["ERROR"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class Common:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as _file:
        _embed = json.load(_file)

    if _embed["COMMON"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif _embed["COMMON"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif _embed["COMMON"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class Help:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as _file:
        _embed = json.load(_file)

    if _embed["HELP"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif _embed["HELP"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif _embed["HELP"]["COLOR"] == "blue":
        COLOR = 0x0000ff

    THUMBNAIL = _embed["HELP"]["THUMBNAIL"]
