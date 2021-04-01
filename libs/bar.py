import pyzbar.pyzbar as pyzbar
import cv2
import sys
import pymysql.cursors
import libs.data as data



class Baread:
  global db 
  db = data.db()
    
  def baread(self):

    self.conn = pymysql.connect(
        host = '192.168.0.32', # host name
        user = 'root', # user name
        password = '2222', # password
        db = 'ddb', # db name
        charset = 'utf8'
        ) 

    self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 라즈베리파이에서는 매개변수 값 0 =>-1
    self.bar = None
    self.i = 0

    while(self.cap.isOpened()):
      self.ret, self.img = self.cap.read()
      self.img = cv2.resize(self.img, dsize=(780,780),interpolation = cv2.INTER_LINEAR)
      # cv2.moveWindow('img',20,200)

      self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

      self.decoded = pyzbar.decode(self.gray)

      for d in self.decoded: 
        x, y, w, h = d.rect
        d_bar = d.data.decode("utf-8")
        self.bar = d_bar
        barcode_type = d.type
        cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        self.text = '%s (%s)' % (self.bar , barcode_type)
        cv2.putText(self.img, self.text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        print(self.bar)
        return self.bar
      cv2.imshow('img', self.img)

      #return self.bar

      self.key = cv2.waitKey(1)
      if self.key == ord('2'):
        with self.conn.cursor() as cursor:
          cursor.execute('TRUNCATE test_area')
          cursor.execute('TRUNCATE test_num')
        sys.exit()
      elif self.key == ord('3'):
        sys.exit()
      elif self.key == ord('1'):
        with self.conn.cursor() as cursor:
          cursor.execute('TRUNCATE test_area')
          cursor.execute('TRUNCATE test_num')
          db.num_w(0,0,0,0,0,0)
        # self.i += 1
        # cv2.imwrite('c_%03d.jpg' % self.i, self.img) 
      

    self.cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    barcode = baread