import discord
from discord.ext.commands import Bot
from discord import Intents

bot = Bot(command_prefix='!') # or whatever prefix you choose(!,%,?)
TOKEN = 'ODU4MDMxMjI3Mjk3NzI2NTA0.YNYN2g.Y7NiBR--GboIfHKX1IiW-ZWJCLY'

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
    if message.content == 'test':
	    await message.channel.send('Testing 1 2 3!')
    
    await bot.process_commands(message)

@bot.command(name='server')
async def beginBattle(context):
    await context.send(f"end")
    await bot.process_commands(context)


bot.run(TOKEN)