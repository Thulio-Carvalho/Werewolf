import json
from ui.CommandHandler import CommandHandler

CONFIG_FILE = 'ui/config.json'

class UserInterface:
    def __init__(self):
        self.__initial_config()
    
    def __initial_config(self):
        
        with open(CONFIG_FILE, "r") as f:
            self.config = json.load(f)

        self.PREFIX = self.config['prefix']
        self.COMMAND_HANDLER = CommandHandler(self.PREFIX)

    def __should_handle_message(self, message):
        ret = False
        if message.content.startswith(self.PREFIX):
            ret = True
        return ret

    async def handle_message(self, message):
        if self.__should_handle_message(message):
            content = message.content[len(self.PREFIX):]

            if content.startswith('ping'):
                await self.COMMAND_HANDLER.ping(message)
            