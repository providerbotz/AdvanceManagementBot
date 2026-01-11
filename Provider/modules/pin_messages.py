from Provider.provider import AdvanceManagementBot
from Provider.functions.handlers import Pin

@AdvanceManagementBot.on_message(Pin.a)
async def pin(_, message):
    if not message.reply_to_message:
        return
    args = message.text.lower().split()
    notify = not any(arg in args for arg in ('loud', 'notify'))
    await message.reply_to_message.pin(disable_notification=notify)

@AdvanceManagementBot.on_message(Pin.b)
async def unpin(_, message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
