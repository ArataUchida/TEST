import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
def total():
     while True:
        select = input('1. 自動販売機飲み物購入機能 / 2.販売機編集 / 3.終了')
        if int(select) == 1:
            cur.execute('SELECT name, price, stock FROM drink_test')
            a = cur.fetchall()
            i = ' / '.join(f'{i[0]} ￥{i[1]} 在庫:{i[2]}' for i in a)
            print(i)
            select_drink = input("商品を選んでください:")
            cur.execute("update drink_test set stock = stock - 1 where name = (?)",(select_drink,))
            conn.commit()
            for i in a:
                if i[0] == select_drink:
                    print("{}：￥{}になります。".format(i[0],i[1]))
                    money_amount = i[1]
                    while True:
                        money = input("お金をお入れ下さい:")
                        if money.isnumeric():
                            if  int(money_amount) > int(money):
                                print(f"{int(money_amount) - int(money)}円足りません")
                                money_amount = int(money_amount) - int(money)
                            else:
                                print(f"{int(money) - int(money_amount)}円お釣りです。")        
                                break                  
                        else:
                            print("数値で入力してください。")
                            
                    break
            else:
                print('商品が存在しません。もう一度入力して下さい。')
        elif int(select) == 2:
            while True:
                select_meny = input("1 自動販売機飲み物個数追加機能 /2 自動販売機飲み物種類追加機能 /3 自動販売機飲み物種類削除機能 / 4 最初に戻る")
                if int(select_meny) == 1:
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
                elif int(select_meny) == 2:
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
                                    break
                                else:
                                    print("数値で入力してください。")
                                    
                            else:
                                print("数値で入力してください。")
                    else:
                        print('もう一度入力をお願いします。')
                elif int(select_meny) == 3:
                    cur.execute('SELECT * FROM drink_test')
                    a = cur.fetchall()
                    i = ' / '.join(f'{i[0]} ￥{i[1]} 在庫:{i[2]}' for i in a)
                    print(i)
                    delete_name = input("削除したい名前を入力して下さい：")
                    for i in a:
                        if i[0] == delete_name:
                            cur.execute('DELETE FROM drink_test WHERE name = (?)', (delete_name,))
                            conn.commit()
                            cur.execute('SELECT * FROM drink_test')
                            a = cur.fetchall()
                            i = ' / '.join(f'{i[0]} ￥{i[1]} 在庫:{i[2]}' for i in a)
                            print(i)
                            break
                    else:
                        print('商品が存在しません。')

                elif int(select_meny) == 4:
                    total()
                    

                else:
                    print("該当番号がありません。もう一度入力して下さい：")
                break
    
        elif int(select) == 3:
            print('プログラム終了')
            exit()
        
        else:
            print('該当する番号ではありません。もう一度入力して下さい。')
            break
        break