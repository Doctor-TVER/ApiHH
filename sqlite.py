# название, регион, ключевые скилы
# python developer, Москва, (python, sql)
# java delevoper, Питер, (java, sql)
# ruby, Москва, (python, ruby)

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('hh.sqlite')

# Создаем курсор
cursor = conn.cursor()

cursor.execute('SELECT * from region')

result = cursor.fetchall()
print(result)

for item in result:
    print(item)
    print(type(item))

cursor.execute('SELECT * from region where name=?', ('Питер',))

print(cursor.fetchall())

# Если запрос ничего не возращает то делаем execute
cursor.execute("insert into vacancy (name, region_id, key_skills) VALUES (?, ?, ?)", ('sql analitik', 1, 2))

cursor.execute('SELECT * from vacancy')

print(cursor.fetchall())

query = 'select v.id, v.name, k.key_skill, r.name from vacancy v, ' \
        'key_skills k, region r where v.key_skills = k.id and v.region_id = r.id'

# Вывести в нормальном виде таблицу скилы + вакансии
cursor.execute(query)

print(cursor.fetchall())