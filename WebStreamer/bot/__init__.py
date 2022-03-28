# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]


from ..vars import Var
from pyrogram import Client
from os import getcwd

StreamBot = Client(
    session_name="WebStreamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    no_updates=True
)

multi_clients = {}
work_loads = {}
