import discord
from discord.ext import commands

class test(commands.Cog, name="Test"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test123(self, ctx):
        await ctx.send("Success")

def setup(bot):
    bot.add_cog(test(bot))