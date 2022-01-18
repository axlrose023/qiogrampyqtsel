base = sqlite3.connect("tgid.db")
cur = base.cursor()
MYID = "395519902"

@dp.message_handler(commands=['moder'])
async def moderr(message: types.Message):
    if str(message.from_user.id) == MYID:
        @dp.message_handler(lambda message: message.text == z)
        async def meee(message: types.Message):
            if str(message.from_user.id) == MYID:
                await bot.send_message("Пиши ответ:")
                soob = message.text
                await bot.send_message(, f"Админ ответил вам: '{soob}'.")
            else:
                print(message.from_user.full_name)