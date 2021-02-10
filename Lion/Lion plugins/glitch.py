"""
designed By @Krishna_Singhal in userge
ported to telethon by @LiMiTLeSS786 and @simpleboy786
"""

import os

from glitch_this import ImageGlitcher
from PIL import Image
from telethon import functions, types

from .. import LOGS
from . import runcmd, take_screen_shot


@bot.on(admin_cmd(outgoing=True, pattern="(glitch|glitchs)(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="(glitch|glitchs)(?: |$)(.*)", allow_sudo=True))
async def glitch(lion):
    if lion.fwd_from:
        return
    cmd = lion.pattern_match.group(1)
    lioninput = lion.pattern_match.group(2)
    reply = await lion.get_reply_message()
    lionid = lion.reply_to_msg_id
    lion = await edit_or_reply(lion, "```Glitching... 😁```")
    if not (reply and (reply.media)):
        await lion.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lionsticker = await reply.download_media(file="./temp/")
    if not lionsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg")):
        os.remove(lionsticker)
        await lion.edit("`Media not found...`")
        return
    os.path.join("./temp/", "glitch.png")
    if lioninput:
        if not lioninput.isdigit():
            await lion.edit("`You input is invalid, check help`")
            return
        lioninput = int(lioninput)
        if not 0 < lioninput < 9:
            await lion.edit("`Invalid Range...`")
            return
    else:
        lioninput = 2
    if lionsticker.endswith(".tgs"):
        lionfile = os.path.join("./temp/", "glitch.png")
        lioncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {lionsticker} {lionfile}"
        )
        stdout, stderr = (await runcmd(lioncmd))[:2]
        if not os.path.lexists(lionfile):
            await lion.edit("`lionsticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = lionfile
    elif lionsticker.endswith(".webp"):
        lionfile = os.path.join("./temp/", "glitch.png")
        os.rename(lionsticker, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("`lionsticker not found... `")
            return
        glitch_file = lionfile
    elif lionsticker.endswith(".mp4"):
        lionfile = os.path.join("./temp/", "glitch.png")
        await take_screen_shot(lionsticker, 0, lionfile)
        if not os.path.lexists(lionfile):
            await lion.edit("```lionsticker not found...```")
            return
        glitch_file = lionfile
    else:
        glitch_file = lionsticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "./temp/" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, lioninput, color_offset=True)
        glitch_img.save(glitched)
        await lion.client.send_file(lion.chat_id, glitched, reply_to=liinid)
        os.remove(glitched)
        await lion.delete()
    elif cmd == "glitch":
        Glitched = "./temp/" + "glitch.gif"
        glitch_img = glitcher.glitch_image(img, lioninput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        mdnoor = await lion.client.send_file(lion.chat_id, Glitched, reply_to=lionid)
        await lion.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=mdnoor.media.document.id,
                    access_hash=mdnoor.media.document.access_hash,
                    file_reference=mdnoor.media.document.file_reference,
                ),
                unsave=True,
            )
        )
        os.remove(Glitched)
        await lion.delete()
    for files in (lionsticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "glitch": "**Plugin : **`glitch`\
    \n\n**Syntax : **`.glitch` reply to media file\
    \n**Usage :** glitches the given mediafile (gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**Syntax : **`.glitchs` reply to media file\
    \n**Usage :** glitches the given mediafile (gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
    }
)
