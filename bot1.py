import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.message import Message
from discord.server import Server
from discord.channel import Channel, ChannelType

BOT_PREFIX = ("?", "!")
TOKEN = 'NDY2MTQ1NzU3MjgwMzM3OTIw.DiX3dA.r5-8Q01tEws2t83feMoB39ZXkWE'

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command(pass_context=True)
async def haha(ctx):
    await client.say(r'haha' + 'haha' * 20, tts=True)


@client.command(name='pm',
                pass_context=True)
async def pm(context):
    await client.send_message(context.message.author, content="hello>?")


@client.command(name='join',
                pass_context=True)
async def join(context: Context):
    vc = await client.join_voice_channel(context.message.author.voice_channel)


@client.command(name='leave',
                pass_context=True)
async def leave(ctx):
    for x in client.voice_clients:
        if x.server == ctx.message.server:
            return await x.disconnect()

    return await client.say("I am not connected to any voice channel on this server!")


@client.event
async def on_message(message):
    await client.say(message.content, tts=True)


@client.event
async def on_ready():
    # await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(60)


client.loop.create_task(list_servers())
client.run(TOKEN)
