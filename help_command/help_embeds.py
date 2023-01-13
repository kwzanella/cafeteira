from discord import Embed
from discord import Colour


def reminder_help(command) -> Embed:
    aliases = command.aliases
    desc = f"**- Função:\n** {command.brief}\n"
    
    if aliases:
        desc += "**- Outros nomes:\n**"

    for alias in aliases:
        if alias == aliases[-1]:
            desc += f"`{alias}` \n"
        else:
            desc += f"`{alias}`, "

    instructions = (
        "Digite o comando seguido do `título`, `comentário`, `data` e `horário` __em ordem__ e terminados por __ponto e vírgula__.\n\n" +
        "O formato aceito para data é `dia/mês/ano` e para horário é `horas:minutos`"
    )
    
    example = ( 
        "`!lembrete título; comentário; data; horário;`\n\n" + 
        "`!lembrete título; ; data; horário;`\n\n"
    )

    note = (
        "__O único dado **NÃO** necessário é o comentário. Para ignorá-lo, apenas coloque (;) como no exemplo acima.__\n\n"
    )

    embed = Embed (
    	title = "Comando 'help lembrete'", 
        type = "rich", 
        description = desc,
        color = Colour.gold()
    )

    embed.add_field(name="- Instruções:", value=instructions, inline=False)
    embed.add_field(name="- Exemplos:", value=example, inline=False)
    embed.add_field(name="- Observação:", value=note, inline=False)
    return embed


def command_embed(command) -> Embed:
    aliases = command.aliases
    params = command.clean_params
    params = list(params.keys())

    desc = f"**- Função:\n** {command.brief}\n"
    if aliases:
        desc += "**- Outros nomes:\n**"

    for alias in aliases:
        if alias == aliases[-1]:
            desc += f"`{alias}` \n"
        else:
            desc += f"`{alias}`, "


    embed = Embed (
        title=f"Comando 'help {command.name}'",
        description=desc,
        color=Colour.gold()
    )

    parameters = ""
    for i in params:
        if i == "title":
            i = "titulo"

        elif i == "text":
            i = "texto"
        
        parameters += f"<{i}> "

    embed.add_field(name="- Exemplo:", value=f"`!{command.name} {parameters}`")
    return embed


def help_embed(mapping) -> Embed:
    desc = ""
    for cog in mapping: # mapping = dict
        if cog is not None:
            desc += f"**- {cog.qualified_name}:\n**"
            
            commands = [command.name for command in mapping[cog]]
            for command in commands:
                if command == commands[-1]:  # checks if last is command
                    desc += f"`{command}`\n"
                else:
                    desc += f"`{command}`, "
    

    embed = Embed (
        title="Comando 'help'",
        type="rich",
        description=desc + "Digite __'!help <nome do comando>'__ para informações sobre um comando específico\n",
        color=Colour.gold()
    )

    return embed