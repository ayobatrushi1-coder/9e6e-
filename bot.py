import discord
from discord.ext import commands
import os

# دروستکرنا بوتێ ب پێشگرێ !
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------")

# فەرمانا !hello
@bot.command()
async def hello(ctx):
    await ctx.send("سڵاو! من بوتەکەم و بە سەرکەوتوویی لەسەر ڕەیلۆ کار دەکەم! 🤖✨")

# وەرگرتنا تۆکنی بوتەکەی خۆت لە Variablesـی ڕەیلۆ
# دڵنیابە کە لە ڕەیلۆ متەمەممەی DISCORD_TOKEN دابنێیت
bot.run(os.getenv("DISCORD_TOKEN"))
