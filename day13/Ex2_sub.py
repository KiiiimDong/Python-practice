import sqlite3
def 저장(db,in_data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS in_data')
    c.execute('''
                CREATE TABLE data(
                    종목명 text,
                    현재가 text,
                    전일비 text,
                    등락률 text,
                    거래량 text,
                    거래대금 text,
                    매수호가 text,
                    매도호가 text,
                    시가총액 text,
                    PER text,
                    ROE text
                )
            ''')
    for i in range(10):
        c.executemany('INSERT INTO data VALUES(:종목명,:현재가,:전일비,:등락률,:거래량,:거래대금,:매수호가,:매도호가,:시가총액,:PER,:ROE)',in_data)
    conn.commit()
    conn.close()
def 출력(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)
저장("Ex2_sub_data.db",{"data1":"data"})
출력("Ex2_sub_data.db")