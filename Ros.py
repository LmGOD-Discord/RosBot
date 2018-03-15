import discord
import asyncio
import platform
import traceback
from discord.ext import commands
from os import listdir
from os.path import isfile, join

import os
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    from utils import config
    token = config.token

client = discord.Client()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), pm_help=False)
bot.remove_command('help')
cogs_dir = "cogs"


@bot.event
async def on_ready():
    servidores_tot = str(len(bot.servers))
    usuarios_tot = str(len(set(bot.get_all_members())))
    permissoes = '8'
    link_convite = f'https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions={permissoes}'

    cor_links = '\033[4;34m'
    cor_verde_n = '\033[1;32m'
    cor_restaura = '\033[0;0m'

    print(f'')
    print(f'╔{"═" * 35}╦{"═" * 39}╦{"═" * 39}╗')
    print(f'║ Logado com Nickname: {bot.user.name:12} ║ Servidores conectados: {cor_verde_n}{servidores_tot:>3}{cor_restaura} servidores ║ Versão Discord.py: {discord.__version__:18} ║')
    print(f'║ Logado com ID: {bot.user.id:18} ║ Usuários conectados: {cor_verde_n}{usuarios_tot:>5}{cor_restaura} usuários   ║ Versão Python: {platform.python_version():22} ║')
    print(f'╠{"═" * 35}╩{"═" * 39}╩{"═" * 39}╣')
    print(f'║ Link de convite: {cor_links}{link_convite:^96}{cor_restaura} ║')
    print(f'╚{"═" * 35}═{"═" * 39}═{"═" * 39}╝')
    print(f'')

    await bot.change_presence(game=discord.Game(type=0, name="!ajuda | ON em {} servidores, para {} usuários!".format(servidores_tot, usuarios_tot)), status=discord.Status("dnd"))


if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
		try:
			bot.load_extension(cogs_dir + "." + extension)
			print(f'Extensão {extension} carregada com sucesso.')
		except Exception as e:
			print(f'Erro ao carregar a extensão {extension}.')
			traceback.print_exc()

bot.run(token)