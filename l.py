from db import Database
from config import PATH, Token, limit, time_limit
db = Database(PATH)
leaderBoard = db.Get_table()
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
key_list = []

for k, v in leaderBoard.items():
        key_list.append(leaderBoard[k])
ld_list  = sorted(key_list)[::-1]
k = 0
board = ''
if len(ld_list) != 1:
        for i in ld_list:
                k+=1
                pop = get_key(leaderBoard, i)
                board += '{k} место занимает --> c {i} топориками {pop}'.format(i=i, k=k, pop=pop) + '\n'
print(board)