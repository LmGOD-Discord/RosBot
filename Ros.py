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
    import config
    config.token

client = discord.Client()
bot = commands.Bot(description='Estou aqui para lhe servir! =]', command_prefix=commands.when_mentioned_or('!'), pm_help=False)
bot.remove_command('help')
cogs_dir = "cogs"


@bot.event
async def on_ready():
    usuarios_tot = str(len(bot.servers))
    servidores_tot = str(len(set(bot.get_all_members())))
    permissoes = '8'
    link_convite = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions={}'.format(bot.user.id, permissoes)

    print('')
    print('#================================================================================================================#')
    print('# Logado com Nickname: {} (ID: {})'.format(bot.user.name, bot.user.id))
    print('# Link de convite: {}'.format(link_convite))
    print('#================================================================================================================#')
    print('# Servidores conectados: {} servidores.'.format(usuarios_tot))
    print('# Usuários conectados: {} usuários.'.format(servidores_tot))
    print('#================================================================================================================#')
    print('# Versão da biblioteca Discord.py: {}'.format(discord.__version__))
    print('# Versão da linguagem Python: {}'.format(platform.python_version()))
    print('#================================================================================================================#')
    print('')

    await bot.change_presence(game=discord.Game(type=0, name="!ajuda | ON em {} servidores, para {} usuários".format(servidores_tot, usuarios_tot)), status=discord.Status("dnd"))

if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
		try:
			bot.load_extension(cogs_dir + "." + extension)
			print(f'Extensão {extension} carregada com sucesso.')
		except Exception as e:
			print(f'Erro ao carregar a extensão {extension}.')
			traceback.print_exc()

bot.run(config.token)