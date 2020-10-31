import discord
from discord.ext import commands
token = 'NzMwNjIwMDU3MzMxMzAyNDQw.XwdHfg.2461z7OylFYnTSjpuPny1G9ALv4'

#In decorator add a list titled aliases with a list of strings

bot = commands.Bot(command_prefix='!')

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


@bot.event
async def on_ready():
    print('Bot is ready.')



@bot.event
async def on_message(message):
    if message.content in get_list():
        await message.channel.purge(limit=1)
        await message.channel.send('You Used A Filtered Word!')
    await bot.process_commands(message)

@bot.command(name='addfilter')
async def addfilter(ctx, word):
    print('add filter works')
    if word not in get_list():
        write(word)
    elif word in get_list():
        await ctx.channel.send(f'The Word {word} is alrady in the filter')
@bot.command(name='filterlist')
async def filterlist(ctx):
    print('Filterlist works')
    await ctx.channel.send(f'The Words In The Filter Are: {str(get_list())}')


@bot.command(name='repeat')
async def repeat(ctx,*,input):
    print('Repeat works')
    await ctx.send(f'What You Just Said Was \n{input}!')
    
@bot.command(name='clear')
async def clear(ctx,*,amount=6):
    print('clear works')
    await ctx.channel.purge(limit=amount+1)




bot.run(token)
