import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)#コネクションオブジェクト(データベースのアクセス)
    con.execute("CREATE TABLE books (title, price, arrival_day)")#テーブルSQL作成
    con.close()