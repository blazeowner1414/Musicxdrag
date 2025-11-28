from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

# from .logging import LOGGER


class Anony(Client):
    def __init__(self):
        print("Starting Bot...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # a = await self.get_chat_member(config.LOGGER_ID, self.id)
# if a.status != ChatMemberStatus.ADMINISTRATOR:
#     exit()
        
        print(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
