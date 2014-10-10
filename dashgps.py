# Author:  Adam Anderson
# Date:    September 26, 2014
# Module:  dashgps.py
# Python:  2.7.3

# Dependencies:
#   gpsd
#   gpsd-clients
#   python-gps

# Make sure that the gpsd daemon is running before running this module.  It can be
# started thusly:
#   sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

# This daemon can be killed like so:
#   sudo killal gpsd

import gps
import time


class PositionReport(object):
    def __init__(self, lat, lat_err, lon, lon_err, timestamp, speed, speed_err, alt, alt_err, climb_rate, identifier):
        self.lat = lat
        self.lat_err = lat_err
        self.lon = lon
        self.lon_err = lon_err
        self.timestamp = timestamp
        self.speed = speed
        self.speed_err = speed_err
        self.alt = alt
        self.alt_err = alt_err
        self.climb_rate = climb_rate
        self.id = identifier
        self.system_time = time.time()

    def __str__(self):
        print "Position Report:\n   L/L:", self.lat, " / ", self.lon, "\n   Speed:", self.speed, "\n   Altitude:", self.alt, "\n   Report Time:", self.timestamp

    def to_csv(self):
        return str(self.system_time) + "," \
               + str(self.lat) + "," \
               + str(self.lon) + "," \
               + str(self.lat_err) + "," \
               + str(self.lon_err) + "," \
               + str(self.speed) + "," \
               + str(self.speed_err) + "," \
               + str(self.alt) + "," \
               + str(self.alt_err) + "," \
               + str(self.timestamp) + "," \
               + str(self.climb_rate) + "," \
               + str(self.id)

def get_gps_csv_header():
    return "#system-time,lat,long,lat_err,lon_err,speed(m/sec),speed_err(m/sec),alt(m),alt_err(m),fix-timestamp,climb(m/min),id"


def initialize():
    # Create and initialize a GPS session.
    gps_session = gps.gps("localhost", "2947")
    gps_session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    return gps_session


def get_posit(session, identifier):
    posit = session.next()

    lat = None
    lat_err = None
    lon = None
    lon_err = None
    time = None
    speed = None
    speed_err = None
    alt = None
    alt_err = None
    climb_rate = None
    

    if hasattr(posit, 'lat'):
        lat = posit.lat
    if hasattr(posit, 'lon'):
        lon = posit.lon
    if hasattr(posit, 'time'):
        time = posit.time
    if hasattr(posit, 'speed'):
        speed = posit.speed
    if hasattr(posit, 'alt'):
        alt = posit.alt
    if hasattr(posit, 'epx'):
        lon_err = posit.epx
    if hasattr(posit, 'epy'):
        lat_err = posit.epy
    if hasattr(posit, 'eps'):
        speed_err = posit.eps
    if hasattr(posit, 'epv'):
        alt_err = posit.epv
    if hasattr(posit, 'climb'):
        climb_rate = posit.climb

    return PositionReport(lat, lat_err, lon, lon_err, time, speed, speed_err, alt, alt_err, climb_rate, identifier)
