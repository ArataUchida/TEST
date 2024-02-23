"""drink_TEST.db定義"""
import sqlite3
def d_sq():
    """drink_TEST.db接続"""
    dbname = 'drink_TEST.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    return cur, conn
