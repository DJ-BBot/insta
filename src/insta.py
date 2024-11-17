import discord
from discord.ext import commands
import re
import signal
import sys

# set up the bot with necessary command prefix
intents = discord.Intents.default()

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command(name="insta")
async def insta(ctx, url: str) -> None:
    # RE to match and validate an instagram URL
    insta_pattern = re.compile(r"https?://(www\.)?instagram\.com/.*")

    if insta_pattern.match(url):
        modified_url = url.replace("instagram.com","ddinstagram.com")
        await ctx.send(f'Modified URL: {modified_url}')
    else:
        await ctx.send(f'URL: {url}')

def get_bot_token() -> str:
    import os
    env_name = "BOT_TOKEN"
    bot_token = os.environ.get(env_name) if env_name in os.environ.keys() else ""
    if bot_token == "":
        raise RuntimeError("BOT_TOKEN not present in environment variables")

def handler(signum, frame):
    print("Finished executing for all time!")
    sys.exit(0)

# Run the bot
try:
    signal.signal(signal.SIGALRM, handler)
    #signal.alarm(21_580) # run for 6 hours, less 20 seconds.
    signal.alarm(10) # run for 6 hours, less 20 seconds.
    bot.run(get_bot_token())
except Exception as e:
    print(str(e))
    sys.exit(1) # execution failed
