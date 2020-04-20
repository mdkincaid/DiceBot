import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = '''Dungeons & Dragons dice rolling bot.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # chagnes bot 'Playing' status
    await bot.change_presence(activity=discord.Game(name='!help for more info'))
    print('Successfully booted and logged in...!')

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Usage: `!roll #d#` e.g. `!roll 1d10`\nUser !help for more info.')

@bot.command(pass_context=True)
async def roll(ctx, roll : str):
    """Rolls a dice using the #d# format.
    e.g. !roll 2d10"""

    resultTotal = 0
    resultString = ''

    try:
        try:
            numDice = roll.split('d')[0]
            diceVal = roll.split('d')[1]
        except Exception as e:
            print(e)
            await ctx.send(f'Format has to be in #d# {ctx.author}')
            return

        if int(numDice) > 500:
            await ctx.send(f'I can\'t roll that many dice {ctx.author}')
            return
        
        await ctx.send(f'Rolling {numDice}d{diceVal} for {ctx.author}')
        rolls, limit = map(int, roll.split('d'))

        for r in range(rolls):
            number = random.randint(1, limit)
            resultTotal = resultTotal + number

            if resultString == '':
                resultString += str(number)
            else:
                resultString += ', ' + str(number)

        if numDice == '1':
            await ctx.send(f'{ctx.author.mention} :game_die:\n**Result:** {resultString}')
        else:
            await ctx.send(f'{ctx.author.mention} :game_die:\n**Result:** {resultString} \n**Total:** {str(resultTotal)}')

    except Exception as e:
        print(e)
        return

bot.run(TOKEN)