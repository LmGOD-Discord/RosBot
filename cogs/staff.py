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
                embedkick.add_field(name='\nMembro: ', value = member.mention, inline=False)
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
                embedban.add_field(name='\nMembro: ', value = member.mention, inline=False)
                embedban.add_field(name='Staff: ', value = autor.mention, inline=False)
                embedban.add_field(name='Motivo: ', value = reason, inline=False)

                await self.bot.say(embed=embedban)

            except discord.Forbidden:
                await self.bot.say(f'{autor.mention}, eu não possuo permissão para banir o membro {member.mention}.')
        else:
            await self.bot.say(f'{autor.mention}, você não possui permissão para usar esse comando.')
        
    @commands.command(guild_only=True, pass_context=True, aliases=['rename'])
    async def renomear(self, ctx, member : discord.Member, *, nickname =""):
        """Altera o apelido de um membro"""
        nickantigo = member.display_name
        autor = ctx.message.author

        if ctx.message.author.server_permissions.manage_nicknames:
            if nickname == "":
                nickname = None
            try:
                await self.bot.change_nickname(member, nickname)
                
                embednick = discord.Embed(title='O apelido de um membro foi alterado no servidor!')
                embednick.add_field(name='Nick antigo: ', value = nickantigo)
                embednick.add_field(name='Nick atual: ', value = member.mention)
                embednick.add_field(name='Alterado pelo Staff: ', value = autor.mention, inline=False)
                
                await self.bot.say(embed=embednick)

            except discord.Forbidden:
                await self.bot.say(f'{autor.mention}, eu não possuo permissão para alterar o apelido do membro {member.mention}.')

            except discord.HTTPException:
                await self.bot.say(f'Não é possível alterar o apelido para o mesmo apelido.')

        else:
            await self.bot.say(f'{autor.mention}, você não possui permissão para usar esse comando.')

def setup(bot):
    bot.add_cog(Staff(bot))