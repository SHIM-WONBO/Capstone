from __future__ import division
import sys
import pyzbar.pyzbar as pyzbar
import cv2
import libs.bar as bar
import time
# import Adafruit_PCA9685
# import con_A
# import con_B
# import serial
import pymysql.cursors
import libs.data as data

# connection 정보
conn = pymysql.connect(
host = '192.168.0.32', # host name
    user = 'root', # user name
    password = '2222', # password
    db = 'ddb', # db name
    charset = 'utf8'
)



a = None
b = None
c = None
d = None
e = None
f = None


BAR = bar.Baread()
db = data.db()

# MO_a = con_A.CON_A()
# MO_b = con_B.CON_B()

#getChar[] = None

def barcode_read():

    global a,b,c,d,e,f

    # if __name__ == '__main__':

    #     ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    #     ser.flush()

    print("'1' : 초기화 (오류 발생 시)\n'2' : 초기화 및 프로그램 종료 \n'3' : 저장 및 프로그램 종료")

    while True:

        BAR = bar.Baread()   

        bar_data = BAR.baread()       
        


        if bar_data == "yeonmudong":
            # ser.write(b'yeonmudong')

            # if ser.in_waiting > 0:

            #     line = ser.readline().decode('utf-8').rstrip()

            #     #print(line)   

            a,b,c,d,e,f = db.num_r()
            a += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_b.yeonmudong()


        elif bar_data == "umandong":            

            a,b,c,d,e,f = db.num_r()
            b += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_b.umandong()



        elif bar_data == "iuidong":         
            # ser.write(b'iuidong')

            # if ser.in_waiting > 0:

            #     line = ser.readline().decode('utf-8').rstrip()

            #     #print(line)      

            a,b,c,d,e,f = db.num_r()
            c += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_b.iuidong()



        elif bar_data == "jidong":
            # ser.write(b'jidong')

            # if ser.in_waiting > 0:

            #     line = ser.readline().decode('utf-8').rstrip()

                #print(line)

            a,b,c,d,e,f = db.num_r()
            d += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_a.jidong()

            

        elif bar_data == "ingyedong":

            a,b,c,d,e,f = db.num_r()
            e += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_a.ingyedong()



        elif bar_data == "hadong":               
            
            # ser.write(b'hadong')

            # if ser.in_waiting > 0:

            #     line = ser.readline().decode('utf-8').rstrip()

                #print(line)

            a,b,c,d,e,f = db.num_r()
            f += 1
            db.num_w(a,b,c,d,e,f)
            db.area(bar_data)
            # MO_a.hadong()

            
 
        else:
            a,b,c,d,e,f = db.num_r()
            db.num_w(a,b,c,d,e,f)
            db.area("error")
            
 

barcode_read()

sys.exit(app.exec_())
conn.close()