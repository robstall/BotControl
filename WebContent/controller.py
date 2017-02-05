#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 
import ServoLib

class SpyBot:
    
    # pins
    RSRV_PIN = 16
    LSRV_PIN = 18

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.rsrv = ServoLib.CRServo(SpyBot.RSRV_PIN)
        self.lsrv = ServoLib.CRServo(SpyBot.LSRV_PIN, reversed=True)
        
    def shutdown(self):
        print 'shutdown'
        self.rsrv.speed(0)
        self.lsrv.speed(0)
        time.sleep(0.5)
        GPIO.cleanup()
        
    def test(self):
        print 'test'
        
    def move(self, speedLeft, speedRight):
        self.lsrv.speed(speedLeft)
        self.rsrv.speed(speedRight)       
        
if __name__ == "__main__":
    while True:
        bot = SpyBot() 
        bot.test()
        bot.shutdown()
        break