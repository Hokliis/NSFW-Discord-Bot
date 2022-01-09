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
                        res = await jsondata.json()
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
                        res = await jsondata.json()
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
                # feetg for gif
                async with pornSession.get(f'https://nekos.life/api/v2/img/feetg') as jsondata:
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
                        res = await jsondata.json()
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
    async def hentai(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/Random_hentai_gif') as jsondata:
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
                        res = await jsondata.json()
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
    async def boobs(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/boobs') as jsondata:
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
                        res = await jsondata.json()
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
    async def tits(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/tits') as jsondata:
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
                        res = await jsondata.json()
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
    async def blowjob(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/blowjob') as jsondata:
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
                        res = await jsondata.json()
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
    async def lewd(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(f'https://nekos.life/api/v2/img/nsfw_neko_gif') as jsondata:
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
                        res = await jsondata.json()
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
    async def daddy(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:

            em = discord.Embed(title="YOU LIL PERVERT!",
                               color=get_embeds.Common.COLOR)
            em.set_author(name=f"{self.client.user.name}",
                          icon_url=f"{self.client.user.avatar_url}")
            em.add_field(name="Lets have some fun shall we?", value="""Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""")
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
