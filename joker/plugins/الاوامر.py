# WRITE  BY joker
# PLUGIN FOR joker 
# @jepthon

from telethon import events
import random, re
from ..Config import Config

from joker.utils import admin_cmd

import asyncio
from joker import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

Command = Config.COMM_ET or "الاوامر"

rehu = [
    "🔕🌚🖤⑅⃝ρ⎽ɹ̈⎽බ⎽ɹ̇ ใ⎽ɹ̇ᒧ𓅓⎽Ь⎽ɹ̣",
    "لـسـه مـيـعـرفـووش اإنـهـم مـيـشـرفـووش.!! 😋👅😏🤘",
    "خليك فاكر يا بطل..  اللعب معانا احنا خطر 🪓🔪🗡",
    "آلي نيتووآ سآلكة ملهووش مآلكة 🔥👆🖤",
    "#صاحب_البار مبيسكرش عشان يتفرج 🔞✌ع المساطيل 🚭😏",
    "نسيونااا ف الديقهه نسينااهم ف نص دقيقه‌⚠️⁩🔥",
    "علي شبـاك المصـالح الصحـاب طوابيـر 🔞🤙🏻🍇⚔️",
    "*ال يقــوولــگ انــت فــيگ وفــيگ قــولــوو لــنــفــســي مــش لــيگــ*🧏🏻😉🔥بو",
    "*يا صاحبي لو الرجولة بفلوس ممكن نلم من بعض ونشترهالك !* 🕴🔥😂",
    "‏لو جاي في رجووووع ‏ماشي يلا بينا انت واحشني كدا كدا",
    "مـتـكـبـرهـاش بـسـنـك عـشـان هـقـل مـنـك😂🔥⚔️َ",
    "*_كلهم كارهينن بعض بس المصلحه لماهم🍻🔥_*",
    "غيرگ حاول بس اتزاااول ⚔️👻🖤ٌ",
    "لــو اهــلــك رمــوكى تــعــالــى فــى حــضــن اخــوكى 😂♥️🍇",
    "﮼انـا ﮼عـمهـا ﮼حـتـي ﮼وانـا ﮼مـش ﮼فـايـقـلها 😉⚓🏴‍☠️",
    "* آڪـتـفـي بـنفسڪ... وآݪـباقي وجـودهـم جـميݪ، وغــيآبـهم أجـمل 🖤🔥*",
    "حـريـمـگـو نـفـسـهـٱا بـس أنا گــاارف لـهـٱا😉🤏🏻🖤💥.",
    "﮼انـا ﮼عـمهـا ﮼حـتـي ﮼وانـا ﮼مـش ﮼فـايـقـلها 😉⚓🏴‍☠️",
]
@l313l.on(admin_cmd(pattern=f"{Command}(?:\s|$)([\s\S]*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lMl10l = random.choice(rehu)
        await event.edit(
        f": **⦑ قائمة اوامر كرستين ⦒**\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n( `.م1` )  ⦙ **اوامر الادمن**\n( `.م2` )  ⦙ **اوامر المجموعة**\n( `.م3` )  ⦙ **اوامر الترحيب والردود**\n( `.م4` )  ⦙ **حماية خاص والتلكراف**\n( `.م5` )  ⦙ **اوامر المنشن والانتحال**\n( `.م6` )  ⦙ **اوامر التحميل والترجمة**\n( `.م7` )  ⦙ **اوامر المنع و القفل**\n( `.م8` )  ⦙ **اوامر التنظيف والتكرار**\n( `.م9` )  ⦙ **اوامر التخصيص والفارات**\n( `.م10` ) ⦙ **اوامر الوقتي و التشغيل**\n( `.م11` ) ⦙ **اوامر الكشف و الروابط**\n( `.م12` ) ⦙ **اوامر المساعدة والإذاعة** \n( `.م13` ) ⦙ **اوامر الارسال والاذكار**\n( `.م14` ) ⦙ **اوامر المـلصقات وكوكل**\n( `.م15` ) ⦙ **اوامر التسلية والميمز والتحشيش** \n( `.م16` ) ⦙ **اوامر الصيغ والجهات**\n( `.م17` ) ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n( `.م18` ) ⦙ **اوامر الحساب والترفيه**\n( `.م19` ) ⦙ **اوامر الميوزك والتشغيل**\n( `.م20` ) ⦙ **اوامر بصمات الميمز**\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n **᯽︙ {lMl10l} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الادمن لسورس كرستين **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس كرستين **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_PP"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n★♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡★\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الارسال **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ اختر احدى هذه الاوامر\n ᯽︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    lMl10l = random.choice(rehu)
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n ♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n- ( `.بصمات انمي` ) \n♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡\n᯽︙ {lMl10l}\n⌔︙CH : @S_EG_P"

)
