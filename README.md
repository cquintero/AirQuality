# Apartment Air Quality Alert System
The PurpleAir II is an accurate, low-cost air quality monitor that publishes sensor readings to both an online map and a json endpoint.
However, this does not allow for at-a-glance, visual air quality monitoring.

This simple script uses a [PurpleAir II](http://purpleair.com/) Air Quality Monitor,
Raspberry Pi, and a breadboard with an LED to visually monitor air quality.
The LED blinks slowly if air quality is concerning and quickly when air quality is bad, alerting 
us to open a window.

## Usage

You will need to connect an LED (make sure to use a resistor) to a 
Raspberry Pi's GPIO pins and set the script to run via cron jobs.

## To Do

- Add error logging functionality.
   - Track unsuccesful requests,
   - Send data once a day to a webserver?
- Build dashboard in colab to read and graph logs
   - Compare indoor sensor readings with nearby outdoor sensor readings
- On bad air events tigger text or email asking "what's going on"

## License
[MIT](https://choosealicense.com/licenses/mit/)

