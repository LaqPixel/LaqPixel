import discord
from discord.ext import commands
import asyncio
import traceback
import random

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="o!", intents=intents)

red = 0xd42a08
green = 0x0e8f37
blue = 0x0e218f
lightblue = 0x11c7d4
lightgreen = 0x14d411
purple = 0x9f1cb0
yellow = 0xe0e031
orange = 0xd49639
pink = 0xeb21d3

TOKEN = 'ODI3NTQ5NDgzODkzNjUzNTM0.YGcphA.qYUPTcmq0iFBEpKWiEpf5KfuEMo' #Don't share!


@client.event
async def on_ready():
    print("ORP bot is of course ready")
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('o!help'))
        await asyncio.sleep(random.randint(7, 10))
        await client.change_presence(activity=discord.Game('made by the best coders'))
        await asyncio.sleep(random.randint(7, 10))

cogs = ['cogs.welcome', 'cogs.help']

if __name__ == '__main__':
    for cog in cogs:
        try:
            client.load_extension(cog)
        except Exception as e:
            print(f'failed to load {cog}')
            traceback.print_exc()

client.run(TOKEN)
