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
        @dp.message_handler(commands='balance')
        async def send_welcome(message: types.Message):
                        if message.from_user.id == 736043856:
                                print(list(message.text.split())[-1])
                                db.plus_score(list(message.text.split())[-1], 100)
                                await bot.send_message(message.chat.id, 'Клава подьехала',reply_markup=keyboard)
                        await bot.send_message(message.chat.id, 'Клава уеехала',reply_markup=keyboard)
                                
                                
        @dp.message_handler(commands='start')
        async def send_welcome(message: types.Message):
                try:
                        if not db.user_exist(message.from_user.id):
                                db.add_user(message.from_user.id,)
                                db.set_score(message.from_user.id, 0)
                                db.set_nickname(message.from_user.id, message.from_user.first_name)
                                print(message.from_user.id, message.from_user.first_name)
                        else:
                            await bot.send_message(message.chat.id, 'Клава подьехала',reply_markup=keyboard)
                except MemoryError:
                        pass
                
        @dp.message_handler(commands='roll')
        async def bot_read(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток {limit}, , Стоимость = 100'.format(limit = limit))
                loop = 10
                all_rez2 = []
                loop = 10
                your_score = db.get_score(message.from_user.id)
                if int(your_score) >= 100:
                        db.minus_score(message.from_user.id, pay*10)
                        for _ in range(int(loop)):
                                result2 =await bot.send_dice(message.chat.id, emoji='🎰', disable_notification=True)
                                time.sleep(time_limit)
                                result2 = result2.dice.value
                                all_rez2.append(int(result2))
                                db.plus_score(message.from_user.id, result2)
                                if result2 == 64:
                                        await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ ТОЧНО В ЦЕЛЬ ПОКОРНЫ ЛОВИ 64 БАЛЛА В КОПИЛКУ")
                                        db.plus_score(message.from_user.id, result2)
                        all_rez2 = sum(all_rez2)
                        await bot.send_message(message.chat.id, 'За эти броски заработал {all_rez}'.format(all_rez=all_rez2))
                else:
                        await bot.send_message(message.chat.id, "У вас недосаточно очков ваши очки {your_score}".format(your_score=your_score))

        @dp.message_handler(commands='darts')
        async def bot_read1(message: types.Message):
                await bot.send_message(message.chat.id, 'кол-во попыток = 5 , Стоимость = 25',)
                loop = 5
                all_rez2 = []
                db.minus_score(message.from_user.id, pay_darts*5)
                your_score = db.get_score(message.from_user.id)
                if int(your_score) >= 25:
                        for _ in range(int(loop)):
                                result2 =await bot.send_dice(message.chat.id, emoji='🎯', disable_notification=True)
                                time.sleep(time_limit)
                                result2 = result2.dice.value
                                all_rez2.append(int(result2))
                                db.plus_score(message.from_user.id, result2)
                                if result2 == 6:
                                        await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ ТОЧНО В ЦЕЛЬ ПОКОРНЫ ЛОВИ 6 БАЛЛА В КОПИЛКУ")
                                        db.plus_score(message.from_user.id, result2)
                        all_rez2 = sum(all_rez2)
                        await bot.send_message(message.chat.id, 'За эти броски заработал {all_rez}'.format(all_rez=all_rez2))
                else:
                        await bot.send_message(message.chat.id, "У вас недосаточно очков ваши очки {your_score}".format(your_score=your_score))
                        
        @dp.message_handler(commands='dies')
        async def bot_read2(message: types.Message):

                await bot.send_message(message.chat.id, 'кол-во попыток = 4, Стоимость = 10',)
                loop = 4
                all_rez2 = []
                db.minus_score(message.from_user.id, pay_darts*2)
                your_score = db.get_score(message.from_user.id)
                if int(your_score) >= 10:
                        for _ in range(int(loop)):
                                result2 = await bot.send_dice(message.chat.id, emoji='🎲', disable_notification=True)
                                time.sleep(time_limit)
                                result2 = result2.dice.value
                                all_rez2.append(int(result2))
                                db.plus_score(message.from_user.id, result2)
                                if result2 == 6:
                                        await bot.send_message(message.chat.id, "ЕЕЕЕЕЕЕЙ ТОЧНО В ЦЕЬ ПОКОРНЫ ЛОВИ 6 БАЛЛА В КОПИЛКУ")
                                        db.plus_score(message.from_user.id, result2)
                        all_rez2 = sum(all_rez2)
                        await bot.send_message(message.chat.id, 'За эти броски заработал {all_rez}'.format(all_rez=all_rez2))
                else:
                         await bot.send_message(message.chat.id, "У вас недосаточно очков ваши очки {your_score}".format(your_score=your_score))
                                        
        @dp.message_handler(commands='score')
        async def send_welcome(message: types.Message):
                try:
                        name, score = db.get_nick_name(message.from_user.id)
                        await message.answer('Татарин  {name} заработал {score} топорика'.format(name=name, score=score))
                except MemoryError:
                        pass
                
                
        @dp.message_handler(commands='help')
        async def send_welcome(message: types.Message):
                try:
                        await bot.send_message(message.chat.id,help_text())
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
                                await bot.send_message(message.chat.id, all_game)
                
                except MemoryError:
                        pass
        
except MemoryError:
        print('you have erro make code debuge')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)