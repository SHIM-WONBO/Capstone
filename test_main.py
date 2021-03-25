from __future__ import division
import sys
from pyzbar import pyzbar
# import pyzbar.pyzbar as pyzbar
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


a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
inx = 1


BAR = bar.Baread()
db = data.db()
# MO_a = con_A.CON_A()
# MO_b = con_B.CON_B()

#getChar[] = None

def barcode_read():

    global a,b,c,d,e,f,inx
    print("'R' : 데이터 리셋 및 프로그램 종료 \n'S' : 데이터 저장 및 프로그램 종료")

    while True:

        BAR = bar.Baread()   

        bar_data = BAR.baread()       
        
        if bar_data == "hadong":               
              
            a += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_a.hadong()

            

        elif bar_data == "jidong":

            b += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_a.jidong()

            

        elif bar_data == "ingyedong":

            c += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_a.ingyedong()

            

        elif bar_data == "umandong":            

            d += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_b.umandong()

            

        elif bar_data == "yeonmudong":
      
            e += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_b.yeonmudong()

            

        elif bar_data == "iuidong":         

            f += 1
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, bar_data)
            inx += 1
            # MO_b.iuidong()


        else:
            db.num(inx,a,b,c,d,e,f)
            db.area(inx, "error")
            inx += 1
 

barcode_read()

sys.exit(app.exec_())
conn.close()