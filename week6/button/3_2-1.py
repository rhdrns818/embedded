import RPi.GPIO as GPIO
import time

sw1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
  while True:
    sw1Value = GPIO.input(sw1)
    if sw1Value == 1:
      print("click")
    time.sleep(0.1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()