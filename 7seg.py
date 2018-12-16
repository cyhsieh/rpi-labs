import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

seg = (13,3,12,18,22,11,10,16)
four_num = (8,5,7,15)


digits = {
        '.':(1,1,1,1,1,1,1,0), 
        '0':(0,0,0,0,0,0,1,1),
        '1':(1,0,0,1,1,1,1,1),
        '2':(0,0,1,0,0,1,0,1),
        '3':(0,0,0,0,1,1,0,1),
        '4':(1,0,0,1,1,0,0,1),
        '5':(0,1,0,0,1,0,0,1),
        '6':(0,1,0,0,0,0,0,1),
        '7':(0,0,0,1,1,1,1,1),
        '8':(0,0,0,0,0,0,0,1),
        '9':(0,0,0,0,1,0,0,1),
        }
def setDigits(num, digit):
    for i in range(0,4):
         if i is num:
             GPIO.output(four_num[i],GPIO.HIGH)
         else:
             GPIO.output(four_num[i],GPIO.LOW)
    for n in range(0,8):
        GPIO.output(seg[n],digits[digit][n])
    time.sleep(0.005)

for n in range(0,8):
    GPIO.setup(seg[n],GPIO.OUT)

for n in range(0,4):
    GPIO.setup(four_num[n],GPIO.OUT)
    GPIO.output(four_num[n],GPIO.LOW)

#input()

#GPIO.output(four_num[2],GPIO.HIGH)
while True:
    nowtime = time.strftime("%H%M")
    d3 = nowtime[0]
    d2 = nowtime[1]
    d1 = nowtime[2]
    d0 = nowtime[3]
    # print(d3,d2,d1,d0)
    # input()
    setDigits(0,d0)
    setDigits(1,d1)
    setDigits(2,d2)
    setDigits(3,d3)
#setDigits(3,8)
#time.sleep(10)

GPIO.cleanup()
