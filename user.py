from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from aiogram import Bot, Dispatcher, types, executor
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types, executor

import sqlite3
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
global base, cur
from aiogram.dispatcher.filters.state import State, StatesGroup

base = sqlite3.connect("pizza_cool.db")
cur = base.cursor()
base.execute("CREATE TABLE IF NOT EXISTS clients(user_id TEXT PRIMARY KEY,user_name TEXT, date TEXT, pizza TEXT, quantity INT, price FLOAT)")
base.commit()

a = cur.execute(f"SELECT price FROM menu WHERE name = 'Наполетана'").fetchone()
print(int(a[0])*2)

