"""
imported from nicegrill
modified by @LiMiTLeSS786
QuotLy: Avaible commands: .qbot
"""
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import convert_tosticker, process


@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def stickerchat(lionquotes):
    if lionquotes.fwd_from:
        return
    reply = await lionquotes.get_reply_message()
    if not reply:
        await edit_or_reply(
            lionquotes, "`I cant quote the message . reply to a message`"
        )
        return
    fetchmsg = reply.message
    repliedreply = None
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await edit_or_reply(lionquotes, "`this format is not supported now`")
        return
    lionevent = await edit_or_reply(lionquotes, "`Making quote...`")
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, lionmsg = await process(fetchmsg, user, lionquotes.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    lionmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await lionquotes.client.send_file(lionquotes.chat_id, endfi, reply_to=reply)
    await lionevent.delete()
    os.remove(endfi)


@bot.on(admin_cmd(pattern="rq(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rq(?: |$)(.*)", allow_sudo=True))
async def stickerchat(lionquotes):
    if lionquotes.fwd_from:
        return
    reply = await lionquotes.get_reply_message()
    if not reply:
        await edit_or_reply(
            lionquotes, "`I cant quote the message . reply to a message`"
        )
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await edit_or_reply(lionquotes, "`this format is not supported now`")
        return
    lionevent = await edit_or_reply(lionquotes, "`Making quote...`")
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, lionmsg = await process(fetchmsg, user, lionquotes.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    lionmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await lionquotes.client.send_file(lionquotes.chat_id, endfi, reply_to=reply)
    await lionevent.delete()
    os.remove(endfi)


@bot.on(admin_cmd(pattern="qbot(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    lionevent = await edit_or_reply(event, "```Making a Quote```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await lionevent.edit("```Please unblock me (@QuotLyBot) u Nigga```")
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Hi!"):
            await lionevent.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await lionevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "quotly": "**Plugin :** `quotly`\
        \n\n**  •Syntax : **`.q reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote__\
        \n\n**  •Syntax : **`.qbot reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote by @quotlybot__\
        "
    }
)
