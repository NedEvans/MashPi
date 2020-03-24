import time
import mashthing
import RPi.GPIO as GPIO
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Create the pi thing.
mash_thing = mashthing.MashThing()

# Print the current switch state.
switch = mash_thing.read_switch()
print('Switch status: {0}'.format(switch))

# Print the current pump state.
pump = mash_thing.read_pump()
print('Pump status: {0}'.format(pump))

#def stopFillingHLT(channel):
 #   print('Stop Filling HLT')
 #  mash_thing.set_led(True)
 #   time.sleep(3000)
 #   GPIO.input(21,False)

#GPIO.add_event_detect(21, GPIO.RISING, callback=stopFillingHLT, bouncetime=1000)

# Now loop forever blinking the LED and reading temp/humidity.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    # Blink the LED.
    mash_thing.set_led(True)
    time.sleep(0.5)
    mash_thing.set_led(False)
    time.sleep(0.5)
    # Get temp & humidity and print them out.
    temperature = mash_thing.read_temperature_0()
    print('Temperature: {0:0.2F}C'.format(temperature))
