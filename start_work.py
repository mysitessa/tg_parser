import os
from telethon import TelegramClient, events

api_id = 24376250
api_hash = '2a470c2c5891f05f67ab97c9437ca6a7'

SOURCE_CHAT = -1001487687256
TARGET_CHAT = -1003641327064

client = TelegramClient("session.session", api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_all_messages(event):
    await client.send_message(
        TARGET_CHAT,
        event.message.text or "",
        file=event.message.media
    )

async def main():
    print("Пересылка запущена...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())