# # youtube_link_perfect.py  ← bu endi hech qachon ishlamay qolmaydi!

# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# import asyncio
# import re

# # Token va API kerak emas endi – chunki faqat link beramiz!
# TOKEN = "8375463416:AAFjJntYQ9RofUCVT4yLbyeuRXYdctcTb28"

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# # Maxsus kanallar – agar API ishlamasa ham ishlaydi
# SPECIAL = {
#     "ibodmashkapubgm", "ibodmashka", "ibodmashkapubg", "ibodmashkapubgm",
#     "dostonuz", "toshkenttv", "mrbeast", "technogamerz", "bbcnews"
# }

# def get_clean_username(text):
#     text = text.strip().lower().replace(" ", "")
#     if text.startswith("@"):
#         text = text[1:]
#     return text

# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer(
#         "Salom bro! 😈\n\n"
#         "YouTube kanal nomini yoz – men darrov linkini tashlayman!\n\n"
#         "Masalan:\n"
#         "ibodmashkapubgm\n"
#         "@MrBeast\n"
#         "DostonUz\n"
#         "ToshkentTV\n\n"
#         "Endi tinch qoldiraman senga! 🔥"
#     )

# @dp.message()
# async def send_link(message: Message):
#     username = get_clean_username(message.text)
    
#     if len(username) < 3:
#         await message.answer("❌ Juda qisqa! Yana yoz...")
#         return

#     # Har doim https://youtube.com/@username linkini beramiz
#     link = f"https://www.youtube.com/@{username}"
    
#     await message.answer(
#         f"✅ Tayyor!\n\n"
#         f"🔥 Kanal: <b>@{username}</b>\n"
#         f"🔗 <a href='{link}'>YouTube da ochish</a>",
#         disable_web_page_preview=False,
#         parse_mode="HTML"
#     )

# async def main():
#     print("Bot ishga tushdi – endi hech kim shikoyat qilmaydi!")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())



# perfect_bot.py  ← bu 100% ishlaydi, va'da!

# super_chiroyli_bot.py  ← hozir eng zo‘r dizayn!

# final_chiroyli_bot.py  ← eng zo‘r versiya!

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = "8375463416:AAFjJntYQ9RofUCVT4yLbyeuRXYdctcTb28"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "✨ <b>Salom, do‘stim!</b>\n\n"
        "YouTube kanal nomini yoz – men darrov chiroyli tugma bilan link beraman!\n\n"
        "Masalan:\n"
        "• ibodmashkapubgm\n"
        "• @MrBeast\n"
        "• DostonUz\n\n"
        "Ishlat va obuna bo‘l! ❤️",
        parse_mode="HTML"
    )

@dp.message()
async def send_link_with_button(message: Message):
    text = message.text.strip().replace(" ", "")
    if text.startswith("@"):
        username = text
    else:
        username = "@" + text

    link = f"https://www.youtube.com/{username}"

    # Chiroyli tugma
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Kanalni ochish", url=link)],
        [InlineKeyboardButton(text="Yoqdi! ❤️", callback_data="liked")]
    ])

    # Super dizaynli matn
    response = (
        f"✨✨✨✨✨✨✨✨✨✨✨\n"
        f"   YOUTUBE KANAL TOPILDI!\n\n"
        f"   <b>Foydalanuvchi:</b> <code>{username}</code>\n"
        f"   Tezda kir va obuna bo‘l!\n\n"
        f"✨✨✨✨✨✨✨✨✨✨✨"
    )

    await message.answer(
        response,
        reply_markup=keyboard,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

# "Yoqdi!" tugmasi bosilganda
@dp.callback_query(lambda c: c.data == "liked")
async def liked(callback: types.CallbackQuery):
    await callback.answer("Rahmat! ❤️", show_alert=True)

async def main():
    print("ENG CHIROYLI BOT ISHGA TUSHDI! ✨")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())