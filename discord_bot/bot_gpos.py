import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os 

load_dotenv()
token = os.getenv('token')
bot = commands.Bot(command_prefix='!')

channel_name = "planificación-de-sesiones"

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    for server in bot.guilds:
        print(server)
        for channel in server.channels:
            if channel.name == "planificación-de-sesiones":
                print("Ahora estoy en:", channel)

@tasks.loop(seconds=30.0)
async def called_every_min():
    for server in bot.guilds:
        print(server)
        for channel in server.channels:
            if channel.name == "planificación-de-sesiones":
                print("Ahora estoy en:", channel)
                await channel.send("Your message")


@called_every_min.before_loop
async def before():
    print("waiting")
    await bot.wait_until_ready()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$mello"):
        await message.channel.send("Hello world, first discord bot")

bot.loop.create_task(before())            
called_every_min.start()            
bot.run(token)

