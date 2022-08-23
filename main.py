import discord

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('?fetchIds'):
        for user in message.guild.members:
            print(user.id)

client.run('token')
