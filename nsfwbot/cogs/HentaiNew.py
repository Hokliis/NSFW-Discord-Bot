import discord
import requests
import textwrap
import urllib
import aiohttp
import datetime
from discord.ext import commands
from nsfwbot.database import get_embeds, get_main
from nsfwbot.database.get_embeds import other_embeds
from nsfwbot.database.get_main import other_settings


class Hentai(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.Cog.listener()
    async def on_message(self, message):
        pass

    @commands.command()
    async def lesbian(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession(other_settings["HentaiCog"]["lesbian"]["APIlink"]) as pornSession:
                async with pornSession.get() as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["HentaiOther"]["StatusCodeError"], inline=False)
                        embed3.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    try:
                        res = await jsondata.json()
                    except:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["HentaiOther"]["JSONerror"], inline=False)
                        embed3.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

            em = discord.Embed(color=get_embeds.Common.COLOR)
            em.set_author(name=f"{self.client.user.name}",
                          icon_url=f"{self.client.user.avatar_url}")
            em.set_image(url=res['url'])
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


def setup(client: commands.Bot):
    client.add_cog(Hentai(client))
