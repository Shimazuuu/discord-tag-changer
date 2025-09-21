import time
import requests

AUTH_TOKEN = "TOKEN-HERE"

CLAN_ENDPOINT = "https://discord.com/api/v9/users/@me/clan"

HEADERS = {
    "accept": "*/*",
    "accept-language": "fr,fr-FR;q=0.9",
    "authorization": AUTH_TOKEN,
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    ),
}

GUILDS = {
    "GUILD ID 1": "Guild Name 1",
    "GUILD ID 2": "Guild Name 2"
}

DELAY = 300 


while True:
    for guild_id, guild_label in GUILDS.items():
        payload = {
            "identity_guild_id": guild_id,
            "identity_enabled": True
        }

        response = requests.put(CLAN_ENDPOINT, json=payload, headers=HEADERS)

        if response.status_code == 200:
            print(f"[OK] Changement effectué -> {guild_id} ({guild_label})")
        else:
            print(f"[ERREUR {response.status_code}] {guild_id} ({guild_label}) : {response.text}")

        time.sleep(DELAY)
