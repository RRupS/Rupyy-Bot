VERSION = 0.1
DEVELOPER = 'rups'
DEVELOPER_ID = 299232190078648323
MODERATOR_ID_LIST = [
    299232190078648323,  # rups
]
EMBED_COLOR = 0xC4AE78
EMBED_FOOTER = 'ruppy.herokuapp.com - dev. by rups'

# --- Imports --- #
import json
import requests
import os
from dotenv import load_dotenv
# --------------- #

load_dotenv()

def get_user(guild, arg):
    if '<@!' in arg:
        return guild.get_member(int(arg[3:-1]))
    elif arg.isdigit():
        return guild.get_member(int(arg))
    return None

def get_mentioned_user(guild, args):
    if args != []:
        mentioned_user = get_user(guild, args[0])
        if mentioned_user != None:
            return mentioned_user
        return False
    return False


def add_xp_member(member_id, guild_id, xp):
    requests.patch(
        url = 'https://rupyy.tk/api/add-xp-member',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        json = {
            'member_id': member_id,
            'guild_id': guild_id,
            'xp': xp
        }
    )

def add_xp_guild(guild_id, xp):
    requests.patch(
        url = 'https://rupyy.tk/api/add-xp-guild',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        json = {
            'guild_id': guild_id,
            'xp': xp
        }
    )

def reset_xp_guilds(time_interval):
    requests.patch(
        url = 'https://rupyy.tk/api/reset-xp-guilds',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        json = {
            'time_interval': time_interval
        }
    )

def get_xp_member(member_id, guild_id):
    user = requests.get(
        url = 'https://rupyy.tk/api/get-member',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        params = {
            'member_id': member_id,
            'guild_id': guild_id
        }
    ).json()
    return user['xp']

def get_xp_guild(guild_id):
    guild = requests.get(
        url = 'https://rupyy.tk/api/get-guild',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        params = {
            'guild_id': guild_id
        }
    ).json()
    return guild

def get_max_xp_member(member_id, guild_id):
    user = requests.get(
        url = 'https://rupyy.tk/api/get-member',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        params = {
            'member_id': member_id,
            'guild_id': guild_id
        }
    ).json()
    return user['max-xp']

def get_level_member(member_id, guild_id):
    user = requests.get(
        url = 'https://rupyy.tk/api/get-member',
        headers = {
            'Authorization': 'Bot {}'.format(os.getenv('TOKEN'))
        },
        params = {
            'member_id': member_id,
            'guild_id': guild_id
        }
    ).json()
    return user['level']