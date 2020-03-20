import time

import mashthing


# Create the pi thing.
mash_thing = mashthing.MashThing()

# Print the current switch state.
switch = mash_thing.read_switch()
print('Switch status: {0}'.format(switch))

# Now loop forever blinking the LED and reading temp/humidity.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    # Blink the LED.
    mash_thing.set_led(True)
    time.sleep(0.5)
    mash_thing.set_led(False)
    time.sleep(0.5)
    # Get temp & humidity and print them out.
    temperature = mash_thing.get_temperature()
    print('Temperature: {0:0.2F}C'.format(temperature))
