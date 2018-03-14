import discord, argparse, re, shlex, traceback, io, textwrap, asyncio
from discord.ext import commands
from utils import checks
from contextlib import redirect_stdout
from collections import Counter


class Staff:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(guild_only=True, pass_context=True)
    async def kick(self, ctx, member: discord.Member, *, reason = 'Nenhum motivo determinado.'):
        """Kicka um membro do servidor."""
        autor = ctx.message.author

        try:
            if ctx.message.author.server_permissions.kick_members:
                await self.bot.kick(member)
                
                embedkick = discord.Embed(title='Um membro foi expulso do servidor!')
                embedkick.add_field(name='Membro: ', value = member.mention, inline=False)
                embedkick.add_field(name='Staff: ', value = autor.mention, inline=False)
                embedkick.add_field(name='Motivo: ', value = reason, inline=False)

                await self.bot.say(embed=embedkick)
            else:
                await self.bot.say(f'{autor.mention}, você não possui permissão para usar esse comando.')
        
        except discord.Forbidden:
            await self.bot.say(f'{autor.mention}, eu não possuo permissão para kickar o membro {member.mention}.')

        
    @commands.command(guild_only=True, pass_context=True)
    async def ban(self, ctx, member: discord.Member, *, reason = 'Nenhum motivo determinado.'):
        """Ban um membro do servidor."""
        autor = ctx.message.author

        if ctx.message.author.server_permissions.unban_members:
            try:
                await self.bot.ban(member)
                
                embedban = discord.Embed(title='Um membro foi banido do servidor!')
                embedban.add_field(name='Membro: ', value = member.mention, inline=False)
                embedban.add_field(name='Staff: ', value = autor.mention, inline=False)
                embedban.add_field(name='Motivo: ', value = reason, inline=False)

                await self.bot.say(embed=embedban)

            except discord.Forbidden:
                await self.bot.say(f'{autor.mention}, eu não possuo permissão para banir o membro {member.mention}.')
        else:
            await self.bot.say(f'{autor.mention}, você não possui permissão para usar esse comando.')
        
        


    @commands.command(guild_only=True, pass_context=True)
    async def unban(self, ctx, member: discord.Member, *, reason = 'Nenhum motivo determinado.'):
        """Unban um membro do servidor."""
        autor = ctx.message.author
            
        if ctx.message.author.server_permissions.unban_members:
            try:
                await self.bot.unban(member)
                
                embedunban = discord.Embed(title='Um membro foi desbanido do servidor!')
                embedunban.add_field(name='Membro: ', value = member.mention, inline=False)
                embedunban.add_field(name='Staff: ', value = autor.mention, inline=False)
                embedunban.add_field(name='Motivo: ', value = reason, inline=False)

                await self.bot.say(embed=embedunban)
        
            except discord.Forbidden:
                await self.bot.say(f'{autor.mention}, eu não possuo permissão para desbanir o membro {member.mention}.')
        else:
            await self.bot.say(f'{autor.mention}, você não possui permissão para usar esse comando.')

def setup(bot):
    bot.add_cog(Staff(bot))