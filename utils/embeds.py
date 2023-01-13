from discord import Colour, Embed

# TODO: Import reminder dentro da função e verifica instância
def show_reminder(rem) -> Embed:
        embed = Embed (
            type = "rich", 
            color = Colour.blue()
        )

        comment = rem.comment
        if not rem.comment:     # Necessário pois Discord não aceita "" como válido
            comment = "**----------------**"

        embed.add_field(name="- Título:", value=rem.title, inline=False)
        embed.add_field(name="- Comentário:", value=comment, inline=False)
        embed.add_field(name="- Data:", value=rem.date, inline=False)
        embed.add_field(name="- Horário:", value=rem.time, inline=False)
        
        return embed


def simple_embed(text: str, color: Colour) -> Embed:
    embed = Embed(
        type = "rich", 
        description = f"**{text}**",
        color = color
    )
    return embed