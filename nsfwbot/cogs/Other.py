import discord
import requests
import textwrap
import urllib
import aiohttp
import datetime
from discord.ext import commands
from nsfwbot.database import get_embeds, get_main


class Other(commands.Cog):
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
    async def lesbian(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/les') as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                        icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    res = await jsondata.json()

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
    
    @commands.command()
    async def anal(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/anal') as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                        icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    res = await jsondata.json()

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
    
    @commands.command()
    async def feet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/feetg') as jsondata: # feetg for gif
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                        icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    res = await jsondata.json()

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
    
    @commands.command()
    async def feet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/Random_hentai_gif') as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                        icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"Bad status code from API", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        return

                    res = await jsondata.json()

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
    client.add_cog(Other(client))
