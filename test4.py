import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('SELECT * FROM drink_test')
a = cur.fetchall()
i = ' / '.join(':'.join(map(str, i)) for i in a)
print(i)
name = input("追加する飲み物の名前を入力してください：")
for i in a:
    if i[0] == name:
        print('既に商品が存在します。')
        break
else:
    drink_price = input("追加する飲み物の値段設定をを入力してください：")
    drink_stock = input("追加する飲み物の在庫数をを入力してください：")
    if drink_price.isnumeric() and drink_stock.isnumeric():
        cur.execute('INSERT INTO drink_test(name, price, stock) values(?, ?, ?)', (name, int(drink_price), int(drink_stock),))
        conn.commit()
        cur.execute('SELECT * FROM drink_test')
        a = cur.fetchall()
        i = ' / '.join(':'.join(map(str, i)) for i in a)
        conn.close()
        print(i)
    else:
        print("数値で入力してください。")
exit = input("販売機編集を続ける場合は「はい」を入力/ 続けない場合は「ENTER」等入力")
