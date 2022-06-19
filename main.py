import os
import time
from keepAlive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix = 'p!')

@client.event
async def on_ready():
    print(f'>สำเร็จ')
    print(f'>ส่งโดย {client.user}')
    print(f'>by discord Patt#7777 ')

@client.event
async def on_message(message):
    await client.process_commands(message)

# Commands
@client.command()
async def sendm(ctx):
  while True:
    time.sleep(0.9)
    await ctx.channel.send("@everyone")

keep_alive()

token = os.environ['TOKEN']
client.run(token)
