# main.py

from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
#from discord import AsyncWebhookAdapter
from discord import Webhook
import aiohttp
from responses import get_response


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
WEBHOOK_URL: Final[str] = os.getenv('DISCORD_WEBHOOK_URL')  # Add this to your .env file
print(TOKEN)

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Discord Webhook Setup
# async def send_webhook_message(message_content: str) -> None:
#     if not WEBHOOK_URL:
#         print("Webhook URL not provided. Skipping webhook message.")
#         return
#
#     async with aiohttp.ClientSession() as session:
#         webhook = Webhook.from_url(WEBHOOK_URL, adapter=AsyncWebhookAdapter(session))
#         await webhook.send(message_content)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        # await send_webhook_message(f"User {message.author} sent: '{user_message}' and received: '{response}'")
    except Exception as e:
        print(e)

# Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
