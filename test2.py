import sqlite3

dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('CREATE TABLE drink_test(name STRING PRIMARY KEY, price INTEGER, stock INTEGER)')
cur.execute('INSERT INTO drink_test(name, price, stock) values("コーラ", 100, 10)')
cur.execute('INSERT INTO drink_test(name, price, stock) values("モンスター", 200, 15)')

conn.commit()
conn.close()
