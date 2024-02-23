"""drink_sqlよりdrink_TEST。dbを接続"""
from drink_sql import d_sq
cur, conn = d_sq()
def a_d():
    """2 自動販売機飲み物種類追加機能 """
    cur.execute('SELECT * FROM drink_test')
    a = cur.fetchall()
    i = ' / '.join(f'{i[0]} ￥{i[1]} 在庫:{i[2]}' for i in a)
    print(i)
    name = input("追加する飲み物の名前を入力してください：").strip()
    if name:
        for i in a:
            if i[0] == name :
                print('既に商品が存在します。')
                break
        else:
            drink_price = input("追加する飲み物の値段設定をを入力してください：")
            if drink_price.isnumeric():
                drink_stock = input("追加する飲み物の在庫数をを入力してください：")
                if drink_stock.isnumeric():
                    cur.execute('INSERT INTO drink_test(name, price, stock) values(?, ?, ?)', (name, int(drink_price), int(drink_stock),))
                    conn.commit()
                    cur.execute('SELECT * FROM drink_test')
                    a = cur.fetchall()
                    i = ' / '.join(f'{i[0]} ￥{i[1]} 在庫:{i[2]}' for i in a)
                    print(i)
                else:
                    print("数値で入力してください。")     
            else:
                print("数値で入力してください。")
    else:
        print('もう一度入力をお願いします。')