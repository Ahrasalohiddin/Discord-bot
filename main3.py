import discord
from discord.ext import commands
import os, random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

bot.run('MTIxMDI1MTk2NjA4OTkyMDUzMg.GJUOw-.4aWUP7YPwZjUjVQkGa9W06Mjd4WDyMm8njPICQ')

