import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
def vending():
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