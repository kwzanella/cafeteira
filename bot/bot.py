import discord
from discord.ext import commands, tasks
from bot import embeds
from json_file import JSONFile


# bot is only going to send notifications and verify periodically using Discord tasks
class NotificationBot(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot     = bot
        self.config = JSONFile("config")
        
        self.channel = None
        try:
            self.channel = self.bot.get_channel(self.config.read("bot_config.json")["channel_id"])
        except KeyError:
            print("bot_config.json not created yet or empty.")
        
        self.check_tasks.start()
  
  
    # initializes channel that messages are going to be sent
    @commands.command(name="iniciar", brief="Define canal que serão enviadas as notificações e mensagens do bot.", aliases=["init"])
    async def init(self, ctx):
        self.config.write("bot_config.json", {"channel_id": ctx.channel.id})
        self.channel = ctx.channel
        
        em = discord.Embed (
            type = "rich",
            color = discord.Colour.blue(),
            description = "**Canal foi definido como padrão e o bot o usará para mandar mensagens.**"
        )
        
        await self.channel.send(embed=em)
    
    
    # task to verify other stuff each 30 minutes
    @tasks.loop(seconds=10)
    async def check_tasks(self):
        if self.channel != None:
        
            await self.channel.send("teste")