import sqlite3 as sq
with sq.connect("database.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER        
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER        
        ) """)
    
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (1 , 'Xusniddin' , 'Urinbayev' , 18)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (2 , 'Anvar' , 'Davronov' , 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id ,user_id , product_name , price)
                VALUES (1 ,1 , 'Olma' , 25000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id ,user_id , product_name , price)
                VALUES (2 , 2 , 'Uzum', 15000)""")
    con.commit()
    
    print("=== Foydalanuvchilar ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)
    print("=== Xaridlar ===")
    cur.execute("SELECT * FROM xaridlar")
    for row in cur.fetchall():
        print(row)
    print("=== Foydalanuvchi va Xaridlari (JOIN) ===")
    cur.execute("""
                SELECT u.first_name, u.last_name, x.product_name, x.price
                FROM users u
                LEFT JOIN xaridlar x ON u.id = x.user_id
                """)
    for row in cur.fetchall():
        print(row)


    cur.execute("DELETE FROM users WHERE id = 2")
    con.commit()
    
    print("\n=== id=2 o'chirilgandan keyin users jadvali ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)
        
    cur.execute("DELETE FROM xaridlar WHERE price < 20000")
    con.commit()
    
    print("\n=== Narxi 20000 dan past xaridlar o'chirildi ===")
    cur.execute("SELECT * FROM xaridlar")
    for row in cur.fetchall():
        print(row)
    
    cur.execute("DELETE FROM xaridlar")
    con.commit()
    
    print("\n=== xaridlar jadvali tozalandi (jadval bor, lekin bo'sh) ===")
    cur.execute("SELECT * FROM xaridlar")
    print(cur.fetchall())
    
    cur.execute("DROP TABLE IF EXISTS xaridlar")
    con.commit()
    
    
    print("\n=== xaridlar jadvali butunlay o'chirildi (DROP TABLE) ===")


    try:
        cur.execute("SELECT * FROM xaridlar")
    except sq.OperationalError as e:
        print(f"Xatolik: {e}")  

    cur.execute("DROP TABLE IF EXISTS users")
    con.commit()
    print("users jadvali ham o'chirildi")   
    
    
    
    
    
    
    
    
    
    