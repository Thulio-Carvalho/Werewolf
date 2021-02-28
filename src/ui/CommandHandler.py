import json

class CommandHandler:
    def __init__(self, prefix):
        self.PREFIX = prefix
    
    def __entrypoint(self, message):
        self.message = message
        self.channel = message.channel

    def __get_parameters(self, message, min_parameters=0):
        parameters = message.content.split(' ')[1:]
        if len(parameters) < min_parameters:
            raise Exception('Not enough parameters')
        return parameters

    async def __send_usage(self, func, parameters=[]):
        msg = 'USAGE: ' + self.PREFIX + func + ' '
        msg += ' '.join(('<' + param + '>') for param in parameters)
        await self.channel.send(msg)

    async def ping(self, message):
        self.__entrypoint(message)

        await self.channel.send('Pong!')

    async def info(self, message):
        self.__entrypoint(message)

        ## Won't work for more than one speciality. Intended.
        speciality = None
        try:
            speciality = self.__get_parameters(message, min_parameters=1)[0]
        except Exception:
            await self.__send_usage('info', ['speciality'])

        with open('ui/messages.json', 'r') as f:
            messages = json.load(f)
        
        if speciality not in messages:
            await self.channel.send("This speciality was not yet implemented.")

        info = messages[speciality]['info']

        await self.channel.send(info)