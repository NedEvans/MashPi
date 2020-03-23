import datetime
import time
import thing
import RPi.GPIO as GPIO
import mashthing
GPIO.setmode(GPIO.BCM)

#create the pi_thing
mash_thing=mashthing.MashThing()

#Brewing Data get user input for this data
start=str('2020-03-05 16:50') #date and time for brew to start

#need to create list of step number and temps
step1_temp=45.0 #celcius

mash_vol=26.0 #litres
sparge_temp=78 #celcius

#Brew Progress Variable
hlt='empty'
mash='empty'
herms=0 #step number 0-not started

def initialise():
    #Turn all valves off at start
    mash_thing.set_pump(False)
    mash_thing.set_heater_1(False)
    mash_thing.set_heater_2(False)
    mash_thing.set_heater_3(False)
    mash_thing.set_solenoid_1(False)
    mash_thing.set_solenoid_2(False)
    mash_thing.set_solenoid_3(False)
    mash_thing.set_solenoid_4(False)
    mash_thing.set_solenoid_5(False)
    mash_thing.set_solenoid_6(False)
    mash_thing.set_solenoid_7(False)
    mash_thing.set_solenoid_8(False)
    mash_thing.set_solenoid_9(False)
    mash_thing.set_solenoid_10(False)

def hlt_start():
    global hlt
    print('open tap to fill HLT')
    mash_thing.set_solenoid_1(True) #turn on hLT fill Tap
    time.sleep(600)
# turn heaters on and off to maintain temp
    if hlt_temp < step1_temp-0.5:
        print('turn HLT heaters on')
        mash_thing.set_heater_1(True)
        mash_thing.set_heater_2(True)
    if hlt_temp >= step1_temp+0.5:
        print('turn HLT heaters off')
        mash_thing.set_heater_1(False)
        mash_thing.set_heater_2(False)
    hlt='filling'  #change state

def fill_mashtun():
    #open valves in preperation of filling
    print('open mash tun fill Valve')
    mash_thing.set_solenoid_3(True)
    print('open HLT Drain Valve')
    mash_thing.set_solenoid_2(True)
    mash='filling'  #change state
    if flowmeter.tally()<=Volume and mash=='filling': #fill mash tun withthe required volume
        print('turn pump on')
    else: #once full turn pump and valves off
        print('turn pump off')
        print('close HLT Drain Valve')
        hlt='sparge' #change state to intiate second filling on next loop
        mash='mashing' #change state

def start_herms():
    if herms==0:
        print('open mash drain valve')
        print('turn on pump')
        herms=1
        #set temp depending on step number of herms
            #need a select case or reference to a list.
        # turn heaters on and off to maintaintemp
            if he_temp < temp-0.5:
                print('turn HLT heaters on')
            if he_temp >= temp+0.5:
                print('turn HLT heaters off')

#define callback function to call when the HLT is full
def stopFillingHLT(channel):
    print('Stop Filling HLT')
    mash_thing.set_solenoid_1(False)
    hlt='full'

GPIO.add_event_detect(24, GPIO.RISING, callback=stopFillingHLT, bouncetime=1000)

# Print the current switch state.
#switch = pi_thing.read_switch()
#print('Switch status: {0}'.format(switch))

while True:
    initialise()
    time.sleep(1)
    now = datetime.datetime.now()
    print(now)
    if now==start_time:
        print("start time met")
        hlt_temp=mash_thing.read_temperatur_0()
        if hlt=='empty':
            hlt_start()
        if hlt_temp == step1_temp:
            if mash=='empty':
                fill_mashtun()
            start_herms()
