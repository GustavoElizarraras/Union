import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os 

load_dotenv()
token = os.getenv('token')
client = discord.Client()
bot = commands.Bot(command_prefix='!')


target_channel_id = 876304013975519255

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@tasks.loop(seconds=10.0)
async def called_every_min():
    message_channel = client.get_channel(target_channel_id)
    print(message_channel)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")

@called_every_min.before_loop
async def before():
    print("waiting")
    await client.wait_until_ready()
    print(client.get_channel(target_channel_id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$mello"):
        await message.channel.send("Hello world, first discord bot")



# @bot.command(pass_context=True)
# async def broadcast(ctx, *, msg):
#     for server in bot.servers:
#         for channel in server.channels:
#             try:
#                 await bot.send_message(channel, msg)
#             except Exception:
#                 continue
#             else:
#                 break
client.loop.create_task(before())            
called_every_min.start()            
client.run(token)

