import pandas as pd
import sqlite3 as sl
film = sl.connect
cursor = connection.cursor()
cursor.execute(
     '"CREATE TABLE my_films (
        film_name VARCHAR(20) PRIMARY KEY,
        year_f INTEGER,
        vid_f Varchar(10),
        status_f boolean
)"'
)
cursor.execute(
    '"INSORT INTO my_films VALUES ('Трасса', 2024, 'детектив', False),
                                   ('Крыша мира', 2015, 'комедия', True),
                                   ('Уроки фарси', 2020, 'драма', True),
                                   ('Триггер', 2018,'драма', True),
                                   ('Золото', 2016, 'детектив', False),
                                   ('Эмпайр-Фоллс', 2005, 'мелодрама', False),
                                   ('Чертополох', 1987, 'драма',False),
                                   ('Хор', 2019, 'семейный', True),
                                   ('Филин', 2021, 'комедия', True),
                                   ('Игры', 2024, 'спорт', True)"'
sql = '"SELECT * FROM my_films"'
print(pd.read_sql(sql,connection)
connection.conmit()
cursor.close()
connection/close()
