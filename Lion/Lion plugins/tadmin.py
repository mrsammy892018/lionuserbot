"""
idea from lynda and rose bot
made by @simpleboy786
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from ..utils import errors_handler
from . import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

# =================== CONSTANT ===================
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = "`I don't have sufficient permissions! This is so sed. Alexa play despacito`"


@bot.on(admin_cmd(pattern=r"tmute(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"tmute(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def tmuter(lion):
    chat = await lion.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(lion, NO_ADMIN)
        return
    lionevent = await edit_or_reply(lion, "`muting....`")
    user, reason = await get_user_from_event(lion)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        liontime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await lionevent.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await lion.client.get_me()
    ctime = await extract_time(lion, liontime)
    if not ctime:
        await lionevent.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {liontime}"
        )
        return
    if user.id == self_user.id:
        await lionevent.edit(f"Sorry, I can't mute myself")
        return
    try:
        await lionevent.client(
            EditBannedRequest(
                lion.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await lionevent.edit(
                f"{user.first_name} was muted in {lion.chat.title}\n"
                f"**Muted for : **{liontime}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await lion.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{lion.chat.title}(`{lion.chat_id}`)\n"
                    f"**Muted for : **`{liontime}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await lionevent.edit(
                f"{user.first_name} was muted in {lion.chat.title}\n"
                f"Muted for {liontime}\n"
            )
            if BOTLOG:
                await lion.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{lion.chat.title}(`{lion.chat_id}`)\n"
                    f"**Muted for : **`{liontime}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await lionevent.edit("`Uh oh my mute logic broke!`")


@bot.on(admin_cmd(pattern="tban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="tban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def ban(lion):
    chat = await lion.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(lion, NO_ADMIN)
        return
    lionevent = await edit_or_reply(lion, "`banning....`")
    user, reason = await get_user_from_event(lion)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        liontime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await lionevent.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await lion.client.get_me()
    ctime = await extract_time(lion, liontime)
    if not ctime:
        await lionevent.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {liontime}"
        )
        return
    if user.id == self_user.id:
        await lionevent.edit(f"Sorry, I can't ban myself")
        return
    await lionevent.edit("`Whacking the pest!`")
    try:
        await lion.client(
            EditBannedRequest(
                lion.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except BadRequestError:
        await lionevent.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await lion.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await lionevent.edit(
            "`I dont have message nuking rights! But still he was banned!`"
        )
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await lionevent.edit(
            f"{user.first_name} was banned in {lion.chat.title}\n"
            f"banned for {liontime}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await lion.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{lion.chat.title}(`{lion.chat_id}`)\n"
                f"**Banned untill : **`{liontime}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await lionevent.edit(
            f"{user.first_name} was banned in {lion.chat.title}\n"
            f"banned for {liontime}\n"
        )
        if BOTLOG:
            await lion.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{lion.chat.title}(`{lion.chat_id}`)\n"
                f"**Banned untill : **`{liontime}`",
            )


CMD_HELP.update(
    {
        "tadmin": "**Plugin :** `tadmin`\
      \n\n  •  **Syntax : **`.tmute <reply/username/userid> <time> <reason>`\
      \n  •  **Function : **__Temporary mutes the user for given time.__\
      \n\n  •  **Syntax : **`.tban <reply/username/userid> <time> <reason>`\
      \n  •  **Function : **__Temporary bans the user for given time.__\
      \n\n  •  **Time units : ** __(2m = 2 minutes) ,(3h = 3hours)  ,(4d = 4 days) ,(5w = 5 weeks)\
      These times are example u can use anything with those units __"
    }
)
