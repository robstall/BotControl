#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging
import ServoLib

class SpyBot:
    
    # pins
    RSRV_PIN = 11
    LSRV_PIN = 13

    def __init__(self):
        logging.debug("SpyBot.init")
        GPIO.setmode(GPIO.BOARD)
        self.rsrv = ServoLib.CRServo(SpyBot.RSRV_PIN)
        self.lsrv = ServoLib.CRServo(SpyBot.LSRV_PIN, reversed=True)
        
    def shutdown(self):
        print 'shutdown'
        self.rsrv.speed(0)
        self.lsrv.speed(0)
        time.sleep(0.5)
        GPIO.cleanup()
        
    def move(self, speedLeft, speedRight):
        logging.debug("SpyBot.move speedLeft=%f, speedRight=%f" % (speedLeft, speedRight))
        self.lsrv.speed(speedLeft)
        self.rsrv.speed(speedRight)
        
    def test(self):
        print 'test'
        self.move(1.0, 1.0)
        time.sleep(2)
        self.move(-1.0, -1.0)
        time.sleep(2) 
        self.move(1.0, -1.0)
        time.sleep(2)
        self.move(-1.0, 1.0)
        time.sleep(2)     
        
if __name__ == "__main__":
    logging.basicConfig(filename="/tmp/controller.log",level=logging.DEBUG)
    bot = SpyBot() 
    bot.test()