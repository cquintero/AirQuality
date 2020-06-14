import json
import requests
import RPi.GPIO as GPIO
import time
import threading

#Comment out if not running on Rpi
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
'''

#Config
sensor_url = 'https://www.purpleair.com/json?show=44315'
check_freq = 60 #PurpleAir sensor query frequency in seconds
notification_freq = 60# notification freqency

def checkair(sensor_url):
    threading.Timer(check_freq, checkair).start()
    purpleair = requests.get(str(sensor_url))
    data = purpleair.json()
    pm2_5_cf_1 = data.get("results")[0]['pm2_5_cf_1']
    pm2_5 = float(pm2_5_cf_1)
    if 0<= pm2_5 <= 60:
        air_quality = 'Good Air'
    elif 60< pm2_5 <= 120:
        air_quality = 'Concerning Air'
    elif pm2_5 >120:
        air_quality = 'Bad Air'
    else:
        air_quality('Unknown')
    return pm2_5, air_quality, time.ctime()

pm2_5, air_quality, logtime = checkair(sensor_url)

def blink_led(air_quality):
    threading.Timer(notification_freq, blink_led).start()
    if air_quality == 'Good Air': #long blink once if good air
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(18,GPIO.LOW)
    elif air_quality == 'Concerning Air': #blink slowly if concerning air
        for _ in range(15):
            GPIO.output(18,GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(18,GPIO.LOW)
            time.sleep(.5)
    elif air_quality == 'Bad Air': #blink quickly if concerning air
        for _ in range(50):
            GPIO.output(18,GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(18,GPIO.LOW)
            time.sleep(.1)
    GPIO.cleanup()
    return
blink_led()