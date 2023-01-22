import logging, time
from config import PATH, Token, limit, time_limit
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from db import Database
from keyboards import keyboard
from func import leader, help_text

API_TOKEN = Token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database(PATH)

try:
        @dp.message_handler(commands='start')
        async def send_welcome(message: types.Message):
                try:
                        if not db.user_exist(message.from_user.id):
                                db.add_user(message.from_user.id,)
                                db.set_score(message.from_user.id, 0)
                                db.set_nickname(message.from_user.id, message.from_user.first_name)
                        else:
                            await bot.send_message(message.chat.id, 'Клава подьехала',reply_markup=keyboard)
                except MemoryError:
                        pass
                
                
        @dp.message_handler(commands='roll')
        async def bot_read(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток',)
                @dp.message_handler()
                async def bot_read(message: types.Message):
                        await bot.send_message(message.chat.id, "Лимит установленный админом = {limit}".format(limit = limit))
                        loop = message.text
                        if loop <= limit:
                                for _ in range(int(loop)):
                                        result =   await bot.send_dice(message.chat.id, emoji='🎰', disable_notification=True, reply_markup=keyboard)
                                        time.sleep(time_limit)
                                        result = result.dice.value
                                        if result == 64:
                                                score = 1
                                                await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ ТРИ ТОПОРА ТЕБЕ ПОКОРНЫ ЛОВИ БАЛЛ В КОПИЛКУ")
                                                db.plus_score(message.from_user.id, score)
                                        else:
                                                await message.answer(message.chat.id, "Вы привысили лимит разовых сообщений равный: {limit}".format(limit = limit))
                                        
                                        
        @dp.message_handler(commands='score')
        async def send_welcome(message: types.Message):
                try:
                        name, score = db.get_nick_name(message.from_user.id)
                        await message.answer('Татарин  {name} заработал {score} топорика'.format(name=name, score=score), reply_markup=keyboard)
                except MemoryError:
                        pass
                
                
        @dp.message_handler(commands='help')
        async def send_welcome(message: types.Message):
                try:
                        await bot.send_message(message.chat.id,help_text(), reply_markup=keyboard)
                except MemoryError:
                        pass         
                
                
        @dp.message_handler(commands='board')
        async def send_welcome(message: types.Message):
                await bot.send_message(message.chat.id, leader(), reply_markup=keyboard)

except MemoryError:
        print('you have erro make code debuge')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
