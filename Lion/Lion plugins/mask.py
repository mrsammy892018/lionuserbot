# credits to @LiMiTLeSS786

#    Copyright (C) 2020  @LiMiTLeSS786

import base64
import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import awooify, baguette, iphonex, lolice


@bot.on(admin_cmd("mask$", outgoing=True))
@bot.on(sudo_cmd(pattern="mask$", allow_sudo=True))
async def _(lionbot):
    reply_message = await lionbot.get_reply_message()
    if not reply_message.media or not reply_message:
        await edit_or_reply(lionbot, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        await edit_or_reply(lionbot, "```Reply to actual users message.```")
        return
    event = await lionbot.edit("```Processing```")
    async with lionbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await lionbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock @hazmat_suit_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await lionbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@bot.on(admin_cmd(pattern="awooify$"))
@bot.on(sudo_cmd(pattern="awooify$", allow_sudo=True))
async def lionbot(lionmemes):
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    try:
        lion = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        lion = Get(lion)
        await lionmemes.client(lion)
    except BaseException:
        pass
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await lionevent.edit("generating image..")
    else:
        await lionevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await lionevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    lion = f"https://telegra.ph{response[0]}"
    lion = await awooify(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@bot.on(admin_cmd(pattern="lolice$"))
@bot.on(sudo_cmd(pattern="lolice$", allow_sudo=True))
async def lionbot(lionmemes):
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    try:
        lion = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        lion = Get(lion)
        await lionmemes.client(lion)
    except BaseException:
        pass
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await lionevent.edit("generating image..")
    else:
        await lionevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await lionevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    lion = f"https://telegra.ph{response[0]}"
    lion = await lolice(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@bot.on(admin_cmd(pattern="bun$"))
@bot.on(sudo_cmd(pattern="bun$", allow_sudo=True))
async def lionbot(lionmemes):
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    try:
        lion = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        lion = Get(lion)
        await lionmemes.client(lion)
    except BaseException:
        pass
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await lionevent.edit("generating image..")
    else:
        await lionevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await lionevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    lion = f"https://telegra.ph{response[0]}"
    lion = await baguette(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


@bot.on(admin_cmd(pattern="iphx$"))
@bot.on(sudo_cmd(pattern="iphx$", allow_sudo=True))
async def lionbot(lionmemes):
    replied = await lionmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    if replied.media:
        lionevent = await edit_or_reply(lionmemes, "passing to telegraph...")
    else:
        await edit_or_reply(lionmemes, "reply to a supported media file")
        return
    try:
        lion = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        lion = Get(lion)
        await lionmemes.client(lion)
    except BaseException:
        pass
    download_location = await lionmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await lionevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await lionevent.edit("generating image..")
    else:
        await lionevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await lionevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    lion = f"https://telegra.ph{response[0]}"
    lion = await iphonex(lion)
    await lionevent.delete()
    await lionmemes.client.send_file(lionmemes.chat_id, lion, reply_to=replied)


CMD_HELP.update(
    {
        "mask": "`.mask` reply to any image file:\
      \nUSAGE:makes an image a different style try out your own.\
      "
    }
)
