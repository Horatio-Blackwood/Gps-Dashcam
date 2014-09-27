# Author:  Adam Anderson
# Date:    September 26, 2014
# Module:  dashcam-main.py
# Python:  2.7.3

import dashcam
import dashgps
import uuid
import time
import os

def write_line(line, outfile):
    out = open(outfile, 'a')
    out.write(line)
    out.write("\n")


def save_report(report, outfile):
    write_line(report.to_csv(), outfile)


if __name__ == "__main__":

    # Initialize variables
    output_dir = "./dashcam/" + str(int(round(time.time())))
    if not os.path.exists("./dashcam"):
        os.mkdir("./dashcam")

    os.mkdir(output_dir)
    gps_outfile = output_dir + "/gps.txt"
    gps_session = dashgps.initialize()
    
    write_line(dashgps.get_gps_csv_header(), gps_outfile)
    
    # Main Loop
    while True:
        # wait for a while
        time.sleep(5)

        # Get an id for this position report
        identifier = str(uuid.uuid4())

        # Get GPS Position Report
        report = dashgps.get_posit(gps_session, identifier)
        save_report(report, gps_outfile)

        # Get Photo
        
