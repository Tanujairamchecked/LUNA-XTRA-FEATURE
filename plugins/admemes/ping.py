"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ππΎπ π°ππ΄ π½πΎπ π³π΄π°π³. ππΎππ π°ππ΄ πππΈπ»π» π·π΄ππ΄. ππΎπ π·π°ππ΄ π½πΎ π»πΎππ΄ π΅πΎπ πΌπ΄ π½πΎπ πΎπΊπ°π .. ππΎπ'ππ π½πΎπ π²π·π°π½πΆπ΄π³ π»πΈπΊπ΄ ππΎπ πππ΄π³ ππΎ π±π΄ .. πΉπππ πππ°ππ /start πΎπ½π΄ π°π π° ππΈπΌπ΄.."
REPO = "<b>ππ·πΈπ πΈπ π½πΎπ πΎπΏπ΄π½ ππΎπππ²π΄ πΏππΎπΉπ΄π²π </b>"
CHANNEL = "<b>ππΎππππ±π΄ π²π·π°π½π½π΄π»</b> βΊβΊ https://youtube.com/channel/UCl1EnIFvBwT7dPtgfOYnvPA\n\n<b>π²π·π°π½π½π΄π»</b> βΊβΊ https://t.me/Inline_db\n\n<b>π»ππ½π°-π»π΄π΄π²π·-ππΎπ½π΄</b> βΊβΊ https://t.me/lunamirror\n\n<b>πΌπΎππΈπ΄-πΆππΎππΏ</b> βΊβΊ https://t.me/Movie_factory01"
LUNA = "<b>π±πΎπ βΊβΊ https://t.me/rb_luna_bot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("luna", COMMAND_HAND_LER) & f_onw_fliter)
async def LUNA(_, message):
    await message.reply_text(LUNA)




