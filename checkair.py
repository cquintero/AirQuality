import json
import requests
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


purpleair = requests.get('https://www.purpleair.com/json?show=44315')
data = purpleair.json()
pm2_5_cf_1 = data.get("results")[0]['pm2_5_cf_1']
pm2_5 = float(pm2_5_cf_1)
print(pm2_5)
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
    

if 0<= pm2_5 <= 60:
    print('Good Air')
elif 60< pm2_5 <= 120:
    for i in range(15):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(.5)
    print('Concerning Air')
elif pm2_5 >120:
    for i in range(50):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(.1)
    print('Bad Air')
else:
    print('Something Weird')


GPIO.cleanup()