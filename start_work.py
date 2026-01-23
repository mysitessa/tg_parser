import os
from telethon import TelegramClient, events

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

SOURCE_CHAT = os.getenv('SOURCE_CHAT')
TARGET_CHAT = os.getenv('TARGET_CHAT')

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