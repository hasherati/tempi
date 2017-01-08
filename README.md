# tempi

This is a web service for reading terperature readings off an MCP9808
board attached to a Raspberry Pi.  To get things up and running:

* Enable I2C in raspi-config and reboot
* Wire it up per https://learn.adafruit.com/assets/19770
* sudo apt-get update
* sudo apt-get install build-essential python-dev python-pip python-smbus git
* sudo pip install RPi.GPIO
* git clone https://github.com/adafruit/Adafruit_Python_MCP9808.git
* cd Adafruit_Python_MCP9808
* sudo python setup.py install
* pip install web.py
* python tempi.py or run it as a service from cron
