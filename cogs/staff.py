import discord, argparse, re, shlex, traceback, io, textwrap, asyncio
from discord.ext import commands
from utils import checks
from contextlib import redirect_stdout
from collections import Counter


class Staff:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(guild_only=True, pass_context=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        """Kicka um membro do servidor."""
        try:
            if ctx.message.author.server_permissions.kick_members:
                await self.bot.kick(member)
                await self.bot.say(f'O membro {member.mention} foi kickado do servidor por {ctx.message.author.mention}')
                await self.bot.message
            else:
                await self.bot.say('Você não possui permissão para usar esse comando.')
        except discord.Forbidden:
            await self.bot.say('Não possuo permissão para kickar o membro {}.'.format(member.mention))
        except discord.BadArgument:
            await self.bot.say('O membro {} não foi encontrado.'.format(member))


def setup(bot):
    bot.add_cog(Staff(bot))