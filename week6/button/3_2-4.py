import RPi.GPIO as GPIO
import time

sws = [5,6,13,19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sws[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sws[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sws[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sws[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
nums = [0,0,0,0]

try:
  while True:
    sw1Value = GPIO.input(sws[0])
    sw2Value = GPIO.input(sws[1])
    sw3Value = GPIO.input(sws[2])
    sw4Value = GPIO.input(sws[3])

    if sw1Value == 1:
      nums[0] += 1
      print("SW1 click", nums[0])
    elif sw2Value == 1:
      nums[1] += 1
      print("SW2 click", nums[1])
    elif sw3Value == 1:
      nums[2] += 1
      print("SW3 click", nums[2])
    elif sw4Value == 1:
      nums[3] += 1
      print("SW4 click", nums[3])
    time.sleep(0.1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()