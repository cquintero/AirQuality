import json
import requests
import RPi.GPIO as GPIO
import time
import csv

#Config
sensor_url = 'https://www.purpleair.com/json?show=44315'
check_freq = 60 #PurpleAir sensor query frequency in seconds
LED = 18 #Using port 18 on the Raspberry Pi. Change if using a different port

def checkair(sensor_url):
    purpleair = requests.get(str(sensor_url)) #Get json from PurpleAir website
    data = purpleair.json() 
    pm2_5_cf_1 = data.get("results")[0]['pm2_5_cf_1'] #extract pm2.5 particle count from json
    pm2_5 = float(pm2_5_cf_1)
    if 0<= pm2_5 <=60: #evaluate current air quality
        air_quality = 'Good Air'
        blink_led(1,1) #blink 1x if good air
    elif 60< pm2_5 <=120:
        air_quality = 'Concerning Air'
        blink_led(10,1) #blink 10x slowly if concerning air
    elif pm2_5 >120:
        air_quality = 'Bad Air'
        blink_led(100,.1) #blink 100x quickly if bad air
    else:
        air_quality('Unknown')
    return pm2_5, air_quality, time.ctime()

def blink_led(blink_num, blink_speed):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED,GPIO.OUT) 
    for _ in range(blink_num):
        GPIO.output(LED,GPIO.HIGH) #turn LED on
        time.sleep(blink_speed) 
        GPIO.output(LED,GPIO.LOW) #turn LED off
        time.sleep(blink_speed)
    GPIO.cleanup()


pm2_5, air_quality, logtime = checkair(sensor_url)

if air_quality == 'Bad Air': #notify me via text via ifttt that there's bad air
        requests.post('https://maker.ifttt.com/trigger/bad_air/with/key/gTCWrvHsuzzzVx_IsH5AdxuKTeXh2OMVRQLHD47ZyvJ')

with open('airqualitylog.csv', 'a', newline='') as aqlog: #log to csv file
    csvwriter = csv.writer(aqlog)
    csvwriter.writerow([logtime, air_quality, pm2_5])
