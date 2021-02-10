# credits to @LiMiTLeSS786

#  Copyright (C) 2020  @LiMiTLeSS786
import asyncio
import base64
import os
import re

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)


@bot.on(admin_cmd(outgoing=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    reply_to_id = await reply_id(lion)
    if not text:
        if lion.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await edit_delete(lion, "`What should i search in google.`", 5)
            return
    lion = await edit_or_reply(lion, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            lion,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    lionfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@bot.on(admin_cmd(outgoing=True, pattern="trump(?: |$)(.*)", command="trump"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="trump(?: |$)(.*)", command="trump"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(lion, "**Trump : **`What should I tweet`", 5)
            return
    lion = await edit_or_reply(lion, "`Requesting trump to tweet...`")
    try:
        hmm = Get(hmm)
        await lion.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await trumptweet(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@bot.on(admin_cmd(outgoing=True, pattern="modi(?: |$)(.*)", command="modi"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="modi(?: |$)(.*)", command="modi"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(lion, "**Modi : **`What should I tweet`", 5)
            return
    lion = await edit_or_reply(lion, "Requesting modi to tweet...")
    try:
        hmm = Get(hmm)
        await lion.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await moditweet(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@bot.on(admin_cmd(outgoing=True, pattern="cmm(?: |$)(.*)", command="cmm"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="cmm(?: |$)(.*)", command="cmm"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(lion, "`Give text to write on banner, man`", 5)
            return
    lion = await edit_or_reply(lion, "`Your banner is under creation wait a sec...`")
    try:
        hmm = Get(hmm)
        await lion.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await changemymind(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@bot.on(admin_cmd(outgoing=True, pattern="kanna(?: |$)(.*)", command="kanna"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="kanna(?: |$)(.*)", command="kanna"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(lion, "**Kanna : **`What should i show you`", 5)
            return
    lion = await edit_or_reply(lion, "`Kanna is writing your text...`")
    try:
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await kannagen(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@bot.on(admin_cmd(outgoing=True, pattern="tweet(?: |$)(.*)", command="tweet"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="tweet(?: |$)(.*)", command="tweet"))
async def nekobot(lion):
    if lion.fwd_from:
        return
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(
                lion,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
            return
    try:
        hmm = Get(hmm)
        await lion.client(hmm)
    except BaseException:
        pass
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            lion,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    lion = await edit_or_reply(lion, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await tweets(text, username)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lion.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


CMD_HELP.update(
    {
        "imgmemes": """**Plugin : **`imgmemes`

  •  **Syntax : **`.fakegs search query ; what you mean text`
  •  **Function : **__Shows you image meme for your google search query__  

  •  **Syntax : **`.trump reply/text`
  •  **Function : **__sends you the trump tweet sticker with given custom text__

  •  **Syntax : **`.modi reply/text`
  •  **Function : **__sends you the modi tweet sticker with given custom text__ 

  •  **Syntax : **`.cmm reply/text`
  •  **Function : **__sends you the  Change my mind banner with given custom text__ 

  •  **Syntax : **`.kanna reply/text`
  •  **Function : **__sends you the kanna chan sticker with given custom text__  

  •  **Syntax : **`.tweet reply/<username> ; <text>`
  •  **Function : **__sends you the desired person tweet sticker with given custom text__ 
  """
    }
)
