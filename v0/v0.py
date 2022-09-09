import discord

TOKEN = '######################################'

#Channel IDs
LB_general = '######################'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if user_message.lower() in ['hello','hi']:
        await message.channel.send(f'Hello {message.author.mention}!')
        return

@client.event
async def on_member_join(member):
    channel = client.get_channel(LB_general)
    await channel.send(f'Welcome {member.mention}! [Placeholder Text, will add the specific text here]')

client.run(TOKEN)
