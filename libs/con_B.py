from __future__ import division
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685() #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
# 
# servo_min = 130
# servo_mid = 380
# servo_max = 630
# 
# 
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)


class CON_B:

    def initial_condition(self):
        #초기 상태
        pwm.set_pwm(12,0,210) #로봇팔 적재된 박스 위치로
        pwm.set_pwm(15,0,180) #right(뒤로)
        pwm.set_pwm(8,0,450)  #left(위로)
        pwm.set_pwm(9,0,350) #right(앞 뒤)
        time.sleep(1)
        
    def move(self):
        
        for right in range(180,320,1):  #오른쪽모터. 앞으로 뻗음
            pwm.set_pwm(15,0,right)
            time.sleep(0.001)
    
        time.sleep(0.3)
        for left in range(450,280,-1):  #Rotate to pick up
            pwm.set_pwm(8,0,left)
            time.sleep(0.001)
        time.sleep(0.7)
        
        pwm.set_pwm(15,0,505) #right(앞 뒤)
        time.sleep(0.7)

        pwm.set_pwm(9,0,140) 
        time.sleep(0.7)  #이제 집었어
        
        #pwm.set_pwm(15,0,450) #right(앞 뒤)
        #pwm.set_pwm(8,0,220)  #left(위 아래)
        time.sleep(0.7)
        pwm.set_pwm(15,0,450)  #490->450
        pwm.set_pwm(8,0,230)
        time.sleep(0.7)
        for right in range(450,320,-1):  #천천히 들어올려 떨어지면 안 되니까
            pwm.set_pwm(15,0,right)
            time.sleep(0.001)
        time.sleep(0.7)
        for left in range(230,450,1):  #천천히 들어올려 떨어지면 안 되니까
            pwm.set_pwm(8,0,left)
            time.sleep(0.001)
        time.sleep(0.7)
        for bottom in range(210,435,1):  #천천히 컨테이너 B로 움직여. 떨어지면 안 되니까
            pwm.set_pwm(12,0,bottom)
            time.sleep(0.001)
        time.sleep(0.7)
        pwm.set_pwm(8,0,390) #400->390
        pwm.set_pwm(15,0,390) #너무 앞으로 가서 좀 뒤로 수정함. 420->390
        time.sleep(0.7)
        pwm.set_pwm(9,0,350)  
        time.sleep(1)

    def umandong(self):
#        pwm = Adafruit_PCA9685.PCA9685() #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
#        pwm.set_pwm_freq(60)
        self.initial_condition()
        self.move()
        #self.initial_condition()
        
    def yeonmudong(self):

        self.initial_condition()
        self.move()
        #time.sleep(2)
        #pwm.set_pwm(5,0,450)  #2번구역 분류판 움직이기 
        #time.sleep(4)
        #pwm.set_pwm(5,0,630)  #분류판 제자리로
        #time.sleep(1)

    def iuidong(self):
        
        self.initial_condition()
        self.move()
        #pwm.set_pwm(6,0,450)  #2번구역 분류판 움직이기 
        #time.sleep(3)
        #pwm.set_pwm(6,0,630)  #분류판 제자리로
        #time.sleep(1)
        
        #self.initial_condition()
if __name__ == "__main__":
    import sys
    mo = CON_B()