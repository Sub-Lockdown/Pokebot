#!/usr/bin/env python3

# Import Python Modules
from dotenv import load_dotenv
import os
import discord
import sys
import logging

# Checks if .env exists, and creates one if it doesn't
if os.path.isfile('.env') is False:
    with open('.env', 'w') as f:
        f.write('# .env\n')
        f.write('DISCORD_TOKEN=\n')
        f.write('DISCORD_GUILD=\n')
        f.write('DISCORD_ADMINS=\n')
    quit()
else:
    # Adds the variables from .env to enviromental variables
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    ADMINS = os.getenv('DISCORD_ADMINS').split(',')

# Setting intents to default, and allow access to message content
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Admin Commands
    if message.author.name in ADMINS:

        # Run a new iteration of the current script, providing any command line args 
        if message.content.startswith('$hello'):
            await message.channel.send('Restarting')
            python = sys.executable
            os.execl(python, python, * sys.argv)

    print(f'{message.author.name}: {message.content}')

if __name__ == "__main__":
    print("This file contains the basic discord bot functions")
    sys.exit()