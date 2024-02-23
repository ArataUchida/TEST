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
from drink_sql import d_sq
from total_menu import t_m
from vending_machine import v_m
from stock_drinks import s_d
from add_drinks import a_d
from delete_drinks import d_d
cur, conn = d_sq()
while True:
    select = input('1. 自動販売機飲み物購入機能 / 2.販売機編集 / 3.終了')
    if int(select) == 1:
        v_m()
    elif int(select) == 2:
        while True:
            select_menu = input("1 自動販売機飲み物個数追加機能 /2 自動販売機飲み物種類追加機能 /3 自動販売機飲み物種類削除機能 / 4 最初に戻る")
            if int(select_menu) == 1:
                s_d()
                break  
            elif int(select_menu) == 2:
                a_d()
                break
            elif int(select_menu) == 3:
                d_d()
                break

            elif int(select_menu) == 4:
                t_m()
                break
            else:
                print("該当番号がありません。もう一度入力して下さい：")
    elif int(select) == 3:
        print('またのご利用お待ちしています。')
        exit()
    else:
        print('該当する番号ではありません。もう一度入力して下さい。')
    exit_flag = input("販売機編集を続ける場合は「はい」を入力/ 続けない場合は「ENTER」等入力:")
    if exit_flag != 'はい':
        break