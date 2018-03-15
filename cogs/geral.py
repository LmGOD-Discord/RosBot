import discord, argparse, re, shlex, traceback, io, textwrap, asyncio
from datetime import datetime, timedelta
from discord.ext import commands
from utils import checks
from contextlib import redirect_stdout
from collections import Counter


class Geral:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(guild_only=True, pass_context=True)
    async def ping(self, ctx):
        """Mostra a latência do BOT até o servidor."""
        d = datetime.utcnow() - ctx.message.timestamp
        s = d.seconds * 1000 + d.microseconds // 1000
        await self.bot.say(f':ping_pong: Pong! Meu ping atual é de {s}ms.')

    
    @commands.command(guild_only=True, pass_context=True)
    async def votar(self, ctx, *, msg: str):        
        botmsg = await self.bot.say(msg)
        await self.bot.delete_message(ctx.message)
        await self.bot.add_reaction(botmsg, '✅')
        await self.bot.add_reaction(botmsg, '❌') 


def setup(bot):
    bot.add_cog(Geral(bot))