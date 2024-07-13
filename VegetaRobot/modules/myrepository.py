
import requests 

from VegetaRobot import pgram, aiohttpsession as session
from pyrogram import filters
from pyrogram.types import *




@pgram.on_message(filters.command("repo"))
async def repo(_, m):
    chat_id = m.chat.id
    users = requests.get("https://t.meracists_support").json()
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")
        count += 1
        total = count-1
    text = f"""
[ Nhi Dunga Repo ]

    await pgram.send_message(chat_id,text=text,
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Repo",url="https://t.me/racists_support"),
InlineKeyboardButton("Group",url="t.me/racists_Support"),]]) ,reply_to_message_id=m.id ,disable_web_page_preview=True)
