#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging

# Class using PWM configured for Parallax Continuous Rotation Servo (#900-00008)
class CRServo:
    def __init__(self, pin, reversed=False):
        logging.debug("CRServo.init pin=%d" % (pin))
        self.pin = pin
        self.direction = 1.0 if reversed else -1.0
        self.cycle_ms = 20.0
        self.frequency = 1000.0 / self.cycle_ms
        self.pulse_ms_center = 1.5
        self.pulse_ms_range = 0.2 # 1.3 - 1.7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)
        
    def speed(self, speed):
        logging.debug("CRServo.speed speed=%f" % (speed))
        pulse_ms = self.pulse_ms_center + self.pulse_ms_range * speed * self.direction
        print("speed:", speed, " pulse_ms:", pulse_ms)
        dutycycle = pulse_ms / self.cycle_ms * 100.0
        self.pwm.ChangeDutyCycle(dutycycle)
        if speed == 0:
            # When stopping, it seems to help to send the 1.5ms pulse before stopping them altogether
            self.pwm.ChangeDutyCycle(0)
            
    def shutdown(self):
        self.pwm.stop()
        GPIO.cleanup()
    
    def test(self):
        self.speed(1.0)
        time.sleep(2)
        self.speed(-1.0)
        time.sleep(2)
        self.speed(0)
        time.sleep(2)
  
if __name__ == "__main__":
    logging.basicConfig(filename="/tmp/SpyBot.log",level=logging.DEBUG)
    srv1 = CRServo(11)
    srv1.test()
    srv1.shutdown()
   
    srv2 = CRServo(13)
    srv2.test()
    srv2.shutdown()