import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefixes = ['/', '!', '$']

bot = commands.Bot(command_prefix=prefixes, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def calculate(ctx):
    try:
        equation = ctx.message.content.replace(f'{ctx.prefix}calculate', '')
        await ctx.send(f'{eval(equation)}')
    except:
        await ctx.send('There was a problem with the equation try again!')


bot.run(
    'YOUR_DISCORD_BOT_ID')
