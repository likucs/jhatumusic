
# GalaxyMusic (Telegram bot project )
# Copyright (C) 2021  Prabhasha

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""𝙃𝙚𝙡𝙡𝙤 👋 𝙩𝙝𝙚𝙧𝙚! 𝙄 𝙘𝙖𝙣 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩𝙨 𝙤𝙛 𝙏𝙚𝙡𝙚𝙜𝙚𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨. 𝙄 𝙝𝙖𝙫𝙚 𝙖 𝙡𝙤𝙩 𝙤𝙛 𝙘𝙤𝙤𝙡 𝙛𝙚𝙖𝙩𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙬𝙞𝙡𝙡 𝙖𝙢𝙖𝙯𝙚 𝙮𝙤𝙪!\n\n🔴 𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙢𝙚 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙜𝙧𝙤𝙪𝙥𝙨'𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩𝙨? 𝙋𝙡𝙚𝙖𝙨𝙚 𝙘𝙡𝙞𝙘𝙠 𝙩𝙝𝙚 \'📜 𝙐𝙨𝙚𝙧 𝙈𝙖𝙣𝙪𝙖𝙡 📜\' 𝙗𝙪𝙩𝙩𝙤𝙣 𝙗𝙚𝙡𝙤𝙬 𝙩𝙤 𝙠𝙣𝙤𝙬 𝙝𝙤𝙬 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙪𝙨𝙚 𝙢𝙚.\n\n🔴 𝙏𝙝𝙚 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙩𝙝𝙚 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥.\n\n𝘼 𝙥𝙧𝙤𝙟𝙚𝙘𝙩 𝙗𝙮 @iAmLiku1 •••""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 𝘽𝙚𝙨𝙩 𝙁𝙤𝙧𝙚𝙫𝙚𝙧 ••• 📜", url="https://t.me/iAmLiku1")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Assistant 👨‍💻", url="https://t.me/iAmLiku1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat 🎙️", url="https://t.me/iAmLiku1"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ 𝙈𝙪𝙨𝙞𝙘 𝙥𝙡𝙖𝙮𝙚𝙧 𝙞𝙨 𝙤𝙣𝙡𝙞𝙣𝙚 😉**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ 𝘽𝙚𝙨𝙩 𝙁𝙤𝙧𝙚𝙫𝙚𝙧 ••• 🎙️", url="https://t.me/GalaxyLanka")
                ]
            ]
        )
   )
