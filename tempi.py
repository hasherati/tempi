# v20170108-1 hasherati
# Simple web service that returns temperature using webpy and
# Adafruit's MCP9808 high percision temperature running on a Raspberry Pi

# https://learn.adafruit.com/mcp9808-temperature-sensor-python-library/software
# http://webpy.org/ most of their Hello World code still intact :)


import web
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

sensor = MCP9808.MCP9808()

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        temp = sensor.readTempC()
        if not name:
            name = 'World'
        return 'Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp))


if __name__ == "__main__":
    app.run()
