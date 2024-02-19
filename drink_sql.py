def drink_sql():
    import sqlite3
    dbname = 'drink_TEST.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    conn.close()