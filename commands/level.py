import discord
from utils import *

async def run(client, message, args):
    mentioned_user = get_mentioned_user(message.guild, args)
    embed = discord.Embed(color=EMBED_COLOR)
    if mentioned_user:
        level = get_level_member(mentioned_user.id, message.guild.id)
        xp = get_xp_member(mentioned_user.id, message.guild.id)
        max_xp = get_max_xp_member(mentioned_user.id, message.guild.id)
        embed.set_author(name=mentioned_user.name+'#'+mentioned_user.discriminator, icon_url=mentioned_user.avatar_url)
    else:
        level = get_level_member(message.author.id, message.guild.id)
        xp = get_xp_member(message.author.id, message.guild.id)
        max_xp = get_max_xp_member(message.author.id, message.guild.id)
        embed.set_author(name=message.author.name+'#'+message.author.discriminator, icon_url=message.author.avatar_url)
    embed.add_field(name='Level', value=level, inline=True)
    embed.add_field(name='XP', value=f'{xp}/{max_xp}', inline=True)
    embed.set_footer(text=EMBED_FOOTER)
    await message.channel.send(embed=embed)