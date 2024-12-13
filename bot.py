import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests


load_dotenv()

intents = discord.Intents(guilds=True, messages=True, message_content=True)
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.slash_command(name='embed', guild_ids=[])
async def embed(ctx: discord.ApplicationContext):
    async for msg in ctx.history(limit=5):
        link = msg.content
        if link.startswith('https://vt.tiktok.com/'):
            real = requests.head(link).headers['location']
            await ctx.respond(real, ephemeral=True)
            return

    await ctx.respond(
        'No tiktok links found within the last 5 messages',
        ephemeral=True
    )
    return


@bot.slash_command(name='e', guild_ids=[325465792210665474, 1135514799556526171])
async def embed_special(ctx: discord.ApplicationContext):
    async for msg in ctx.history(limit=5):
        link = msg.content
        if link.startswith('https://vt.tiktok.com/'):
            real = requests.head(link).headers['location']
            await ctx.respond(real, ephemeral=True)
            return

    await ctx.respond(
        'No tiktok links found within the last 5 messages',
        ephemeral=True
    )
    return


bot.run(os.getenv('TOKEN'))
