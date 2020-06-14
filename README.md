# Apartment Air Quality Alert System

This is a simple script that uses a PurpleAir Air Quality Monitor,
Raspberry Pi, and breadboard with an LED to monitor apartment air quality.

Despite publishing air quality data to a json API, the PurpleAir device
does not allow for easy, visual airquality monitoring. I set this up
so that the LED repeatedly blinks when air quality is bad, alerting 
us to open a window. Test edit

## Usage

You will need to connect an LED (make sure to use a resistor) to a 
Raspberry Pi's GPIO pins a set the script to run via cron jobs.

## To Do

- Change architecture to run at startup, not via cron every minute
- Add logging functionality.
   - Track unsuccesful get requests, air events, errors?
   - Send data once a day to a webserver?
- Build dashboard in colab to read and graph logs
   - Compare indoor sensor readings with nearby outdoor sensor readings

## License
[MIT](https://chosealicense.com/licenses/mit/)

