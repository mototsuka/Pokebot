import asyncio
import discord
import random

from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!poke ')
Token = 'Insert Token Here'



class Pokebot(commands.Cog) :
    
    def __init__(self,bot):
        self.bot=bot
        self.counter = 0
        self.range = 151
        self.trainers = {}
    
    # Bot Commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong!')

    @commands.command()
    async def yeet(self,ctx):
        await ctx.send('yote!')
    
    @commands.command()
    async def exit(self,ctx):
        await ctx.send('Aight Imma head out.')
        await self.bot.close()

    @commands.command()
    async def start(self,ctx):
        if ctx.author.id not in self.trainers:
            await ctx.send('Welcome to World of Pokemon! Please Enter your name in the format: "Hello, my name is ________')
            self.trainers[ctx.author.id] = "New Trainer"
        else:
            await ctx.send("You are already a Trainer!")

    @commands.command()
    async def count(self,ctx):
        await ctx.send(self.counter)

    @commands.command()
    async def trainer(self,ctx):
        await ctx.send(self.trainers)

    #Bot Listeners

    """@commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id is not self.bot.user.id and message.content.startswith ("Hello, my name is"):
            splitMessage=message.content
            x=splitMessage.split()
            await message.channel.send(x[4])
"""
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id is not self.bot.user.id and not message.content.startswith("!poke "):
            self.counter+=1
        if self.counter == 5:
            self.counter = 0
            randNum = random.randint(1,self.range)
            await message.channel.send("A wild Pokemon #" + str(randNum) +" appeared!")

if __name__ == '__main__' :
    bot.add_cog(Pokebot(bot))
    bot.run(Token)
