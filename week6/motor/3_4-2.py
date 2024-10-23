import RPi.GPIO as GPIO
import time

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
SWS = [5,6,13,19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(SWS[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

try:
  while True:
    time.sleep(0.05) #디바운싱 추가
    swValues = [GPIO.input(SWS[0]),GPIO.input(SWS[1]),GPIO.input(SWS[2]),GPIO.input(SWS[3])]

    if swValues[0] == 1:
      print("SW1")
      GPIO.output(AIN1,0)
      GPIO.output(AIN2,1)
      GPIO.output(BIN1,0)
      GPIO.output(BIN2,1)
      L_Motor.ChangeDutyCycle(50)
      R_Motor.ChangeDutyCycle(50)
    elif swValues[1] == 1:
      print("SW2")
      GPIO.output(AIN1,0)
      GPIO.output(AIN2,1)
      L_Motor.ChangeDutyCycle(50)
      R_Motor.ChangeDutyCycle(0)
    elif swValues[2] == 1:
      print("SW3")
      GPIO.output(AIN1,1)
      GPIO.output(AIN2,0)
      L_Motor.ChangeDutyCycle(50)
      R_Motor.ChangeDutyCycle(0)
    elif swValues[3] == 1:
      print("SW4")
      GPIO.output(AIN1,1)
      GPIO.output(AIN2,0)
      GPIO.output(BIN1,1)
      GPIO.output(BIN2,0)
      L_Motor.ChangeDutyCycle(50)
      R_Motor.ChangeDutyCycle(50)
    else:
      L_Motor.ChangeDutyCycle(0)
      R_Motor.ChangeDutyCycle(0)

except KeyboardInterrupt:
  pass

GPIO.cleanup()