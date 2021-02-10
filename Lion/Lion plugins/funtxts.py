import nekos


@bot.on(admin_cmd(pattern="tlion$"))
@bot.on(sudo_cmd(pattern="tlion$", allow_sudo=True))
async def hmm(lion):
    if lion.fwd_from:
        return
    reactlion = nekos.textlion()
    await edit_or_reply(lion, reactlion)


@bot.on(admin_cmd(pattern="why$"))
@bot.on(sudo_cmd(pattern="why$", allow_sudo=True))
async def hmm(lion):
    if lion.fwd_from:
        return
    whylion = nekos.why()
    await edit_or_reply(lion, whylion)


@bot.on(admin_cmd(pattern="fact$"))
@bot.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(lion):
    if lion.fwd_from:
        return
    factlion = nekos.fact()
    await edit_or_reply(lion, factlion)


CMD_HELP.update(
    {
        "funtxts": """**Plugin : **`funtxts`

  •  **Syntax : **`.tlion`
  •  **Function : **__Sens you some random lion facial text art__

  •  **Syntax : **`.why`
  •  **Function : **__Asks some random Funny questions__

  •  **Syntax : **`.fact`
  •  **Function : **__Sends you some random facts__"""
    }
)
