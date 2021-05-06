import pymysql.cursors

class db:
    # connection 정보
    
    def num_w(self, a, b, c, d, e, f):
        conn = pymysql.connect(
        host = '192.168.0.46', # host name
        port = 3307,
        user = 'root', # user name
        password = 'Jmctrls4867)(12', # password
        db = 'challenger', # db name
        charset = 'utf8'
        )
        with conn.cursor() as cursor:
            sql = 'INSERT INTO amount (yeonmudong, umandong, iuidong, jidong, ingyedong, hadong) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (a, b, c, d, e, f))
        conn.commit()

        conn.close()

    def num_r(self):
        try:
            conn = pymysql.connect(
            host = '192.168.0.46', # host name
            port = 3307,
            user = 'root', # user name
            password = 'Jmctrls4867)(12', # password
            db = 'challenger', # db name
            charset = 'utf8'
            )
            
            with conn.cursor() as cursor:    
                sql = "select * from amount"
                cursor.execute(sql)
            
            rows = cursor.fetchall()
            #print(rows[-1][0], rows[-1][1], rows[-1][2], rows[-1][3], rows[-1][4], rows[-1][5], rows[-1][6])
            return rows[-1][1], rows[-1][2], rows[-1][3], rows[-1][4], rows[-1][5], rows[-1][6]
        except IndexError:
            db.num_w(self,0,0,0,0,0,0)
            conn = pymysql.connect(
            host = '192.168.0.46', # host name
            port = 3307,
            user = 'root', # user name
            password = 'Jmctrls4867)(12', # password
            db = 'challenger', # db name
            charset = 'utf8'
            )
            
            with conn.cursor() as cursor:    
                sql = "select * from amount"
                cursor.execute(sql)
            
            rows = cursor.fetchall()
            #print(rows[-1][0], rows[-1][1], rows[-1][2], rows[-1][3], rows[-1][4], rows[-1][5], rows[-1][6])
            return rows[-1][1], rows[-1][2], rows[-1][3], rows[-1][4], rows[-1][5], rows[-1][6]
        conn.commit()
        conn.close()

    def area(self, bar_data):
        conn = pymysql.connect(
        host = '192.168.0.46', # host name
        port = 3307,
        user = 'root', # user name
        password = 'Jmctrls4867)(12', # password
        db = 'challenger', # db name
        charset = 'utf8'
        )    
        with conn.cursor() as cursor:
            sql = 'INSERT INTO location (AREA) VALUES (%s)'
            cursor.execute(sql, (bar_data))
        conn.commit()

        conn.close()

if __name__ == "__main__":
    import sys
    db = db()
    db.num_r()