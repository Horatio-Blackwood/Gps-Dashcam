# Adam Anderson
# October 8, 2014
# LED Test

import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, False)
    time.sleep(5)


main()
