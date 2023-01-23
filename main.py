import logging, time
from config import PATH, Token, limit, time_limit, pay, pay_darts, dice_limit, darts_limit
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from db import Database
from keyboards import keyboard
from func import help_text


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
                                db.set_score(message.from_user.id, 100)
                                db.set_nickname(message.from_user.id, message.from_user.first_name)
                                print(message.from_user.id, message.from_user.first_name)
                        else:
                            await bot.send_message(message.chat.id, 'Клава подьехала',reply_markup=keyboard)
                except MemoryError:
                        pass
        
        @dp.message_handler(commands='balanc')
        async def send_welcome(message: types.Message):
                try:
                        if message.from_user.id == 736043856:
                                db.plus_score(message.from_user.id, 100)
                                await bot.send_message(message.chat.id, 'баланс пополнен',)
                except MemoryError:
                        pass

                
        @dp.message_handler(commands='roll')
        async def bot_read(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток',)
                await bot.send_message(message.chat.id, "Лимит установленный админом = {limit}".format(limit = limit))
                @dp.message_handler()
                async def bot_read(message: types.Message):
                        name, score = db.get_nick_name(message.from_user.id)
                        loop = message.text
                        db.minus_score(message.from_user.id, pay*loop)
                        all_rez = []
                        if (int(loop) <= limit or score >= pay) and (int(loop) <= limit and score >= pay):
                                for _ in range(int(loop)):
                                        result = await bot.send_dice(message.chat.id, emoji='🎰', disable_notification=True)
                                        time.sleep(time_limit)
                                        result = result.dice.value
                                        all_rez.append(result)
                                        db.plus_score(message.from_user.id, result)
                                        if result == 64:
                                                await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ {name} ТРИ ТОПОРА ТЕБЕ ПОКОРНЫ ЛОВИ 64 БАЛЛА В КОПИЛКУ".format(name = name))
                                                db.plus_score(message.from_user.id, result)
                                all_rez = sum(all_rez)
                                await bot.send_message(message.chat.id, 'За эту прокрутку {name} заработал {all_rez}'.format(name = name, all_rez=all_rez))
                        else:
                                await bot.send_message(message.chat.id, "Вы привысили лимит разовых сообщений равный: {limit} или недосаточно очков".format(limit = limit))
                                
                                
        @dp.message_handler(commands='darts')
        async def bot_read(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток',)
                await bot.send_message(message.chat.id, "Лимит установленный админом = {limit}".format(limit = darts_limit))
                @dp.message_handler()
                async def bot_read(message: types.Message):
                        name, score = db.get_nick_name(message.from_user.id)
                        loop = message.text
                        db.minus_score(message.from_user.id, pay_darts*loop)
                        all_rez = []
                        if (int(loop) <= darts_limit or score >= pay_darts) and (int(loop) <= darts_limit and score >= pay_darts):
                                for _ in range(int(loop)):
                                        result = await bot.send_dice(message.chat.id, emoji='🎯', disable_notification=True)
                                        time.sleep(time_limit)
                                        result = result.dice.value
                                        all_rez.append(result)
                                        db.plus_score(message.from_user.id, result)
                                        if result == 6:
                                                await bot.send_message(message.chat.id, "{name} ЕЕЕЕЕЕЕЙ ТОЧНО В ЦЕЬ ПОКОРНЫ ЛОВИ 6 БАЛЛА В КОПИЛКУ".format(name = name))
                                                db.plus_score(message.from_user.id, result)
                                all_rez = sum(all_rez)
                                await bot.send_message(message.chat.id, 'За эти броски {name} заработал {all_rez}'.format(name = name, all_rez=all_rez))
                        else:
                                await bot.send_message(message.chat.id, "Вы привысили лимит разовых сообщений равный: {limit} или недосаточно очков".format(limit = darts_limit))
                                
        @dp.message_handler(commands='darts')
        async def bot_read(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток',)
                await bot.send_message(message.chat.id, "Лимит установленный админом = {limit}".format(limit = dice_limit))
                @dp.message_handler()
                async def bot_read(message: types.Message):
                        name, score = db.get_nick_name(message.from_user.id)
                        loop = message.text
                        db.minus_score(message.from_user.id, pay_darts*loop)
                        all_rez = []
                        if (int(loop) <= dice_limit or score >= pay_darts) and (int(loop) <= dice_limit and score >= pay_darts):
                                for _ in range(int(loop)):
                                        result = await bot.send_dice(message.chat.id, emoji='🎯', disable_notification=True)
                                        time.sleep(time_limit)
                                        result = result.dice.value
                                        all_rez.append(result)
                                        db.plus_score(message.from_user.id, result)
                                        if result == 6:
                                                await bot.send_message(message.chat.id, "{name} ЕЕЕЕЕЕЕЙ ТОЧНО В ЦЕЬ ПОКОРНЫ ЛОВИ 6 БАЛЛА В КОПИЛКУ".format(name = name))
                                                db.plus_score(message.from_user.id, result)
                                all_rez = sum(all_rez)
                                await bot.send_message(message.chat.id, 'За эти броски {name} заработал {all_rez}'.format(name = name, all_rez=all_rez))
                        else:
                                await bot.send_message(message.chat.id, "Вы привысили лимит разовых сообщений равный: {limit} или недосаточно очков".format(limit = dice_limit))
                                        
                                        
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
                
                try:
                        leaderBoard = db.Get_table()
                        key_list = []
                        for k in leaderBoard:
                                key_list.append(int(k))
                        ld_list = sorted(key_list)[::-1]
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
        