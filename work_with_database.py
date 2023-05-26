import psycopg2

conn = psycopg2.connect(dbname="raspisanie", user="postgres", password="12qw34er", host="127.0.0.1")
cursor = conn.cursor()

# conn.autocommit = True

# # команда для создания базы данных
# sql = "CREATE DATABASE raspisanie"
#
# # выполняем код sql
# cursor.execute(sql)
# print("База данных успешно создана")

# # создаем таблицу
# cursor.execute("CREATE TABLE classroom (id SERIAL PRIMARY KEY, nomer INTEGER, korpus INTEGER)")
# cursor.execute("CREATE TABLE rasp_1 (classroom INTEGER NOT NULL, date DATE NOT NULL, num_pair INTEGER NOT NULL, "
#                "predmet VARCHAR(200), teacher VARCHAR(200))")
#
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица rasp_1 успешно создана")
# cursor.execute("DROP TABLE classroom")
# добавляем строку в таблицу people
# cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (430, 1)")
# cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (450, 1)")
# cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (454, 1)")
# выполняем транзакцию
# conn.commit()
# print("Данные добавлены")

cursor.close()
conn.close()