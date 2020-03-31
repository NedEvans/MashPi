from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#set pins
left_switch=13 #triggers end of travel left
right_switch=25 #triggers end of travel right
R=5 #output to motor travel right
L=26 #output to motor travel left

#GPIO setup
GPIO.setup(left_switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input pin with pull down resistor
GPIO.setup(right_switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #input pin with pull down resistor
GPIO.setup(R,GPIO.OUT)
GPIO.setup(L,GPIO.OUT)

#initial state of output
GPIO.output(R,False)
GPIO.output(L,False)

#set variables
left_trigger = 0 #when left_switch activates left_trigger is turned on
right_trigger = 0 #when right_switch activates left_trigger is turned on
count=-1 #count cycles

try:
    while(1):
        while left_trigger==1:
            GPIO.output(R,True) #travel right
            if GPIO.input(right_switch)==GPIO.HIGH: #right switch activated at the end of travel
                print('Right Switch = ' + str(GPIO.input(right_switch))) #print right_swtich state, this should be '1'
                GPIO.output(R,False) #stop motion
                GPIO.output(L,False)
                sleep(2) #2 second pause
                left_trigger=0 #turn off left trigger
                right_trigger=1 #turn on right trigger
        while right_trigger==1:
            GPIO.output(L,True) #travel left
            if GPIO.input(left_switch)==GPIO.HIGH: #if left switch actiated atthe end of travel
                check = str(GPIO.input(left_switch)) #capture state of left switch
                print('left switch = ' + check)
                if check=='1': #confirm that left switch has activated. this was required to capture a false positive signal that stopped motion without triggering relay
                    GPIO.output(R,False) #stop motion
                    GPIO.output(L,False)
                    sleep(2) #2 second pause
                    left_trigger=1
                    right_trigger=0
                    count=count+1
                    print('count = ' + str(count))

except KeyboardInterrupt:
        print('Quit')
        GPIO.cleanup()
