
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
        f"""ššš”š”š¤ š š©ššš§š! š ššš£ š„š”šš® š¢šŖšØšš šš£ š«š¤ššš šššš©šØ š¤š ššš”ššššš¢ šš§š¤šŖš„šØ. š ššš«š š š”š¤š© š¤š šš¤š¤š” šššš©šŖš§š š©ššš© š¬šš”š” šš¢ššÆš š®š¤šŖ!\n\nš“ šæš¤ š®š¤šŖ š¬šš£š© š¢š š©š¤ š„š”šš® š¢šŖšØšš šš£ š®š¤šŖš§ ššš”ššš§šš¢ šš§š¤šŖš„šØ'š«š¤ššš šššš©šØ? šš”šššØš šš”ššš  š©šš \'š ššØšš§ ššš£šŖšš” š\' ššŖš©š©š¤š£ ššš”š¤š¬ š©š¤ š š£š¤š¬ šš¤š¬ š®š¤šŖ ššš£ šŖšØš š¢š.\n\nš“ ššš š¼šØšØššØš©šš£š© š¢šŖšØš© šš šš£ š®š¤šŖš§ šš§š¤šŖš„ š©š¤ š„š”šš® š¢šŖšØšš šš£ š©šš š«š¤ššš šššš© š¤š š®š¤šŖš§ šš§š¤šŖš„.\n\nš¼ š„š§š¤šššš© šš® @iAmLiku1 ā¢ā¢ā¢""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "š š½ššØš© šš¤š§šš«šš§ ā¢ā¢ā¢ š", url="https://t.me/iAmLiku1")
                  ],[
                    InlineKeyboardButton(
                        "šØāš» Assistant šØāš»", url="https://t.me/iAmLiku1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat šļø", url="https://t.me/iAmLiku1"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ā ššŖšØšš š„š”šš®šš§ ššØ š¤š£š”šš£š š**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šļø š½ššØš© šš¤š§šš«šš§ ā¢ā¢ā¢ šļø", url= "https://t.me/ourbots1")
                ]
            ]
        )
   )
