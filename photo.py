#connect the raspi cam with the raspi pcb board and enable the camera in the raspiconfig settings 
#then open the taerminal and run the   """python photo.py"""

#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('myfirstpicbyraspi.jpg')
camera.stop_preview()

