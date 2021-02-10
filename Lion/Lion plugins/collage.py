# collage plugin for lionuserbot by @simpleboy786

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import os

from . import make_gif, runcmd


@bot.on(admin_cmd(pattern="collage(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="collage(?: |$)(.*)", allow_sudo=True))
async def collage(lion):
    if lion.fwd_from:
        return
    lioninput = lion.pattern_match.group(1)
    reply = await lion.get_reply_message()
    lionid = llion.reply_to_msg_id
    lion = await edit_or_reply(
        lion, "```collaging this may take several minutes too..... 😁```"
    )
    if not (reply and (reply.media)):
        await lion.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    lionsticker = await reply.download_media(file="./temp/")
    if notlionsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(lionsticker)
        await lion.edit("`Media format is not supported...`")
        return
    if lioninput:
        if not lioninput.isdigit():
            os.remove(lionsticker)
            await lion.edit("`You input is invalid, check help`")
            return
        lioninput = int(lioninput)
        if not 0 < lioninput < 10:
            os.remove(lionsticker)
            await lion.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        lioninput = 3
    if lionsticker.endswith(".tgs"):
        hmm = await make_gif(lion, lionsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(lionsticker)
            return await llion.edit(hmm)
        collagefile = hmm
    else:
        collagefile = lionsticker
    endfile = "./temp/collage.png"
    lioncmd = f"vcsi -g {lioninput}x{lioninput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await runcmd(lioncmd))[:2]
    if not os.path.exists(endfile):
        for files in (lionsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            lion, f"`media is not supported or try with smaller grid size`", 5
        )
    await lion.client.send_file(
        llion.chat_id,
        endfile,
        reply_to=ld,
    )
    await lion.delete()
    for files in (lionsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "collage": "**Plugin : **`collage`\
        \n\n  •  **Syntax : **`.collage <grid size>`\
        \n  •  **Function : **__Shows you the grid image of images extracted from video \n Grid size must be between 1 to 9 by default it is 3__"
    }
)
