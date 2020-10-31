import discord
from discord.ext import commands
token = "a"

#In decorator add a list titled aliases with a list of strings

client = commands.Bot(command_prefix='!')




@client.event
async def on_ready():
    print('Bot is ready.')



@client.event
async def on_message(message):
    if message.content in get_list():
        await message.channel.purge(limit=1)
        await message.channel.send('You Used A Filtered Word!')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


def get_list():
    a_file = open("filterlist.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
        x = []
        for i in list_of_lists:
            x.append(i[0])
    a_file.close()
    return(x)

def write(word):
    x = open('filterlist.txt', 'a')
    x.write('\n'+word)
    x.close()

client.run(token)
