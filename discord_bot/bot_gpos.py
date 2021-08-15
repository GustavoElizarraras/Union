import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os 
from random import randint

load_dotenv()
token = os.getenv('token')
bot = commands.Bot(command_prefix='!')

# Discord channel for each server
channel_name = "planificación-de-sesiones"

# Hour blocks identified by numbers
schedules = {
    1:"7:00-8:30",
    2:"8:30-10:00",
    3:"10:00-11:30",
    4:"11:30-13:00",
    5:"13:00-14:30",
    6:"14:30-16:00",
    7:"16:00-17:30",
    8:"17:30-19:00",
    9:"19:00-20:30"
}



# Actions for starting the Bot, show name and ID
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

# Repeating a task each time
@tasks.loop(seconds=30.0)
async def called_every_min():
    for server in bot.guilds:
        hours = (randint(1, 9), randint(1, 9))
        print(dir(server))
        for channel in server.channels:
            if channel.name == "planificación-de-sesiones":
                print("Ahora estoy en:", channel)
                await channel.send(F"En el horario de {schedules[hours[0]]} y {schedules[hours[1]]} tendremos una hora de estudio")

# Validating the bot is online, before the time loop
@called_every_min.before_loop
async def before():
    print("waiting")
    await bot.wait_until_ready()

# Test function to intereact with a particular message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("$mello"):
        await message.channel.send("Hello world, first discord bot")

bot.loop.create_task(before())            
called_every_min.start()            
bot.run(token)

