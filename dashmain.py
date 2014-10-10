# Author:  Adam Anderson
# Date:    September 26, 2014
# Module:  dashcam-main.py
# Python:  2.7.3

import dashcam
import dashgps
import reset
import uuid
import time
import os

import RPi.GPIO as GPIO

def write_line(line, outfile):
    out = open(outfile, 'a')
    out.write(line)
    out.write("\n")


def save_report(report, outfile):
    write_line(report.to_csv(), outfile)


if __name__ == "__main__":

    # Initialize variables
    output_dir = "./data/" + str(int(round(time.time())))
    pic_dir = output_dir + "/pics"
    if not os.path.exists("./data"):
        os.mkdir("./data")

    os.mkdir(output_dir)
    os.mkdir(pic_dir)
    gps_outfile = output_dir + "/gps.txt"
    gps_session = dashgps.initialize()
    cam = dashcam.initialize(1280, 720)

    # Number of times that we can allow 'None' fix before restarting
    # The daemon and camera ( 12 * 10 seconds = 2 minutes)
    maxFailures = 12
    currentFailures = 0

    # Set up GPIO for bad fix LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    # Init GPS CSV file
    write_line(dashgps.get_gps_csv_header(), gps_outfile)
    
    # Main Loop
    while True:
        # wait for a while
        time.sleep(10)

        # Get an id for this position report
        identifier = str(uuid.uuid4())

        # Get GPS Position Report
        report = dashgps.get_posit(gps_session, identifier)
        save_report(report, gps_outfile)

        # Automatically handle reset
        if report.lat == None:
            # If we get a null position report, light up the warning LED.
            GPIO.output(7, True)
            currentFailures += 1
            if currentFailures > maxFailuresmax:
                GPIO.output(7, False)
                reset.reset()
        else:
            # if the position report is good, turn out the light.
            GPIO.output(7, False)
            currentFailures = 0

        # Get Photo
        dashcam.take_picture(cam, pic_dir + "/" + identifier + ".jpg")
