from db import Database
from config import PATH


db = Database(PATH)


def leader():
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
                return board
        else:
                for i in ld_list:
                        all_game = 'у всех татаринов по --> {i} топорика'.format(i=i)
                return all_game
    except MemoryError:
        pass
    


def help_text():
    text = '/score --> кол-во очков татрина в топориках, /start --> команда для участия в зачете,/roll --> комнада для прокрутки ,/board --> таблица лидеров, Прошу к боту относиться с уважением он только родился и постпенно будет развиваться, devlope stagE: PRE-ALFA-TEST'+ '\n'+ 'для тех кто хочет помочь с кодом или просто покапться в нем https://github.com/hace4/Bot_tg.git, создавайте свои ветки и пишите код!'
    return text