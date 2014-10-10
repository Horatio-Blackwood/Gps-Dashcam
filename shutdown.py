# Adam Anderson
# October 8, 2014

import RPi.GPIO as GPIO
from subprocess import call


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

    # Wait until someone hits the button
    GPIO.wait_for_edge(17, GPIO.FALLING)
    call(["sudo", "shutdown", "-hP", "now"])


if __name__ == "__main__":
    main()
