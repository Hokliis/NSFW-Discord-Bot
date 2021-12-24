from random import randint as randomint

import discord
import aiohttp
from discord.ext import commands
from nsfwbot.database import get_embeds, get_main


class Pornlink(commands.Cog):
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


def setup(client: commands.Bot):
    client.add_cog(Pornlink(client))
