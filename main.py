import logging, time
from config import PATH, Token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from db import Database

API_TOKEN = Token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database(PATH)
main_button = ['/roll', '/score', '/board', '/help']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(*main_button)
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
                        loop = message.text
                        for _ in range(int(loop)):
                                result =   await bot.send_dice(message.chat.id, emoji='🎰', disable_notification=True, reply_markup=keyboard)
                                time.sleep(3)
                                result = result.dice.value
                                print(result)
                                if result == 64:
                                        score = 1
                                        await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ ТРИ ТОПОРА ТЕБЕ ПОКОРНЫ ЛОВИ БАЛЛ В КОПИЛКУ")
                                        db.plus_score(message.from_user.id, score)
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
                        await bot.send_message(message.chat.id,'/score --> кол-во очков татрина в топориках, /start --> команда для участия в зачете,/roll --> комнада для прокрутки ,/board --> таблица лидеров, Прошу к боту относиться с уважением он только родился и постпенно будет развиваться, devlope stagE: PRE-ALFA-TEST'+ '\n'+ 'для тех кто хочет помочь с кодом или просто покапться в нем https://github.com/hace4/Bot_tg.git, создавайте свои ветки и пишите код!', reply_markup=keyboard)
                except MemoryError:
                        pass         
        @dp.message_handler(commands='board')
        async def send_welcome(message: types.Message):
                try:
                        leaderBoard = db.Get_table()
                        print(leaderBoard)
                        key_list = []
                        for k in leaderBoard:
                                key_list.append(int(k))
                        ld_list = sorted(key_list)[::-1]
                        key_list = []
                        k = 0
                        board = ''
                        if len(ld_list) != 1:
                                for i in ld_list:
                                        k+=1
                                        pop = leaderBoard[i]
                                        board += '{k} место занимает --> c {i} топориками {pop}'.format(i=i, k=k, pop=pop) + '\n'
                                await bot.send_message(message.chat.id, board, reply_markup=keyboard)
                        else:
                                for i in ld_list:
                                        all_game = 'у всех татаринов по --> {i} топорика'.format(i=i)
                                await bot.send_message(message.chat.id, all_game, reply_markup=keyboard)
                                
                except MemoryError:
                        pass
except MemoryError:
        print('you have erro make code debuge')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
