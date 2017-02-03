import RPi.GPIO as GPIO
import time

# Run the drive motors at the passed speeds where 1 is full forward, 0 is stopped,
# -1 is full reverse and values in between are slower.
def drive(speedLeft, speedRight):
    print("drive")
    if speedLeft != 0:
        GPIO.output(11,GPIO.HIGH)
    if speedRight != 0:
        GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)

def test():
    print("testing")

if __name__ == '__main__':
    test()