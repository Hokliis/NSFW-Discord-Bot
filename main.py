import os

import discord
from discord.ext import commands

from nsfwbot.database import get_main

bot_prefix = get_main.BotMainDB.MESSAGE_PREFIX
bot_creator_name = get_main.BotMainDB.BOT_CREATOR_NAME
bot_current_version = get_main.BotMainDB.BOT_VERSION
bot_manager_ids = get_main.BotMainDB.DEV_AND_OWNERS


with open("token.txt", "r", encoding="utf-8") as tokenfile:
    token = tokenfile.read()


client = commands.Bot(command_prefix=bot_prefix)

client.load_extension("nsfwbot.cogs.General")
print("[+] Loaded: nsfwbot.cogs.General")
client.load_extension("nsfwbot.cogs.HentaiOld")
print("[+] Loaded: nsfwbot.cogs.HentaiOld")
client.load_extension("nsfwbot.cogs.HentaiNew")
print("[+] Loaded: nsfwbot.cogs.HentaiNew")
client.load_extension("nsfwbot.cogs.Eporner")
print("[+] Loaded: nsfwbot.cogs.Eporner")


@client.command()
async def loadex(ctx, extension):
    if ctx.author.id in bot_manager_ids:
        client.load_extension(f'nsfwbot.cogs.{extension}')
        embed = discord.Embed(
            title="SUCCESS", description=f"`ADDED cogs.{extension} from NearBot`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/923073371695099914/4rghdDI6DXyVN7U-mRBWYzN--y97aYNv_RP3PpKnHa1Om-xzj9A3a58Of5kKdKKbfjzdm2kI73o1QHfruCkkAkzmu10t4Wc.png")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await ctx.send(embed=embed)
        return


@client.command()
async def unloadex(ctx, extension):
    if ctx.author.id in bot_manager_ids:
        client.unload_extension(f'nsfwbot.cogs.{extension}')
        embed = discord.Embed(
            title="SUCCESS", description=f"`REMOVED cogs.{extension} from NearBot`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/923073371695099914/4rghdDI6DXyVN7U-mRBWYzN--y97aYNv_RP3PpKnHa1Om-xzj9A3a58Of5kKdKKbfjzdm2kI73o1QHfruCkkAkzmu10t4Wc.png")
        await ctx.send(embed=embed)
        return
    else:

        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await ctx.send(embed=embed)
        return


# This is for user input sanitization
# Add more stuff here to make it better
# Bascially, i dont know regex. sad. lol
blacklisted_letters_n_words = (
    # Full grabify link detection
    "grabify.link", "partpicker.shop", "websafe.online", "sportshub.bar", "herald.sbs", "locations.quest", "leancoding.co"
    "lovebird.guru", "trulove.guru", "dateing.club", "shrekis.life", "headshot.monster", "gaming-at-my.best", "stopify.co",
    "progaming.monster", "yourmy.monster", "imageshare.best", "screenshot.best", "gamingfun.me", "catsnthing.com",
    "catsnthings.fun", "curiouscat.club", "joinmy.site", "fortnitechat.site", "fortnight.space", "freegiftcards.co",

    # Others
    "nc", "netcat", "ncat", "apt", "snap", "remove", "uninstall", "{", "}", "<", ">", "/silent", "/verysilent", "python -c", "python3 -c"
)


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    msg = message.content

    if msg.startswith(f'{bot_prefix}'):

        msgaftercmnd = msg.split(" ")[1:-1]

        messagesubcont = ""
        for messagesubcontlp in msgaftercmnd:
            messagesubcont += messagesubcontlp

        if messagesubcont in blacklisted_letters_n_words:
            embed = discord.Embed(
                title="Something is wrong!", description="Please enter the command with valid characters", color=0xff0000)
            embed.set_author(
                name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
            await message.send(embed=embed)
            return

    await client.process_commands(message)

client.run(token)
