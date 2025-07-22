import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name="ping")
async def ping(context):
    await context.send("Pong")

bot.run("")

# stable_version
# |                     \          \
# stable_version         pong       ping
# |                    /
# stable_version