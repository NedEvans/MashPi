import RPi.GPIO as GPIO

PUMP_PIN = 2
HEATER_1_PIN = 3
HEATER_2_PIN = 4
HEATER_3_PIN = 17
SOLENOID_1_PIN = 27
SOLENOID_2_PIN = 19
SOLENOID_3_PIN = 26
SOLENOID_4_PIN = 5
SOLENOID_5_PIN = 6
SOLENOID_6_PIN = 15
SOLENOID_7_PIN = 14
SOLENOID_8_PIN = 18
SOLENOID_9_PIN = 13
SOLENOID_10_PIN = 22
FLOW_PIN = 23

SWITCH_PIN  = 24
LED_PIN     = 25


class PiThing(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        """Set Outputs"""
        GPIO.setup(PUMP_PIN, GPIO.OUT)
        GPIO.setup(HEATER_1_PIN, GPIO.OUT)
        GPIO.setup(HEATER_2_PIN, GPIO.OUT)
        GPIO.setup(HEATER_1_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_1_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_2_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_3_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_4_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_5_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_6_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_7_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_8_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_9_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_10_PIN, GPIO.OUT)
        
        GPIO.setup(LED_PIN, GPIO.OUT)
        
        '''Set Inputs'''
        '''need to add temp sensors as input through MCP3008 ADC'''
        GPIO.setup(FLOW_PIN, GPIO.IN)
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def read_switch(self):
        """Read the switch state and return its current value.
        """
        return GPIO.input(SWITCH_PIN)
        
    def read_flow(self):
        """Read the flow state and return its current value.
        
           NEED TO ADD COUNT VALUE
           MAYBE ADD TALLY DEF TO ROVIDE TOTAL COUNT
           
        """
        return GPIO.input(FLOW_PIN)


    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off)."""
        GPIO.output(LED_PIN, value)

    def set_pump(self, value):
        """Set the pump to the provided value (True = on, False = off)."""
        GPIO.output(PUMP_PIN, value)

    def set_heater_1(self, value):
        """Set the heater_1 to the provided value (True = on, False = off)."""
        GPIO.output(HEATER_1_PIN, value)

    def set_heater_2(self, value):
        """Set the heater_2 to the provided value (True = on, False = off)."""
        GPIO.output(HEATER_2_PIN, value)

    def set_heater_3(self, value):
        """Set the heater_3 to the provided value (True = on, False = off)."""
        GPIO.output(HEATER_3_PIN, value)
        
    def set_solenoid_1(self, value):
        """Set the solenoid_1 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_1_PIN, value)
        
    def set_solenoid_2(self, value):
        """Set the solenoid_2 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_2_PIN, value)
        
    def set_solenoid_3(self, value):
        """Set the solenoid_3 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_3_PIN, value)

    def set_solenoid_4(self, value):
        """Set the solenoid_4 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_4_PIN, value)

    def set_solenoid_5(self, value):
        """Set the solenoid_5 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_5_PIN, value)

    def set_solenoid_6(self, value):
        """Set the solenoid_6 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_6_PIN, value)
        
    def set_solenoid_7(self, value):
        """Set the solenoid_7 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_7_PIN, value)
        
    def set_solenoid_8(self, value):
        """Set the solenoid_8 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_8_PIN, value)
        
    def set_solenoid_9(self, value):
        """Set the solenoid_9 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_9_PIN, value)
        
    def set_solenoid_10(self, value):
        """Set the solenoid_10 to the provided value (True = on, False = off)."""
        GPIO.output(SOLENOID_10_PIN, value)
