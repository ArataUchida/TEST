"""drink_sqlよりdrink_TEST。dbを接続"""
from drink_sql import d_sq
cur, conn = d_sq()
def v_m():
    """1. 自動販売機飲み物購入機能"""
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
            menu_amount = i[1]
            while True:
                menu = input("お金をお入れ下さい:")
                if menu.isnumeric():
                    if  int(menu_amount) > int(menu):
                        print(f"{int(menu_amount) - int(menu)}円足りません")
                        menu_amount = int(menu_amount) - int(menu)
                    else:
                        print(f"{int(menu) - int(menu_amount)}円お釣りです。")        
                        break                  
                else:
                    print("数値で入力してください。")
                    
            break
    else:
        print('商品が存在しません。もう一度入力して下さい。')
