"""drink_sqlよりdrink_TEST。dbを接続"""
from drink_sql import d_sq
cur, conn = d_sq()
def d_d():
    """3 自動販売機飲み物種類削除機能 """
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