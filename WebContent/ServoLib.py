#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Class using PWM configured for Parallax Continuous Rotation Servo (#900-00008)
class CRServo:
    def __init__(self, pin, reversed=False):
        self.pin = pin
        self.direction = 1.0 if reversed else -1.0
        self.cycle_ms = 20.0
        frequency = 1000.0 / self.cycle_ms
        self.pulse_ms_center = 1.5
        self.pulse_ms_range = 0.2 # 1.3 - 1.7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, frequency)
        
    def speed(self, speed):
        if speed == 0:
            self.pwm.stop()
        else:
            pulse_ms = self.pulse_ms_center + self.pulse_ms_range * speed * self.direction
            dutycycle = pulse_ms / self.cycle_ms * 100.0
            self.pwm.ChangeDutyCycle(dutycycle)
            self.pwm.start(dutycycle)
  
if __name__ == "__main__":
   servo = CRServo(7)

   servo.speed(1.0)
   time.sleep(2)
   
   servo.speed(0.5)
   time.sleep(2)
   
   servo.speed(0)
   time.sleep(2)
   
   servo.speed(-1.5)
   time.sleep(2)
   
   servo.speed(1.0)
   time.sleep(2)
   
   servo.stop()

   GPIO.cleanup()
    
