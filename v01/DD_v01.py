from DD_v01_complete import the_list
import discord

TOKEN = '##################################################'

#Channel IDs
LB_general = '###################'
LB_welcome = '###################'


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} ({channel}) {type(user_message)}')

    if message.author == client.user:
        return
    
    elif user_message.lower() in ['hello','hi']:
        await message.channel.send(f'Hello {message.author.mention}!')
        return

    elif  message.content == '/POAPs':

        link = message.content
        final_list = the_list(link)

        for i in range(len(final_list)):
            recipient = int(final_list[i][0])
            user = client.get_user(recipient)

            await user.send(f"Hello! Here's your POAP link! {final_list[i][1]}")

        return

@client.event
async def on_member_join(member):
    channel = client.get_channel(LB_general)
    await channel.send(f'Welcome {member.mention}! Please introduce yourself in {channel(LB_welcome)}!')

client.run(TOKEN)
