# Work with Python 3.6
import discord
import asyncio
from roe_model import get_screen_shot_path
from os import walk


BOT_PREFIX = ("?", "!")
TOKEN = 'NDY2MTQ1NzU3MjgwMzM3OTIw.DiX3dA.r5-8Q01tEws2t83feMoB39ZXkWE'


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!roe'):
        msg = 'Yeah gidday {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        # Rewrite
        with open(get_screen_shot_path(), 'rb') as picture:
            await client.send_file(message.channel, picture)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print()
        await asyncio.sleep(60)


client.loop.create_task(list_servers())
client.run(TOKEN)