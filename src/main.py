import discord
import os
from ui.UserInterface import UserInterface

TOKEN = os.environ['WEREWOLF_TOKEN']
UI = None

client = discord.Client()

@client.event
async def on_ready():
    print("Efetuamos o login como {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await UI.handle_message(message)


def main():
    global UI

    UI = UserInterface()

    client.run(TOKEN)

if __name__ == '__main__':
    main()