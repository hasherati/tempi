

##This is a web service for reading terperature readings off an MCP9808 board attached to a Raspberry Pi.  

![alt tag](https://raw.githubusercontent.com/hasherati/tempi/master/annimation.gif)

To get things up and running:

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

```
pi@raspberrypi:~/Adafruit_Python_MCP9808/examples $ python tempi.py
http://0.0.0.0:8080/
192.168.1.17:41900 - - [08/Jan/2017 23:33:43] "HTTP/1.1 GET /" - 200 OK
192.168.1.84:37244 - - [08/Jan/2017 23:34:07] "HTTP/1.1 GET /" - 200 OK
192.168.1.84:37244 - - [08/Jan/2017 23:34:08] "HTTP/1.1 GET /favicon.ico" - 200 OK
192.168.1.20:59474 - - [08/Jan/2017 23:34:33] "HTTP/1.1 GET /" - 200 OK
192.168.1.20:59474 - - [08/Jan/2017 23:34:33] "HTTP/1.1 GET /favicon.ico" - 200 OK
```
