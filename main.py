import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def oyun(ctx):
    await ctx.send(f'Merhaba ben ')
    await ctx.send(f'karton hangi kutuya konur a/kağıt kutusu b/cam c/metal')
    @bot.command()
    async def a(ctx):
        await ctx.send(f'aferin')
bot.run("MTE0NDY1OTY2ODgyODk1MDU4OQ.GVk-K5.ZEjyGH2qlao73Yb6mxs3l7P5ZhNpM30BKUMels")
