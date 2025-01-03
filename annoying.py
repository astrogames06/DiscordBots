import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefixes = ['/', '!', '$']

bot = commands.Bot(command_prefix=prefixes, intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'yes' in message.content.lower():
        await message.channel.send('No')
    elif 'no' in message.content.lower():
        await message.channel.send('Yes')
    if 'maybe' in message.content.lower():
        await message.channel.send('😡')

    await bot.process_commands(message)


bot.run(
    'YOUR_DISCORD_BOT_ID')
