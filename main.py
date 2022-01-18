from datetime import date

from aiogram import Bot, Dispatcher, types, executor
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import sqlite3
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "2038638130:AAHBxLoGg6Pa-cMXoVuiAGSBMBaGnnwsjic"
storage = MemoryStorage()


def sql_start():
    global base, cur
    base = sqlite3.connect("pizza_cool.db")
    cur = base.cursor()
    if base:
        print("Database connected OK!")
    base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price INT)")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES(?,?,?,?)", tuple(data.values, ))
        base.commit()


async def sql_delete_command(data):
    cur.execute("DELETE FROM menu WHERE name == ?", (data,))
    base.commit()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


class FSMUser(StatesGroup):
    pizza = State()
    quantity = State()


class FSMUserNap(StatesGroup):
    photo = State()
    name = State()
    price = State()


@dp.message_handler(lambda message: message.text == "Пицца", state=None)
async def menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = ["Наполетана", "Карбонара", "Футбольная", "Сырный бум", "Мясная", "Назад"]
    keyboard.add(*kb)
    for a in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(message.from_user.id, a[0], f"{a[1]}\nОписание: {a[2]}\nЦена: {a[-1]}", \
                             reply_markup=keyboard)
    await FSMUser.next()


@dp.message_handler(state=FSMUser.pizza)
async def pizza_state(message: types.Message, state: FSMContext):
    async with state.proxy() as client_data:
        client_data["user_id"] = str(message.from_user.id)
        client_data["user_name"] = message.from_user.full_name
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        client_data["date"] = d2
        client_data['pizza'] = message.text

    await FSMUser.next()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = ["1", "2", "3", "4", "5", "6"]
    keyboard.add(*kb)
    await message.reply("Теперь введите количество желаемых пиц: ", reply_markup=keyboard)


@dp.message_handler(state=FSMUser.quantity)
async def quantity_state(message: types.Message, state: FSMContext):
    async with state.proxy() as client_data:
        client_data["quantity"] = message.text
        a = cur.execute(f"SELECT price FROM menu WHERE name = '{client_data['pizza']}'").fetchone()
        client_data["price"] = int(client_data["quantity"]) * int(a[0])

    await message.reply("Заказ успешен!")
    cur.execute("INSERT or REPLACE INTO clients VALUES(?,?,?,?,?,?)", tuple(client_data.values()))
    base.commit()
    await state.finish()
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = ["Корзина", "Меню"]
    key.add(*kb)
    await message.answer("Перейти в корзину или продолжить покупки?", reply_markup=key)


@dp.message_handler(lambda message: message.text == "Меню")
async def lamafter(message: types.Message):
    await menu(message)


@dp.message_handler(lambda message: message.text == 'Корзина')
async def korzina(message: types.Message):
    read = cur.execute(f"SELECT * FROM clients WHERE user_id = {message.from_user.id}").fetchall()
    for a in read:
        await message.answer(f"{a[1]}, вы выбрали {a[3]} в количестве {a[4]}.")
        keyb = InlineKeyboardMarkup()
        key = InlineKeyboardButton(text="Оформить заказ", callback_data='key1')
        keyb.add(key)
        await message.reply("Оформить заказ?", reply_markup=keyb)


@dp.message_handler(lambda message: message.text == "Напитки")
async def napitki(message: types.Message):
    await FSMUserNap.photo.set()
    await message.reply("Загрузи фото")

@dp.message_handler(content_types=["photo"], state=FSMUserNap.photo)
async def nap_st(message: types.Message, state: FSMContext):
    async with state.proxy() as datanap:
        datanap["photo"]= message.photo[0].file_id
    await FSMUserNap.next()
    await message.reply("Теперь введи название!")


@dp.message_handler(state=FSMUserNap.name)
async def nap_name(message: types.Message, state: FSMContext):
    async with state.proxy() as datanap:
        datanap["name"] = message.text
    await FSMUserNap.next()
    await message.reply("Теперь введите цену!")

@dp.message_handler(state=FSMUserNap.price)
async def nap_price(message: types.Message, state: FSMContext):
    async with state.proxy() as datanap:
        datanap["price"] = message.text
    await message.reply(str(datanap))
    await state.finish()


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sql_delete_command(callback_query.data.replace("del ", ""))
    await callback_query.answer(text=f"{callback_query.data.replace('del ', '')} удалена.", show_alert=True)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = ["Русский", "Украинский"]
    keyboard.add(*kb)
    await message.answer("Выберите язык", reply_markup=keyboard)
    global peop
    peop = message.from_user.full_name
    await message.answer(f"Добро пожаловать, {peop}")


@dp.message_handler(lambda message: message.text == 'Русский')
async def menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = ["Пицца", "Напитки", "Акции", "Задать вопрос", "Корзина"]
    keyboard.add(*kb)
    await message.answer("Добрый день, что вас интересует?", reply_markup=keyboard)


@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes(message: types.Message):
    global ID
    ID = message.from_user.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = ["/Загрузить", "/Удалить"]
    keyboard.add(*kb1)
    await bot.send_message(message.from_user.id, "Вы администратор, что нужно?", reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        key = ["Пиццы", "Напитки", "Отменить загрузку"]
        keyb.add(*key)
        await message.reply("Выберите, что загрузить:", reply_markup=keyb)
    else:
        await message.reply('Вы не администратор бота!')


@dp.message_handler(lambda message: message.text == "Отменить загрузку")
async def cm_calcel(message: types.Message):
    await make_changes(message)


@dp.message_handler(lambda message: message.text == "Пиццы")
async def cm_starts(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Загрузи фото!")


@dp.message_handler(content_types=["photo"], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи название!")


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введи описание!")


@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введи цену!")


@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["price"] = message.text
            cur.execute("INSERT INTO menu VALUES(?,?,?,?)", tuple(data.values()))
            base.commit()
        await message.reply(str(data))
        await state.finish()


@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals="отмена"), state="*")
async def calcel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")


@dp.message_handler(commands="Удалить")
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = cur.execute("SELECT * FROM menu").fetchall()
        for a in read:
            await bot.send_photo(message.from_user.id, a[0], f"{a[1]}\nОписание: {a[2]}\nЦена {a[-1]}")
            await bot.send_message(message.from_user.id, text="|||", reply_markup=InlineKeyboardMarkup(). \
                                   add(InlineKeyboardButton(f"Удалить {a[1]}", callback_data=f'del {a[1]}')))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=sql_start())
