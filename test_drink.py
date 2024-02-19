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
from total_menu import total
from vending_machine import vending
from stock_drinks import stock
from add_drinks import add
from delete_drinks import delete
import sqlite3
dbname = 'drink_TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
while True:
    select = input('1. 自動販売機飲み物購入機能 / 2.販売機編集 / 3.終了')
    if int(select) == 1:
        vending()
        
    elif int(select) == 2:
        while True:
            select_meny = input("1 自動販売機飲み物個数追加機能 /2 自動販売機飲み物種類追加機能 /3 自動販売機飲み物種類削除機能 / 4 最初に戻る")
            if int(select_meny) == 1:
                stock()
                break
                
            elif int(select_meny) == 2:
                add()
                break
            elif int(select_meny) == 3:
                delete()
                break

            elif int(select_meny) == 4:
                total()
                break
            
    
    elif int(select) == 3:
        print('またのご利用お待ちしています。')
        exit()
 
    exit_flag = input("販売機編集を続ける場合は「はい」を入力/ 続けない場合は「ENTER」等入力:")
    if exit_flag != 'はい':
        break
conn.close()