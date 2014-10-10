# Adam Anderson
# October 8, 2014

import RPi.GPIO as GPIO
from subprocess import call
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

    # Wait until someone hits the button
    GPIO.wait_for_edge(18, GPIO.FALLING)
    # Kill the daemon.
    call(["sudo", "killall", "gpsd"])
    time.sleep(5)
    print "killed daemon."
    # start the daemon.
    call(["sudo", "gpsd", "/dev/ttyUSB0", "-F", "/var/run/gpsd.sock"])
    print "restarted daemon"
    # Start up the dashcam again, (it should die automatically when the daemon stops)
    call(["cd", "/home/pi/Desktop/gps-dashcam")])
    call(["python", "dashmain.py", ">", "/home/pi/Desktop/gps-dashcam/data/output-restart.txt"])

if __name__ == "__main__":
    main()
