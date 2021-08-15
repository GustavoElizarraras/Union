import discord
from discord.ext import commands, tasks

client = discord.Client()
bot = commands.Bot(command_prefix='!')

target_channel_id = 876304013975519259

@tasks.loop(minutes=1)
async def called_every_min():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")

@called_every_min.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello world, first discord bot")

@bot.command(pass_context=True)
async def broadcast(ctx, *, msg):
    for server in bot.servers:
        for channel in server.channels:
            try:
                await bot.send_message(channel, msg)
            except Exception:
                continue
            else:
                break
            
called_every_min.start()            
client.run("ODc2Mjk4OTQ3NDE1NjYyNjUz.YRiC_Q.qED2aVic72pg1UKiQQg6mgOakVM")

