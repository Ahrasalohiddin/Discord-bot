import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot.run('MTIxMDI1MTk2NjA4OTkyMDUzMg.G1-YiQ.5Ts5UGQNV3DoKJ79Ibxk6sTg2pFGAUxRcpH_Yw')