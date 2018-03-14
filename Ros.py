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
    config.token

client = discord.Client()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), pm_help=False)
bot.remove_command('help')
cogs_dir = "cogs"


@bot.event
async def on_ready():
    usuarios_tot = str(len(bot.servers))
    servidores_tot = str(len(set(bot.get_all_members())))
    permissoes = '8'
    link_convite = f'https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions={permissoes}'

    print('')
    print('#================================================================================================================#')
    print(f'# Logado com Nickname: {bot.user.name} (ID: {bot.user.id})')
    print(f'# Link de convite: {link_convite}')
    print('#================================================================================================================#')
    print(f'# Servidores conectados: {usuarios_tot} servidores')
    print(f'# Usuários conectados: {servidores_tot} usuários')
    print('#================================================================================================================#')
    print(f'# Versão da biblioteca Discord.py: {discord.__version__}')
    print(f'# Versão da linguagem Python: {platform.python_version()}')
    print('#================================================================================================================#')
    print('')

    await bot.change_presence(game=discord.Game(type=0, name="!ajuda | ON em {} servidores, para {} usuários!".format(servidores_tot, usuarios_tot)), status=discord.Status("dnd"))


if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
		try:
			bot.load_extension(cogs_dir + "." + extension)
			print(f'Extensão {extension} carregada com sucesso.')
		except Exception as e:
			print(f'Erro ao carregar a extensão {extension}.')
			traceback.print_exc()

bot.run(config.token)