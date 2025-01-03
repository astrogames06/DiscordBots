import openai, os
from openai import OpenAI

import discord
from discord.ext import commands

client = OpenAI(
  api_key='YOUR_API_KEY',
)

intents = discord.Intents.default()
intents.message_content = True

prefixes = ['/', '!', '$']

bot = commands.Bot(command_prefix=prefixes, intents=intents)

def chat_with_gpt(response):
    completion = client.chat.completions.create(
        model="gpt-4o",
        user="asst_IftBSHE1ZeKKDaHFEja8XuVd",
        messages=[{"role": "user", "content": response}]
    )

    return completion.choices[0].message.content

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def GPT(ctx):
    response = chat_with_gpt(ctx.message.content.replace("!GPT", ""))
    await ctx.send(response)


bot.run(
    'YOUR_DISCORD_BOT_ID')