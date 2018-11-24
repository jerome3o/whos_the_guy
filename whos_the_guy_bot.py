# Work with Python 3.6
import discord
from discord.message import Message
import asyncio
from random import randint
from roe_model import get_screen_shot_path
from os import walk

# invite: https://discordapp.com/oauth2/authorize?client_id=515762398637064192&scope=bot

BOT_PREFIX = ("?", "!")
TOKEN = 'NTE1NzYyMzk4NjM3MDY0MTky.Dtp1Ng.uoOn7fFEz0NQCEkGD9CToj4kGhw'


client = discord.Client()

@client.event
async def on_message(message: Message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!wtg'):
        content = message.content  # type: str
        args = content.split(' ')
        names = []
        print(args)
        if len(args) > 1:
            if args[1] == 'add':
                names = args[2:]
        if message.author.voice_channel:
            for person in message.author.voice_channel.voice_members:
                names.append(person.name)

        msg = f"Potential guys: {', '.join(names)}"
        await client.send_message(message.channel, msg)

        the_guy = names[randint(0, len(names) - 1)]
        msg = f"{the_guy} is the guy."
        await client.send_message(message.channel, msg)

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