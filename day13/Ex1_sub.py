import sqlite3
data=[{"종목명":"에이비프로바이오","PER":"-21.48"}]
db="data.db"
def 저장(db,data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
                CREATE TABLE data(
                    종목명text,
                    PER text
                )
            ''')
    c.executemany('INSERT INTO data VALUES(:종목명,:PER)', data)
    conn.commit()
    conn.close()
#첫째날 Ex1?인듯?
def 출력(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)
저장(db,data)
출력(db)
