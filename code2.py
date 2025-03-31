import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
led = digitalio.DigitalInOut(board.GP5)


try:
    while True:
        GPIO.output(trigPin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(trigPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(trigPin, GPIO.LOW)

        start_time = time.time()
        while GPIO.input(echoPin) == 0:
            start_time = time.time()

        while GPIO.input(echoPin) == 1:
            stop_time = time.time()

        duration = stop_time - start_time
        distance = (duration * 34300) / 2

        if distance < 10:
            GPIO.output(led, GPIO.HIGH)
        else: 
            GPIO.output(led, GPIO.LOW)

        print(distance, "cm")   
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()