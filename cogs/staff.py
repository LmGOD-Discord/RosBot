import discord, argparse, re, shlex, traceback, io, textwrap, asyncio
from discord.ext import commands
#from utils import checks
from contextlib import redirect_stdout
from collections import Counter


class Staff:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(guild_only=True, pass_context=True)
    async def an(self, ctx, *, msg: str, channel: discord.Channel=None):
        '''Diz a mensagem em forma de anúncio!'''
        canal = channel or ctx.message.channel
        await self.bot.say(canal, 'Você disse: {}'.format(msg))

def setup(bot):
    bot.add_cog(Staff(bot))