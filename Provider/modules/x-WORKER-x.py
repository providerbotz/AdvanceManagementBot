from pyrogram import filters
from Provider.provider import AdvanceManagementBot
from Provider.modules.auto_filters import auto_filters, send_for_index
from Provider.modules.manual_filters import manual_filters
from Provider.functions.settings import get_settings
from Provider.database import db


@AdvanceManagementBot.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client, message):

    k = await manual_filters(client, message)
    if k == False:
        settings = await get_settings(message.chat.id)
        if settings["autofilter"]:
            await auto_filters(client, message)

@AdvanceManagementBot.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming)
async def start_for_index(client, message):
    await send_for_index(client, message)
