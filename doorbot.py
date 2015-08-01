import time
import RPi.GPIO as GPIO
import serial
from twython import TwythonStreamer

# Search terms
TERMS = '#watchmydoor'
ser = serial.Serial('/dev/ttyACM0', 9600)
# GPIO pin number of LED
LED = 22

# Twitter application authentication
# replace with your credentials
APP_KEY = 'RwPfiWmpcGsicFFUze2S8kbAG'
APP_SECRET = '64HB10qRMwLJH3wekwJkv3RJP6TZFK9sJfPxfmbZZotAs96dl0'
OAUTH_TOKEN = '2835817897-EJU8lEN2qv4cLq9CqtCqixF9y2G0PCfwEGDxpZl'
OAUTH_TOKEN_SECRET = 'WdcBJd1oBPjXTrmoIaL5fH29P0EiwArF8ucYQAXWflyvC'

# Setup callbacks from Twython Streamer
#
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
 			print '-'
			ser.write('a')
			

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()
