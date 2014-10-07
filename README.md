Depends on having the following installed:
	gpsd
	gpsd-clients
	python-gps
	python-picamera


To Start GPS Daemon:
	sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock


To Kill GPS Daemon (if something isn't working right):
	sudo killall gpsd


To Run a GPS client to check to see if the GPS Daemon is running right:
	cpgs -s
