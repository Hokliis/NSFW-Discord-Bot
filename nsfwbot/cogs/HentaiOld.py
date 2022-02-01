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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lesbian"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lesbian"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["anal"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["anal"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["anal"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["feet"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["feet"]["JSONerror"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["feet"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["hentai"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hentai"]["JSONerror"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hentai"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["boobs"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["boobs"]["JSONerror"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["boobs"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["tits"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["tits"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["tits"]["JSONerror"], inline=False)
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

    @commands.command(aliases=["bji"])
    async def blowjobi(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["blowjobi"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["blowjobi"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["blowjobi"]["JSONerror"], inline=False)
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
                async with pornSession.get(other_settings["HentaiCog"]["lewd"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewd"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewd"]["JSONerror"], inline=False)
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

    # @commands.command()
    # async def daddy(self, ctx):
    #     loading_message = await ctx.send(embed=self.please_wait_emb)
    #     try:

    #         em = discord.Embed(title="YOU LIL PERVERT!",
    #                            color=get_embeds.Common.COLOR)
    #         em.set_author(name=f"{self.client.user.name}",
    #                       icon_url=f"{self.client.user.avatar_url}")
    #         em.add_field(name="Lets have some fun shall we?", value="""Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""")
    #         em.set_footer(text=f"Requested by {ctx.author.name}")
    #         await loading_message.delete()
    #         await ctx.send(embed=em)

    #     except Exception as e:
    #         embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
    #                                description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
    #         embed3.set_author(name=f"{self.client.user.name}",
    #                           icon_url=f"{self.client.user.avatar_url}")
    #         embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
    #         embed3.add_field(
    #             name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
    #         embed3.set_footer(text=f"Requested by {ctx.author.name}")
    #         await loading_message.delete()
    #         await ctx.send(embed=embed3)

    # NEW

    @commands.command()
    async def hentaii(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["hentaii"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hentaii"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hentaii"]["JSONerror"], inline=False)
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
    async def yuri(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["yuri"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["yuri"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["yuri"]["JSONerror"], inline=False)
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
    async def erofeet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["erofeet"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erofeet"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erofeet"]["JSONerror"], inline=False)
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
    async def erok(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["erok"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erok"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erok"]["JSONerror"], inline=False)
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
    async def hololewd(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["hololewd"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hololewd"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["hololewd"]["JSONerror"], inline=False)
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
    async def lewdk(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["lewdk"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewdk"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewdk"]["JSONerror"], inline=False)
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
    async def keta(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["keta"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["keta"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["keta"]["JSONerror"], inline=False)
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
    async def eroyuri(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["eroyuri"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["eroyuri"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["eroyuri"]["JSONerror"], inline=False)
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
    async def pussyi(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["pussyi"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pussyi"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pussyi"]["JSONerror"], inline=False)
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
    async def pussy(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["pussy"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pussy"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pussy"]["JSONerror"], inline=False)
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
    async def cumi(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["cumi"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["cumi"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["cumi"]["JSONerror"], inline=False)
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
    async def cum(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["cum"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["cum"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["cum"]["JSONerror"], inline=False)
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
    async def spank(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["spank"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["spank"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["spank"]["JSONerror"], inline=False)
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
    async def lewdkemo(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["lewdkemo"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewdkemo"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["lewdkemo"]["JSONerror"], inline=False)
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

    # API endpoint has an issue
    # @commands.command()
    # async def smallboobs(self, ctx):
    #     loading_message = await ctx.send(embed=self.please_wait_emb)
    #     try:
    #         async with aiohttp.ClientSession() as pornSession:
    #             async with pornSession.get(other_settings["HentaiCog"]["smallboobs"]["APIlink"]) as jsondata:
    #                 if not 300 > jsondata.status >= 200:
    #                     embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
    #                                            description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
    #                     embed3.set_author(name=f"{self.client.user.name}",
    #                                       icon_url=f"{self.client.user.avatar_url}")
    #                     embed3.set_thumbnail(
    #                         url=get_embeds.ErrorEmbeds.THUMBNAIL)
    #                     embed3.add_field(
    #                         name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["smallboobs"]["StatusCodeError"], inline=False)
    #                     embed3.set_footer(
    #                         text=f"Requested by {ctx.author.name}")
    #                     await loading_message.delete()
    #                     await ctx.send(embed=embed3)
    #                     return

    #                 try:
    #                     res = await jsondata.json()
    #                 except:
    #                     embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
    #                                            description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
    #                     embed3.set_author(name=f"{self.client.user.name}",
    #                                       icon_url=f"{self.client.user.avatar_url}")
    #                     embed3.set_thumbnail(
    #                         url=get_embeds.ErrorEmbeds.THUMBNAIL)
    #                     embed3.add_field(
    #                         name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["smallboobs"]["JSONerror"], inline=False)
    #                     embed3.set_footer(
    #                         text=f"Requested by {ctx.author.name}")
    #                     await loading_message.delete()
    #                     await ctx.send(embed=embed3)
    #                     return

    #         em = discord.Embed(color=get_embeds.Common.COLOR)
    #         em.set_author(name=f"{self.client.user.name}",
    #                       icon_url=f"{self.client.user.avatar_url}")
    #         em.set_image(url=res['url'])
    #         em.set_footer(text=f"Requested by {ctx.author.name}")
    #         await loading_message.delete()
    #         await ctx.send(embed=em)

    #     except Exception as e:
    #         embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
    #                                description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
    #         embed3.set_author(name=f"{self.client.user.name}",
    #                           icon_url=f"{self.client.user.avatar_url}")
    #         embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
    #         embed3.add_field(
    #             name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
    #         embed3.set_footer(text=f"Requested by {ctx.author.name}")
    #         await loading_message.delete()
    #         await ctx.send(embed=embed3)

    @commands.command()
    async def avatar(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["avatar"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["avatar"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["avatar"]["JSONerror"], inline=False)
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
    async def soloi(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["soloi"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["soloi"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["soloi"]["JSONerror"], inline=False)
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
    async def solo(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["solo"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["solo"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["solo"]["JSONerror"], inline=False)
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
    async def ero(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["ero"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["ero"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["ero"]["JSONerror"], inline=False)
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
    async def eron(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["eron"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["eron"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["eron"]["JSONerror"], inline=False)
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
    async def erokemo(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["erokemo"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erokemo"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["erokemo"]["JSONerror"], inline=False)
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
    async def trap(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["trap"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["trap"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["trap"]["JSONerror"], inline=False)
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

    @commands.command(aliases=["bj"])
    async def blowjob(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["blowjob"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["blowjob"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["blowjob"]["JSONerror"], inline=False)
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
    async def holoero(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["holoero"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["holoero"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["holoero"]["JSONerror"], inline=False)
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
    async def gasm(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["gasm"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["gasm"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["gasm"]["JSONerror"], inline=False)
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
    async def futanari(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["futanari"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["futanari"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["futanari"]["JSONerror"], inline=False)
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
    async def pwank(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            async with aiohttp.ClientSession() as pornSession:
                async with pornSession.get(other_settings["HentaiCog"]["pwank"]["APIlink"]) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                               description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                        embed3.set_author(name=f"{self.client.user.name}",
                                          icon_url=f"{self.client.user.avatar_url}")
                        embed3.set_thumbnail(
                            url=get_embeds.ErrorEmbeds.THUMBNAIL)
                        embed3.add_field(
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pwank"]["StatusCodeError"], inline=False)
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
                            name=get_embeds.ErrorEmbeds.FIELD_NAME, value=other_embeds["pwank"]["StatusCodeError"], inline=False)
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
