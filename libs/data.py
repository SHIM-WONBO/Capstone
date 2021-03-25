import pymysql.cursors

class db:
    # connection 정보
        
    def num(self, inx, a, b, c, d, e, f):
        conn = pymysql.connect(
        host = '192.168.0.32', # host name
        user = 'root', # user name
        password = '2222', # password
        db = 'ddb', # db name
        charset = 'utf8'
        )
        with conn.cursor() as cursor:
            sql = 'INSERT INTO test_num (INX, hadong, jidong, ingyedong, umandong, yeonmudong, iuidong) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (inx, a, b, c, d, e, f))
        conn.commit()

        conn.close()

    def area(self, inx, bar_data):
        conn = pymysql.connect(
        host = '192.168.0.32', # host name
        user = 'root', # user name
        password = '2222', # password
        db = 'ddb', # db name
        charset = 'utf8'
        )    
        with conn.cursor() as cursor:
            sql = 'INSERT INTO test_area (INX, AREA) VALUES (%s, %s)'
            cursor.execute(sql, (inx, bar_data))
        conn.commit()

        conn.close()