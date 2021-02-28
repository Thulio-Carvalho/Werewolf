class CommandHandler:
    def __init__(self, prefix):
        self.PREFIX = prefix

    async def ping(self, message):
        await message.channel.send('Pong!')