"""
https://discord.com/developers/docs/interactions/slash-commands#registering-a-command
"""

import os

import requests

# APPLICATION_ID = os.environ.get("APPLICATION_ID")
# GUILD_ID = os.environ.get("GUILD_ID")
# BOT_TOKEN = os.environ.get("BOT_TOKEN")

APPLICATION_ID = "829714503699660882"
GUILD_ID = "829358438265520129"
BOT_TOKEN = "ODI5NzE0NTAzNjk5NjYwODgy.YG8J2Q.rdsvMStjFfLeL_OyoFyQYjFvwR8"

url = f"https://discord.com/api/v8/applications/{APPLICATION_ID}/guilds/{GUILD_ID}/commands"

json = {
    "name": "vh",
    "description": "List, start, stop or get the status of the Valheim server",
    "options": [
        {
            "name": "list",
            "description": "List available servers",
            "type": 3,
        },
        {
            "name": "status",
            "description": "Show server status",
            "type": 3,
        },
        {
            "name": "start",
            "description": "Start a given server name",
            "type": 3,
        },
        {
            "name": "stop",
            "description": "Stop a given server name",
            "type": 3,
        },
    ]
}

headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

if __name__ == "__main__":
    r = requests.post(url, headers=headers, json=json)
    print(r.content)