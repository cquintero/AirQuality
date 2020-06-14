import json
import requests
import RPi.GPIO as GPIO
import time

#Comment out if not running on Rpi

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#Config
sensor_url = 'https://www.purpleair.com/json?show=44315'
check_freq = 60 #PurpleAir sensor query frequency in seconds
LED = 18 #GPIO port number

def checkair(sensor_url):
    purpleair = requests.get(str(sensor_url))
    data = purpleair.json()
    pm2_5_cf_1 = data.get("results")[0]['pm2_5_cf_1']
    pm2_5 = float(pm2_5_cf_1)
    if 0<= pm2_5 <= 60:
        air_quality = 'Good Air'
        GPIO.output(LED,GPIO.HIGH) #long blink once if good air
        time.sleep(5)
        GPIO.output(LED,GPIO.LOW)
    elif 60< pm2_5 <= 120:
        air_quality = 'Concerning Air'
        for _ in range(15):
            GPIO.output(LED,GPIO.HIGH) #blink slowly if concerning air
            time.sleep(.5)
            GPIO.output(LED,GPIO.LOW)
            time.sleep(.5)
    elif pm2_5 >120:
        air_quality = 'Bad Air'
        for _ in range(50):
            GPIO.output(LED,GPIO.HIGH) #blink quickly if concerning air
            time.sleep(.1)
            GPIO.output(LED,GPIO.LOW)
            time.sleep(.1)
    else:
        air_quality('Unknown')
    GPIO.cleanup()        
    return pm2_5, air_quality, time.ctime()

pm2_5, air_quality, logtime = checkair(sensor_url)