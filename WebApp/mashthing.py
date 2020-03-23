import RPi.GPIO as GPIO
import threading
import time
from gpiozero import MCP3008
import math


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


class MashThing(object):
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
        GPIO.setup(SOLENOID_1_PIN, GPIO.OUT) #HLT Fill Valve
        GPIO.setup(SOLENOID_2_PIN, GPIO.OUT) #HLT drain Valve
        GPIO.setup(SOLENOID_3_PIN, GPIO.OUT) #Mash Tun Fill Valve
        GPIO.setup(SOLENOID_4_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_5_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_6_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_7_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_8_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_9_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_10_PIN, GPIO.OUT)

        GPIO.setup(LED_PIN, GPIO.OUT)

        '''Set Inputs'''
        GPIO.setup(FLOW_PIN, GPIO.IN)
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()
        # Setup a thread to read the ADC sensor MCP3008 every 2 seconds and store
        # its last known value.
        self._temperature = None
        self._adc_thread = threading.Thread(target=self._update_adc)
        self._adc_thread.daemon = True  # Don't let this thread block exiting.
        self._adc_thread.start()

    def _update_adc(self):
        """Main function for ADC update thread, will grab new temp values every two seconds."""
        T0=MCP3008(0)
        T1=MCP3008(1)
        T2=MCP3008(2)
        counter=0
        temp_a0=0
        temp_a1=0
        temp_a2=0
        temp_b0=0
        temp_b1=0
        temp_b2=0
        temp_c0=0
        temp_c1=0
        temp_c2=0
        while True:
            with self._lock:
                # Read the temperature from the ADC and deliver weighted average
                V0=T0.value*3.3
                V1=T1.value*3.3
                V2=T2.value*3.3
                if counter ==0:
                    temp_a0 = (10.617*math.pow(V0,4))-(65.957*math.pow(V0,3))+(155.58*math.pow(V0,2))-(197.45*V0)+146.08
                    temp_a1 = (10.617*math.pow(V1,4))-(65.957*math.pow(V1,3))+(155.58*math.pow(V1,2))-(197.45*V1)+146.08
                    temp_a2 = (10.617*math.pow(V2,4))-(65.957*math.pow(V2,3))+(155.58*math.pow(V2,2))-(197.45*V2)+146.08
                if counter ==1:
                    temp_b0 = (10.617*math.pow(V0,4))-(65.957*math.pow(V0,3))+(155.58*math.pow(V0,2))-(197.45*V0)+146.08
                    temp_b1 = (10.617*math.pow(V1,4))-(65.957*math.pow(V1,3))+(155.58*math.pow(V1,2))-(197.45*V1)+146.08
                    temp_b2 = (10.617*math.pow(V2,4))-(65.957*math.pow(V2,3))+(155.58*math.pow(V2,2))-(197.45*V2)+146.08
                if counter ==2:
                    temp_c0 = (10.617*math.pow(V0,4))-(65.957*math.pow(V0,3))+(155.58*math.pow(V0,2))-(197.45*V0)+146.08
                    temp_c1 = (10.617*math.pow(V1,4))-(65.957*math.pow(V1,3))+(155.58*math.pow(V1,2))-(197.45*V1)+146.08
                    temp_c2 = (10.617*math.pow(V2,4))-(65.957*math.pow(V2,3))+(155.58*math.pow(V2,2))-(197.45*V2)+146.08
                counter=counter+1
                if counter==3:
                    counter=0
                self._temperature_0=(temp_a0+temp_b0+temp_c0)/3
                self._temperature_1=(temp_a1+temp_b1+temp_c1)/3
                self._temperature_2=(temp_a2+temp_b2+temp_c2)/3
                # Wait 2 seconds then repeat.
            time.sleep(2.0)

    def read_temperature_0(self):
        """Get the most recent temperature value (in degrees Celsius)."""
        with self._lock:
            return self._temperature_0

    def read_temperature_1(self):
        """Get the most recent temperature value (in degrees Celsius)."""
        with self._lock:
            return self._temperature_1

    def read_temperature_2(self):
        """Get the most recent temperature value (in degrees Celsius)."""
        with self._lock:
            return self._temperature_2

    def read_switch(self):
        """Read the switch state and return its current value.
        """
        with self._lock:
            return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(LED_PIN, value)

    def set_pump(self, value):
        """Set the pump to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(PUMP_PIN, value)

    def set_heater_1(self, value):
        """Set the heater_1 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(HEATER_1_PIN, value)

    def set_heater_2(self, value):
        """Set the heater_2 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(HEATER_2_PIN, value)

    def set_heater_3(self, value):
        """Set the heater_3 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(HEATER_3_PIN, value)

    def set_solenoid_1(self, value):
        """Set the solenoid_1 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_1_PIN, value)

    def set_solenoid_2(self, value):
        """Set the solenoid_2 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_2_PIN, value)

    def set_solenoid_3(self, value):
        """Set the solenoid_3 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_3_PIN, value)

    def set_solenoid_4(self, value):
        """Set the solenoid_4 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_4_PIN, value)

    def set_solenoid_5(self, value):
        """Set the solenoid_5 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_5_PIN, value)

    def set_solenoid_6(self, value):
        """Set the solenoid_6 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_6_PIN, value)

    def set_solenoid_7(self, value):
        """Set the solenoid_7 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_7_PIN, value)

    def set_solenoid_8(self, value):
        """Set the solenoid_8 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_8_PIN, value)

    def set_solenoid_9(self, value):
        """Set the solenoid_9 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_9_PIN, value)

    def set_solenoid_10(self, value):
        """Set the solenoid_10 to the provided value (True = on, False = off)."""
        with self._lock:
            GPIO.output(SOLENOID_10_PIN, value)
