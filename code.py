import discord
import asyncio
import random
import os
from discord.ext import commands
from discord.ext.commands.core import dm_only


client = commands.Bot(command_prefix='.')


TOKEN = 'OTI3NzYyNjcwNjA4ODc1NTMx.YdO8UQ.UpttaqaD_HEd_R4jGDuV5k6xGNw'


@client.event
async def on_ready():
    print('Bot Is Succesfully Online and Can be Used Now!')
    await statuschange()
    client.loop.create_task(statuschange())


@client.event
async def statuschange():
    await client.wait_until_ready()
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="discord.py   |.help"))
        await asyncio.sleep(5)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! My Current Ping is {round(client.latency * 1000)}')


@ client.command()
async def say(ctx, *, message):
    await ctx.send(message)


client.run(TOKEN)
