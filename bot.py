import discord
from discord.ext import commands

prefix = ["!","."]#bu şekilde kolayca prefix eklenebiliyor. Tek prefix olmasını istiyorsanız şu şekilde yapabilirsiniz: prefix = ["!"]

bot = commands.Bot(command_prefix=prefix)

print("Lütfen bekleyiniz...")

@bot.event
async def on_ready():     
    print("Bot aktif!")
    print("Bot ismi: "  + bot.user.name)
    print("Bot ID'si: " + str(bot.user.id))

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pingim: {round(bot.latency * 1000)}ms")

bot.run("buraya botunuzun tokenini girin")
