from Provider.provider import AdvanceManagementBot 
from Provider.functions.extract_user import extract_user
from Provider.functions.extract_time import extract_time
from Provider.functions.handlers import Ban

@AdvanceManagementBot.on_message(Ban.a)
async def ban_user(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                ""Someone else is creating trouble..! "
                f"{user_first_name}"
                " has been banned."
            )
        else:
            await message.reply_text(
                "Someone else is creating trouble..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " has been banned."
            )

@AdvanceManagementBot.on_message(Ban.b)
async def un_ban_user(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "okay, changed... now "
                f"{user_first_name} "
                "can join the group!"
            )
        else:
            await message.reply_text(
                "okay, changed... now "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> "
                "can join the group!"
            )

@AdvanceManagementBot.on_message(Ban.c)
async def temp_ban_user(_, message):
    if not len(message.command) > 1:
        return

    user_id, user_first_name, _ = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "invalid time type specified. "
                "expected m, h, or d, got: {}"
            ).format(message.command[1][-1])
        )
        return

    try:
        await message.chat.ban_member(user_id=user_id, until_date=until_date_val)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is creating trouble..! "
                f"{user_first_name}"
                f" banned for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Someone else is creating trouble..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                f" banned for {message.command[1]}!"
            )