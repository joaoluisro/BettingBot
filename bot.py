import discord
from discord.ext import commands

class BetClient(commands.Bot(command_prefix="-")):
    async def on_ready(self):
        print('We have logged in as {0.user}', self.user)

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

client = BetClient()
client.run('Nzk4NjUzMjExODU0NjM1MDU4.X_4Jww.9IXxIlLBdBeS1vBGo3uNr2lkoZk')
