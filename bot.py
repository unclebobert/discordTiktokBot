import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests


load_dotenv()

intents = discord.Intents(guilds=True, messages=True, message_content=True)
bot = commands.Bot(intents=intents, command_prefix='+')


@bot.hybrid_command()
async def embed(ctx: commands.Context):
    async for msg in ctx.channel.history(limit=5):
        link = msg.content
        if link.startswith('https://vt.tiktok.com/'):
            real = requests.head(link).headers['location']
            await ctx.send(real, ephemeral=True)
            return

    await ctx.send('No tiktok links found within the last 5 messages', ephemeral=True)
    return

bot.tree.sync()
bot.run(os.getenv('TOKEN'))
