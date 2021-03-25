import pymysql.cursors

# connection 정보
conn = pymysql.connect(
host = '192.168.0.32', # host name
    user = 'root', # user name
    password = '2222', # password
    db = 'ddb', # db name
    charset = 'utf8'
)

data1 = 11 
data2 = ""

while True:
    with conn.cursor() as cursor:
        data1 += 1
        data2 = input("사용자 ID를 입력하세요(엔터 클릭 시 종료): ") # data2변수에 ID 입력받기 
        if data2 == "" : # 만약 data2에 아무값도 입력받지 않는다면 
            break
        sql = 'INSERT INTO test (INX, area) VALUES (%s, %s)'
        cursor.execute(sql, (data1, data2))
    conn.commit()

conn.close()