"""下記の機能を持った自動販売機システムを作成してください。
メニュー画面を作成
メニュー内容
・自動販売機飲み物購入機能
→ 今まで課題で作成した自動販売機プログラム搭載
・販売機編集
→ 以下機能を含んでいる
1 自動販売機飲み物個数追加機能
→ 既存の飲み物の個数をユーザーが指定した個数に追加できる
2 自動販売機飲み物種類追加機能
→ 既存の飲み物に加えて新しい種類の飲み物を買えるようにする
3 自動販売機飲み物種類削除機能
→ 既存の飲み物をユーザーが任意に削除できるようにする"""
import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
while True:
    select = input('1. 自動販売機飲み物購入機能 / 2.販売機編集')
    if int(select) == 1:
        cur.execute('SELECT name, price, stock FROM drink_test')
        a = cur.fetchall()
        print(a)
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
                        if  money_amount > int(money):
                            print(f"{money_amount - int(money)}円足りません")
                            money_amount = money_amount - int(money)
                        else:
                            print(f"{int(money) - money_amount}円お釣りです。")        
                            break                  
                    else:
                        print("数値で入力してください。")
    
        exit = input("続けますか？ はい／それ以外を入力")
        if exit != "はい":
            break
    elif int(select) == 2:
        while True:
            select_meny = input("1 自動販売機飲み物個数追加機能 /2 自動販売機飲み物種類追加機能 /3 自動販売機飲み物種類削除機能")
            if int(select_meny) == 1:
                cur.execute('SELECT name, stock FROM drink_test')
                a = cur.fetchall()
                print(a)
                name = input("名前を入力して下さい：")
                stock_drink = input('何個在庫しますか？')
                cur.execute("update drink_test set stock = stock + (?) where name = (?)",(stock_drink, name,))
                conn.commit()
                cur.execute('SELECT name, stock FROM drink_test')
                a = cur.fetchall()
                print(a)
                print("またのご利用お待ちしております。")
                break
            elif int(select_meny) == 2:
                cur.execute('SELECT * FROM drink_test')
                a = cur.fetchall()
                print(a)
                name = input("追加する飲み物の名前を入力してください：")
                drink_price = input("追加する飲み物の値段設定をを入力してください：")
                drink_stock = input("追加する飲み物の在庫数をを入力してください：")
                cur.execute('INSERT INTO drink_test(name, price, stock) values(?, ?, ?)', (name, drink_price, drink_stock))
                conn.commit()
                cur.execute('SELECT * FROM drink_test')
                a = cur.fetchall()
                print(a)
                print("またのご利用お待ちしております。")
                break
            elif int(select_meny) == 3:
                cur.execute('SELECT * FROM drink_test')
                a = cur.fetchall()
                print(a)
                select_list = input("1.リスト取消希望 / 2.リスト取消無し：")
                if int(select_list) == 1:
                    delete_name = input("削除したい名前を入力して下さい：")
                    cur.execute('DELETE FROM drink_test WHERE name = (?)', (delete_name,))
                    conn.commit()
                    cur.execute('SELECT * FROM drink_test')
                    a = cur.fetchall()
                    print(a)
                    conn.close()
                    break
                else:
                    print("またのご利用お待ちしております。")
                    break
            else:
                print("該当番号がありません。もう一度入力して下さい：")
        break
    else:
        print('該当する番号ではありません。もう一度入力して下さい。')