import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def سڵاو(ctx):
    await ctx.send("سڵاڤ! ئەز بوتەکێ دیسکۆردی مە.")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
