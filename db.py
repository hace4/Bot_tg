
import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def add_user(self, user_id):
            self.cursor.execute("INSERT INTO `champion_sheep` (`user_id`) VALUES (?)", (user_id,))
    def user_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `champion_sheep` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `champion_sheep` SET `Name` = ? WHERE `user_id` = ?", (nickname, user_id,))
    def get_nick_name(self, user_id):
        result = self.cursor.execute("SELECT `Name` FROM `champion_sheep` WHERE `user_id` = ?", (user_id,)).fetchall()
        result1 = self.cursor.execute("SELECT `score` FROM `champion_sheep` WHERE `user_id` = ?", (user_id,)).fetchall()
        for row in result:
            nickname = str(row[0])
        for row in result1:
            score = str(row[0])
            return nickname, score
        
        
    def get_score(self, user_id):
        result1 = self.cursor.execute("SELECT `score` FROM `champion_sheep` WHERE `user_id` = ?", (user_id,)).fetchall()
        for row in result1:
            score = str(row[0])
            return  score
        
    def set_score(self, user_id, score):
        with self.connection:
            return self.cursor.execute("UPDATE `champion_sheep` SET `score` =   ? WHERE `user_id` = ?", (score, user_id))
    
    def plus_score(self, user_id, score):
            with self.connection:
                return self.cursor.execute("UPDATE `champion_sheep` SET `score` =  `score` +? WHERE `user_id` = ?", (score, user_id))
    def minus_score(self, user_id, score):
            with self.connection:
                return self.cursor.execute("UPDATE `champion_sheep` SET `score` =  `score` -? WHERE `user_id` = ?", (score, user_id))
            
    def Get_table(self):
        self.cursor.execute("""SELECT * from champion_sheep""")
        records = self.cursor.fetchall()
        table = {}
        for row in records:
            table[row[2]] = row[3]
        return table
            
