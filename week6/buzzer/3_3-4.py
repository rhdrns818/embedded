import RPi.GPIO as GPIO
import time

BUZZER = 12
SWS = [5,6,13,19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SWS[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWS[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


sounds = [262,394,330,523]
p = GPIO.PWM(BUZZER,261)
p.start(0)

try:
  while True:
    sw1Value = GPIO.input(SWS[0])
    sw2Value = GPIO.input(SWS[1])
    sw3Value = GPIO.input(SWS[2])
    sw4Value = GPIO.input(SWS[3])

    if sw1Value == 1:
      p.start(50)
      p.ChangeFrequency(sounds[1])
      time.sleep(1.0)
    elif sw2Value == 1:
      p.start(50)
      p.ChangeFrequency(sounds[0])
      time.sleep(1.0)
    elif sw3Value == 1:
      p.start(50)
      p.ChangeFrequency(sounds[2])
      time.sleep(1.0)
    elif sw4Value == 1:
      p.start(50)
      p.ChangeFrequency(sounds[32])
      time.sleep(1.0)
    
    p.start(0)

except KeyboardInterrupt:
  pass

p.stop()
GPIO.cleanup()