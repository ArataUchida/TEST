import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
def stock():
    cur.execute('SELECT name, stock FROM drink_test')
    a = cur.fetchall()
    i = ' / '.join(f'{i[0]} 在庫:{i[1]}' for i in a)
    print(i)
    name = input("名前を入力して下さい：")
    for i in a:
        if i[0] == name:
            stock_drink = input('何個在庫しますか？')
            if stock_drink.isnumeric():
                cur.execute("update drink_test set stock = stock + (?) where name = (?)",(int(stock_drink), name,))
                conn.commit()
                cur.execute('SELECT name, stock FROM drink_test')
                a = cur.fetchall()
                i = ' / '.join(f'{i[0]} 在庫:{i[1]}' for i in a)
                print(i)
                break 
            else:
                print("数値で入力してください。")
            break
    else:
        print('商品が存在しません。')