import pymysql.cursors
import libs.data as data

db = data.db()
a = db.num_r()
print(a)