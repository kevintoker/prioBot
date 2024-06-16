from typing import Final
import os
import discord
from discord import Client, Intents, Message
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Select
import discord
from discord.ext import commands
import json

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(os.getcwd())
os.path.dirname(os.path.abspath(__file__))
with open("./discord_bot/links.json", 'r') as j:
    contents = json.loads(j.read())

print(contents)


bot: commands.Bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot has connected to Discord!")

@bot.command()
async def dbind(ctx: commands.Context):
    embed = discord.Embed(title = 'Defensive Bind Lineups', description=f'Here are the lineups for each relevant agent:', color = discord.Color.dark_orange(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name ="Viper", value = "[A Site Showers One Way Orb](https://www.youtube.com/watch?v=KaK4ABhI2h0)\n [A Site Spam Orb (From B)](https://www.youtube.com/watch?v=rpza3hGNv0w)\n [Default Viper Wall](https://www.youtube.com/watch?v=rAOE4pBpRlU)\n [A Site Stall Molly](https://www.youtube.com/watch?v=SjEnYW_jicE)\n [A Site Stall Molly (From B)](https://www.youtube.com/watch?v=FFN7nEGEHYE)\n [B Site Stall Molly](https://www.youtube.com/watch?v=j50LIrZN5SU)\n [B Site Stall Molly (From A)](https://www.youtube.com/watch?v=vR_RFuomI_Y)")
    embed.add_field(name ="Brimstone", value = "[A Site Stall Molly](https://www.youtube.com/watch?v=SjEnYW_jicE)\n [A Site Stall Molly (From B)](https://www.youtube.com/watch?v=FFN7nEGEHYE)\n [B Site Stall Molly](https://www.youtube.com/watch?v=j50LIrZN5SU)\n [B Site Stall Molly (From A)](https://www.youtube.com/watch?v=vR_RFuomI_Y)")
    embed.add_field(name ="KAY/O", value = "[A Site Stall Molly](https://www.youtube.com/watch?v=Go_MMFtgAmo)\n [A Site Stall Molly (From B)](https://www.youtube.com/watch?v=nHuEPFCUT0M)\n [B Site Cubby Molly](https://www.youtube.com/watch?v=lqQrqO03nfs)\n [B Site Stall Molly](https://www.youtube.com/watch?v=T82Zd-TixrU)\n [A Site Showers Knife](https://www.youtube.com/watch?v=Vcgf70mIzVo)\n [A Site Short Knife (From B)](https://www.youtube.com/watch?v=4lzDIulcT0E)\n [A Site Market Knife (From B)](https://www.youtube.com/watch?v=fLC6YzMRZi0)\n [A Site Showers Knife (From B)](https://www.youtube.com/watch?v=7kDx8yj4jRA)\n [B Site Fountain Knife](https://www.youtube.com/watch?v=K-HXON7vOhQ)\n [B Site Sands Knife](https://www.youtube.com/watch?v=sNwTAinero8)")
    await ctx.send(embed = embed)

@bot.command()
async def obind(ctx: commands.Context):
    embed = discord.Embed(title = 'Offensive Bind Lineups', description=f'Here are the lineups for each relevant agent:', color = discord.Color.dark_orange(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name ="Viper", value = "[A Site U-Hall Orb](https://www.youtube.com/watch?v=AdOAIWAd704)\n [A Site Heaven Orb](https://www.youtube.com/watch?v=mOArUTf4rCw)\n [B Site One Way Orb](https://www.youtube.com/watch?v=HDUQMSLICRg)\n [A Site Showers Molly](https://www.youtube.com/watch?v=KFb_4NVeidM)\n [A Site Back Truck Molly](https://www.youtube.com/watch?v=5o9CEaxe8YU)\n [A Site Default Molly](https://www.youtube.com/watch?v=p15ipkCKTQ0)\n [B Site Garden Molly](https://www.youtube.com/watch?v=YQogtRNwb0w)\n [B Site Tube Molly](https://www.youtube.com/watch?v=G0BYL3EktqE)\n [B Site Default Molly](https://www.youtube.com/watch?v=xtUYdBLTW10)")
    embed.add_field(name ="Brimstone", value = "[A Site Showers Molly](https://www.youtube.com/watch?v=bfbqaxM3Odk)\n [A Site Back Truck Molly](https://www.youtube.com/watch?v=NV2CaGKY1yY)\n [A Site Default Molly](https://www.youtube.com/watch?v=lv8BHHvOge8)\n [B Site Default Molly](https://www.youtube.com/watch?v=y16dRHK6G3M)")
    embed.add_field(name ="KAY/O", value = "[A Site Showers Molly](https://www.youtube.com/watch?v=Kh7zOUl9qi0)\n [A Site Back Truck Molly](https://www.youtube.com/watch?v=uLNd3MN1RxU)\n [A Site Default Molly](https://www.youtube.com/watch?v=k4xZqTtRbTc)\n [B Site Hookah Molly](https://www.youtube.com/watch?v=EoaJS44hNSA)\n [B Site Garden Molly](https://www.youtube.com/watch?v=_f50kZg8IrE)\n [B Site Tube Molly](https://www.youtube.com/watch?v=w7e7wYVluVQ)\n [B Site Default Molly](https://www.youtube.com/watch?v=i7umyAxrk8M)\n [A Site Showers Knife](https://www.youtube.com/watch?v=q1aGiD4tNz8)\n [A Site U-Hall Knife](https://www.youtube.com/watch?v=M--4IatobjA)\n [B Site Hookah Knife](https://www.youtube.com/watch?v=dgPgHpCQ4CU)\n [B Site Garden Knife](https://www.youtube.com/watch?v=cxRqpeJJ9yM)")
    await ctx.send(embed = embed)
bot.run(TOKEN)


