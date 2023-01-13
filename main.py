from discord.ext import commands
from bot import NotificationBot
from help_command import CustomHelpCommand


bot = commands.Bot(command_prefix='!', help_command=CustomHelpCommand())


@bot.event
async def on_ready():
    bot.add_cog(NotificationBot(bot))
    print(f"Logado como {bot.user}!")


def main():
    bot.run("") # get another key using env variables
    
    
if __name__ == "__main__":
    main()
