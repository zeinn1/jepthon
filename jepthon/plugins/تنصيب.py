from telethon import events, Button
from ..Config import Config
from ..sql_helper.globals import gvarstatus
from JepIQ.razan.resources.mybot import *

ROZ_PIC = "https://telegra.ph//file/835b48f330763bffc34a7.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [[Button.url("1- قناة السورس", "https://t.me/S_EG_P"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://t.me/str_12bot"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://heroku.com/deploy?template=https://github.com/zeinn1/iiqllll"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/devpokemon"),]]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False)
            elif ROZ_PIC:
                result = builder.document(ROZ_PIC,title="joker",text=ROZ,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="joker",text=ROZ,buttons=buttons,link_preview=False)
            await event.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="السورس"))
async def repo(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(TG_BOT, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()

# edit by ~ @lMl10l
