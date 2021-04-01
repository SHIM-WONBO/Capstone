import pyzbar.pyzbar as pyzbar
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI_edit_ver import *


class Baread:
  def baread(self):
    self.cap = cv2.VideoCapture(-1)
    self.bar = None
    self.i = 0

    while(self.cap.isOpened()):
      self.ret, self.img = self.cap.read()
      self.img = cv2.resize(self.img, dsize=(700,600),interpolation = cv2.INTER_LINEAR)

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

      self.key = cv2.waitKey(1)
      if self.key == ord('q'):
        break
      elif self.key == ord('s'):
        self.i += 1
        cv2.imwrite('c_%03d.jpg' % self.i, self.img) 
      

  
      QApplication.processEvents()
      
    self.cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    barcode = Baread()
    barcode.baread()
