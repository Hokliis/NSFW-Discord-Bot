from random import randint as randomint

import discord
import aiohttp
from discord.ext import commands
from nsfwbot.database import get_embeds, get_main


class Eporner(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.command()
    async def pornlink(self, ctx, *, query):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            index_to_give = randomint(1, 70)

            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f"https://www.eporner.com/api/v2/video/search/?query={query}&per_page=72&thumbsize=big&order=top-weekly&format=json") as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                        embed3.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    try:
                        resultjson = await jsondata.json()
                    except:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Unable to convert API result to json", inline=False)
                        embed3.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

            em = discord.Embed(title="Pornographic Content", url=f'{resultjson["videos"][index_to_give]["url"]}',
                               description="Here is a video for you!", color=get_embeds.Common.COLOR)
            em.set_author(name=f"{self.client.user.name}",
                          icon_url=f"{self.client.user.avatar_url}")
            em.set_image(url=resultjson["videos"]
                         [index_to_give]["default_thumb"]["src"])
            em.add_field(
                name="Title", value=f'{resultjson["videos"][index_to_give]["title"]}', inline=False)
            em.add_field(
                name="Keywords", value=f'{resultjson["videos"][index_to_give]["keywords"]}', inline=False)
            em.add_field(
                name="Views", value=f'{resultjson["videos"][index_to_give]["views"]}', inline=False)
            em.add_field(
                name="Rating", value=f'{resultjson["videos"][index_to_give]["rate"]}', inline=False)
            em.add_field(
                name="Uploaded on", value=f'{resultjson["videos"][index_to_give]["added"]}', inline=False)
            em.add_field(
                name="Length", value=f'{resultjson["videos"][index_to_give]["length_min"]}', inline=False)
            em.add_field(
                name="URL", value=f'{resultjson["videos"][index_to_give]["url"]}', inline=False)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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
    async def pornlinks(self, ctx, amount: int = None, *, query=None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:

            if (amount == None) or (query == None):
                embed = discord.Embed(title="Invalid Usage",
                                      description=f"Invalid command usage for {get_main.BotMainDB.MESSAGE_PREFIX}pornlinks")
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(
                    url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed.add_field(
                    name="Usage", value=f"```{get_main.BotMainDB.MESSAGE_PREFIX} <amount> *<query>```", inline=False)
                embed.add_field(
                    name="Usage - Example", value=f"```{get_main.BotMainDB.MESSAGE_PREFIX} 5 hardcore```", inline=False)
                embed.add_field(name="<amount>",
                                value="Type: integer. a non decimal number. Maximum allowed number is 60. This amount of porn videos will be sent to you via DM", inline=True)
                embed.add_field(name="*<query>",
                                value="Type: string. a text. this is being queried from the API for a porn video", inline=True)
                embed.set_footer(
                    text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
                return

            else:
                async with aiohttp.ClientSession() as pornSession:
                    async with pornSession.get(f"https://www.eporner.com/api/v2/video/search/?query={query}&per_page=62&thumbsize=big&order=top-weekly&format=json") as jsondata:
                        if not 300 > jsondata.status >= 200:
                            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                            embed3.set_author(name=f"{self.client.user.name}",
                                              icon_url=f"{self.client.user.avatar_url}")
                            embed3.set_thumbnail(
                                url=get_embeds.ErrorEmbeds.THUMBNAIL)
                            embed3.add_field(
                                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                            embed3.set_footer(
                                text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return

                        try:
                            resultjson = await jsondata.json()
                        except:
                            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                            embed3.set_author(name=f"{self.client.user.name}",
                                              icon_url=f"{self.client.user.avatar_url}")
                            embed3.set_thumbnail(
                                url=get_embeds.ErrorEmbeds.THUMBNAIL)
                            embed3.add_field(
                                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Unable to convert API result to json", inline=False)
                            embed3.set_footer(
                                text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return

                if int(amount) <= 60:
                    emchannels = discord.Embed(
                        title="Pornographic Content", description="```Please check your Direct Messages```", color=get_embeds.Common.COLOR)
                    emchannels.set_footer(
                        text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=emchannels)

                    for index_to_give in range(int(amount)):
                        em = discord.Embed(title="Pornographic Content", url=f'{resultjson["videos"][index_to_give]["url"]}',
                                           description="Here are some videos for you!", color=get_embeds.Common.COLOR)
                        em.set_author(name=f"{self.client.user.name}",
                                      icon_url=f"{self.client.user.avatar_url}")
                        em.set_image(url=resultjson["videos"]
                                     [index_to_give]["default_thumb"]["src"])
                        em.add_field(
                            name="Title", value=f'{resultjson["videos"][index_to_give]["title"]}', inline=False)
                        em.add_field(
                            name="Keywords", value=f'{resultjson["videos"][index_to_give]["keywords"]}', inline=False)
                        em.add_field(
                            name="Views", value=f'{resultjson["videos"][index_to_give]["views"]}', inline=False)
                        em.add_field(
                            name="Rating", value=f'{resultjson["videos"][index_to_give]["rate"]}', inline=False)
                        em.add_field(
                            name="Uploaded on", value=f'{resultjson["videos"][index_to_give]["added"]}', inline=False)
                        em.add_field(
                            name="Length", value=f'{resultjson["videos"][index_to_give]["length_min"]}', inline=False)
                        em.add_field(
                            name="URL", value=f'{resultjson["videos"][index_to_give]["url"]}', inline=False)
                        em.set_footer(text=f"Requested by {ctx.author.name}")
                        await ctx.author.send(embed=em)

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


def setup(client: commands.Bot):
    client.add_cog(Eporner(client))
