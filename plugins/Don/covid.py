import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("π²π»πΎππ΄", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_video(
        video="https://graph.org/file/c220fae7eb1baab2df1f0.mp4",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**π²πΎππΈπ³ π·πΏ πΈπ½π΅πΎππΌπ°ππΈπΎπ½**--
αβΊ π²πΎππ½πππ : `{country}`
αβΊ π°π²ππΈππ΄π³ : `{active}`
αβΊ π²πΎπ½π΅πΈππΌπ΄π³ : `{confirmed}`
αβΊ π³π΄π°ππ·π : `{deaths}`
αβΊ πΈπ³ : `{info_id}`
αβΊ π»π°ππ ππΏπ³π°ππ΄ : `{last_update}`
αβΊ π»π°ππΈπππ³π΄ : `{latitude}`
αβΊ π»πΎπ½πΆπΈπππ³π΄ : `{longitude}`
αβΊ ππ΄π²πΎππ΄ππ΄π³ : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
