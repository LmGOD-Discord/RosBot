import discord
import asyncio
import platform
from discord.ext import commands

import os
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import config
    config.token

#startup_extensions = ["cogs/comandos"]
bot = commands.Bot(description='Estou aqui para lhe servir! =]', command_prefix=commands.when_mentioned_or('!'), pm_help=False)


@bot.event
async def on_ready():
    print('')
    print('#=================================================================================#')
    print('# Logado com Nickname: {}'.format(bot.user.name))
    print('# Logado com ID: {}'.format(bot.user.id))
    print('#=================================================================================#')
    print('# Servidores conectados: {} servidores.'.format(str(len(bot.servers))))
    print('# Usuários conectados: {} usuários.'.format(str(len(set(bot.get_all_members())))))
    print('#=================================================================================#')
    print('# Versão da biblioteca Discord.py: {}'.format(discord.__version__))
    print('# Versão da linguagem Python: {}'.format(platform.python_version()))
    print('#=================================================================================#')
    print('')


'''@bot.command()
async def load(extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command()
async def unload(extension_name: str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


class Main_Commands():
    def __init__(self, bot):
        self.bot = bot


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}. {}'.format(extension, exc))'''

bot.run(config.token)