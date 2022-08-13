from gpiozero import Servo
from time import sleep

servo = Servo(25)

try:
    while True:
        servo.min()
        sleep(1.5)
        servo.mid()
        sleep(2.5)
        servo.max()
        sleep(2.5)
        servo.min()
except KeyboardInterrupt:
	print("Program stopped")
