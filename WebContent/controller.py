#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 
import ServoLib

class SpyBot:
    
    # pins
    RSRV_PIN = 16
    LSRV_PIN = 18

    # direction
    FWD = 0
    STOP = 1
    REV = 2

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.rsrv = ServoLib.Servo(SpyBot.RSRV_PIN, 20, [1.3, 1.5, 1.7])
        self.lsrv = ServoLib.Servo(SpyBot.LSRV_PIN, 20, [1.7, 1.5, 1.3])
        
    def shutdown(self):
        print 'shutdown'
        self.rsrv.stop()
        self.lsrv.stop()
        time.sleep(0.5)
        GPIO.cleanup()
        
    def test(self):
        print 'test'
        
    def move(self, speedLeft, speedRight):
        
        
if __name__ == "__main__":
    while True:
        bot = SpyBot() 
        bot.test()
        bot.shutdown()
        break