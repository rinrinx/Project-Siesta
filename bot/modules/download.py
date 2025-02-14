import asyncio

from bot import CMD
from pyrogram.types import Message
from pyrogram import Client, filters

from ..helpers.translations import lang
from ..helpers.utils import check_user, antiSpam
from ..helpers.message import send_message


@Client.on_message(filters.command(CMD.DOWNLOAD))
async def download_track(client, msg:Message):
    if await check_user(msg=msg):
        try:
            if msg.reply_to_message:
                link = msg.reply_to_message.text
                reply = True
            else:
                link = msg.text.split(" ", maxsplit=1)[1]
                reply = False
        except:
            await send_message(msg, lang.ERR_NO_LINK)

        spam = await antiSpam(msg.from_user.id, msg.chat.id)
        if not spam:
            # dummy task
            await send_message(msg, 'Downlaoding.......')
            await asyncio.sleep(30)
            await antiSpam(msg.from_user.id, msg.chat.id, True)