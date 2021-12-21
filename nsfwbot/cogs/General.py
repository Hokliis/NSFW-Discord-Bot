from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime

import discord
from discord.ext import commands
from nsfwbot.database import get_embeds, get_main


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # For custom help
        self.client.remove_command('help')

        # Bot uptime
        self.start_time = None

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user.name}')
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {cur_python_version()}')
        self.start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))
        print('Bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="ERROR", description="`You don't have the permissions required to use this command!`", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Something is wrong!", description="An error has been occured!", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
            embed.add_field(
                # name="Possible Fix", value=f"use `{get_main.BotMainDB.MESSAGE_PREFIX}help all` to list out all the command and check the proper usage of the command you used", inline=True)
                name="Possible Fix", value=f"use `{self.client.get_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
            await ctx.send(embed=embed)
            return

    @commands.command()
    async def ping(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed = discord.Embed(title="Response Time",
                                  color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(
                name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
    async def uptime(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - self.start_time))
            text = str(dttimedelta(seconds=difference))
            embed = discord.Embed(color=get_embeds.Common.COLOR)
            embed.add_field(name="The bot was online for: ",
                            value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clean(self, ctx, amount=5):
        """
        Delete messages sent by the bot itself to the message channel
        You need have the "manage_messages" permission to use this command
        """
        try:
            if amount <= 100:
                amttdel = amount + 1
                await ctx.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                if amount == "1":
                    msgtxt = "message"
                else:
                    msgtxt = "messages"

                embed = discord.Embed(
                    title="Success!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.add_field(
                    name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed, delete_after=4)

            else:
                embed2 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                       description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed2.set_author(name=f"{self.client.user.name}",
                                  icon_url=f"{self.client.user.avatar_url}")
                embed2.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(
                    name="Error:", value=f"Please enter a value below 100!", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed2)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)

    @commands.command()
    async def help(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        bp = get_main.BotMainDB.MESSAGE_PREFIX

        try:
            embed3 = discord.Embed(
                title=":gear: Help", color=get_embeds.Help.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(
                url=get_embeds.Help.THUMBNAIL)
            embed3.add_field(
                name="Crypto:", value=f"", inline=False)

            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)


def setup(client: commands.Bot):
    client.add_cog(General(client))
