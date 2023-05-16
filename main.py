import psycopg2

conn = psycopg2.connect(dbname="raspisanie", user="postgres", password="12qw34er", host="127.0.0.1")
cursor = conn.cursor()

# conn.autocommit = True

# # команда для создания базы данных metanit
# sql = "CREATE DATABASE raspisanie"
#
# # выполняем код sql
# cursor.execute(sql)
# print("База данных успешно создана")

# # создаем таблицу аудиторий
# cursor.execute("CREATE TABLE classroom (id SERIAL PRIMARY KEY, nomer INTEGER,  korpus INTEGER)")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица classroom успешно создана")

# добавляем строку в таблицу people
cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (430, 1)")
cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (450, 1)")
cursor.execute("INSERT INTO classroom (nomer, korpus) VALUES (454, 1)")
# выполняем транзакцию
conn.commit()
print("Данные добавлены")

cursor.close()
conn.close()