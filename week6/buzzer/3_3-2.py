import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,261)
p.start(50)
sounds = [330,394,262,394,330,394,330]
try:
  while True:
    for i in range(len(sounds)):
      p.ChangeFrequency(sounds[i])
      time.sleep(1.0)

except KeyboardInterrupt:
  pass

p.stop()
GPIO.cleanup()