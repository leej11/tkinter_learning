import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('drop table if exists data')
cur.execute('create table data(log_date TIMESTAMP, weight INT, reps INT)')
con.commit()
print('DB created')