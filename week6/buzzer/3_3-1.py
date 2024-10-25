import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,261)
p.start(50)
sounds = [262,394,330,349,292,440,494,523]
try:
  while True:
    for i in range(len(sounds)):
      p.ChangeFrequency(sounds[i])

except KeyboardInterrupt:
  pass

p.stop()
GPIO.cleanup()