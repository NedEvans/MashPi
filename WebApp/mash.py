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

def fill_hlt():
    global hlt
    print('open tap to fill HLT')
    mash_thing.set_solenoid_1(True) #turn on hLT fill Tap
    if hlt=='empty': #when hlt is empty pause to allow water to fil past the heaters
        time.sleep(600) # pause for 10 mins
    hlt='filling'  #change state to stop the above pause and the call from main loop
    if mash_thing.read_hlt_full(True) and hlt=='filling':
            mash_thing.set_solenoid_1(False) #turn off hLT fill Tap
            hlt='full'  #change state to stop skip turning tap off and the call from main loop


def maintain_hlt_temp():
# turn heaters on and off to maintain temp
    if mash=='empty':
        temperature=step1_temp
    else:
        temperature=sparge
    if hlt_temp < temperature-0.5:
        print('turn HLT heaters on')
        mash_thing.set_heater_1(True)
        mash_thing.set_heater_2(True)
    if hlt_temp >= temperature+0.5:
        print('turn HLT heaters off')
        mash_thing.set_heater_1(False)
        mash_thing.set_heater_2(False)

def fill_mashtun():
    #open valves in preperation of filling
    print('open mash tun fill Valve')
    mash_thing.set_solenoid_3(True) #open mash tun fill Valve
    print('open HLT Drain Valve')
    mash_thing.set_solenoid_2(True) #open HLT Drain Valve
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

# Print the current switch state.
#switch = pi_thing.read_switch()
#print('Switch status: {0}'.format(switch))

while True:
    initialise() #set all solenoids to false
    time.sleep(1) #set timing cycle
    # check time to start has been reached
    now = datetime.datetime.now()
    print(now)
    if now==start_time:
    # proceed once time to start has been reached
        print("start time met")
        hlt_temp=mash_thing.read_temperatur_0() #read hlt temp.
        # fill hlt only on first cycle. subsequent cycles hlt will not be set to empty
        if hlt=='empty':
            fill_hlt() #fill hlt and change state to stop this call on subsequent loops
        maintain_hlt_temp() #turn heaters on and off to maintain the temp
        #once step 1 temp reached in hlt pump water to mash tun
        if hlt_temp == step1_temp: #temp reached
            if mash=='empty': #fill mash tun on first cycle only thenchange state to stop call.
                fill_mashtun() #start filling mash
            start_herms()
