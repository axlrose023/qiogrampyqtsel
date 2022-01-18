from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command, CommandStart, CommandHelp
from typing import Union
from aiogram.utils.callback_data import CallbackData
TOKEN = "2114789375:AAEED-CyfOITgsnsEFR2X7UF6sB-KookqiQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")

async def make_callback_data(level, category="0", subcategory="0", item_id="0")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!"
                         f"Жми /menu")


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await list_categories(message)




async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()




async def on_startup():
    print("Бот запущен!")
if __name__ == "__main__:"
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())