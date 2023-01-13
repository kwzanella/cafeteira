import discord
from discord.ext import commands
from help_command import help_embeds as he
import utils


logger = utils.set_logger(__name__, file_name="help_commands.log") 


class CustomHelpCommand(commands.HelpCommand):
    
    def __init__(self, **options):
        self.channel = None
        super().__init__(**options)

    # called when user send "!help"
    async def send_bot_help(self, mapping):
        self.channel = self.get_destination()
        logger.info("Usuário requisitou '!help'")
        await self.channel.send(embed=he.help_embed(mapping))

    # called when "!help <command_name>"
    async def send_command_help(self, command):
        self.channel = self.get_destination()
        logger.info(f"Usuário requisitou '!help' para comando '{command.name}'")

        if command.name == "lembrete":
            await self.channel.send(embed=he.reminder_help(command))
        else:
            await self.channel.send(embed=he.command_embed(command))

    # called by "send_error_message"
    def command_not_found(self, string):
        return f"""Nenhum comando de nome "{string}" foi encontrado."""

    
    def subcommand_not_found(self, command, string):    # Called by "send_error_message"
        if isinstance(command, discord.Group) and len(command.all_commands) > 0:
            return f"""Comando "{command.qualified_name}" não tem nenhum subcomando chamado {string}"""

        return f"""Comando "{command.qualified_name}" não tem subcomandos."""
        
    # called when "!help <command_name>" is not found
    async def send_error_message(self, error):
        self.channel = self.get_destination()
        logger.warning(error)
        await self.channel.send(embed=utils.simple_embed(error, discord.Colour.red()))
        

    """async def send_cog_help(self, cog):
        self.channel = self.get_destination()

        await self.channel.send(f"{cog.qualified_name}: {[command.name for command in cog.get_commands()]}")


    async def send_group_help(self, group):
        self.channel = self.get_destination()

        await self.channel.send(f"{group.name}: {[command.name for index, command in enumerate(group.commands)]}")"""
