import threading
import RPi.GPIO as GPIO
import os
import pigpio
import subprocess
from time import sleep
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#run PIGPIOD as daemon
#subprocess.call(["sudo pigpiod"], shell=True)
pigpio.exceptions = False
pi = pigpio.pi()

#motor control
ENGA = 4                        #LEFT
ENGB = 17                       #RIGHT
ENABLEA = 23                    #RIGHT
ENABLEB = 24                    #LEFT

GPIO.setup(ENGA, GPIO.OUT)
GPIO.setup(ENGB, GPIO.OUT)
GPIO.setup(ENABLEA, GPIO.OUT)
GPIO.setup(ENABLEB, GPIO.OUT)

#PWM servos
#pi.set_mode(13, pigpio.OUTPUT)
#pi.set_mode(19, pigpio.OUTPUT)

#defaul servos position
pi.set_servo_pulsewidth(19, 2300)
pi.set_servo_pulsewidth(13, 1250)

#sensor control
GPIO_TRIGGER = 21
GPIO_ECHO = 26

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


#LEDS control
LIGHT_FRWD = 16
GPIO.setup(LIGHT_FRWD, GPIO.OUT)

LIGHT_BACK = 5
GPIO.setup(LIGHT_BACK, GPIO.OUT)


#directions
def frwd(going):
        with going:
                GPIO.output(ENABLEB, True)
                GPIO.output(ENABLEA, True)
                GPIO.output(ENGA, True)
                GPIO.output(ENGB, True)
                #diode
                GPIO.output(LIGHT_FRWD, True)
                GPIO.output(LIGHT_BACK, False)
def back(going):
        with going:
                GPIO.output(ENABLEB, True)
                GPIO.output(ENABLEA, True)
                GPIO.output(ENGA, False)
                GPIO.output(ENGB, False)
                #diode
                GPIO.output(LIGHT_FRWD, False)
                GPIO.output(LIGHT_BACK, True)
def stopit(going):
        with going:
                GPIO.output(ENABLEB, False)
                GPIO.output(ENABLEA, False)
                GPIO.output(ENGA, False)
                GPIO.output(ENGB, False)
                #diode
                GPIO.output(LIGHT_FRWD, False)
                GPIO.output(LIGHT_BACK, False)
def turn_back_aside(going):
        with going:
                GPIO.output(ENABLEB, True)
                GPIO.output(ENABLEA, False)
                GPIO.output(ENGA, True)
                GPIO.output(ENGB, False)
                #diode
                GPIO.output(LIGHT_FRWD, False)
                GPIO.output(LIGHT_BACK, True)
def turn_back_aside2(going):
        with going:
                GPIO.output(ENABLEB, False)
                GPIO.output(ENABLEA, True)
                GPIO.output(ENGA, False)
                GPIO.output(ENGB, True)
                #diode
                GPIO.output(LIGHT_FRWD, False)
                GPIO.output(LIGHT_BACK, True)
def measure(going):
        with going:
                while True:
                        GPIO.output(GPIO_TRIGGER, False)
                        sleep(0.05)
                        GPIO.output(GPIO_TRIGGER, True)
                        sleep(0.0001)
                        GPIO.output(GPIO_TRIGGER, False)

                        start = time.time()
                        stop = time.time()
                        while GPIO.input(GPIO_ECHO) == 0:
                                start = time.time()
                        while GPIO.input(GPIO_ECHO) == 1:
                                stop = time.time()
                        elapsed = stop - start
                        distance = elapsed * 34300
                        distance = distance / 2
                        print distance

                        if distance > 43:
                                pi.set_servo_pulsewidth(13, 1250)
                                frwd(going)
                        elif distance < 30:
                                pi.set_servo_pulsewidth(13, 500)
                                turn_back_aside(going)
                                sleep(0.5)
			elif distance < 20:
				pi.set_servo_pulsewidth(19, 500)
				stopit(going)
                        else:
                                pi.set_servo_pulsewidth(13, 2500)
                                turn_back_aside2(going)
                                sleep(0.5)


if __name__ == '__main__':
        going = threading.Semaphore(4)
        go = threading.Thread(target = frwd, args = (going, ))
        ultra = threading.Thread(target = measure, args = (going, ))
        ultra.start()
        go.start()

