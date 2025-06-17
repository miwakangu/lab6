# SPDX-FileCopyrightText: 2024 Google LLC
# SPDX-License-Identifier: Apache-2.0

"""
This CircuitPython example reads the temperature from the onboard sensor
of the Adafruit Circuit Playground Express (CPX).

It uses the slide switch to determine the output unit:
- If the slide switch is ON (True), it converts the temperature to Fahrenheit
  and prints it.
- If the slide switch is OFF (False), it prints the temperature in Celsius.

The temperature reading and display to the serial console only occur
when Button A on the CPX is pressed.

Try moving the switch and pressing Button A to observe the temperature readings!
"""

import time
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# --- Temperature Conversion Functions ---
def cel_to_fahr(celsius):
    #Converts a temperature from Celsius to Fahrenheit.

    return (celsius * 1.8) + 32

def fahr_to_cel(fahrenheit):

    #Converts a temperature from Fahrenheit to Celsius.

    return (fahrenheit - 32) / 1.8

# Inform the user that the program has started and where to look for output.
print(" Temperature Reader Started")
print("Connect to the serial console to see temperature readings.")
print("Toggle the slide switch to change between Celsius (OFF) and Fahrenheit (ON).")
print("Press Button A to get a temperature reading!")
print("-" * 30)

while True:
    # Check if Button A is currently pressed.
    # 'cp.button_a' is True when the button is pressed, and False otherwise.
    if cp.button_a:
        # Read the raw temperature in from the sensor.
        current_celsius = cp.temperature

        # Read the state of the slide switch.
        # 'cp.switch' is True when the switch is in one position (usually right),
        # and False when in the other (usually left).
        switch_state = cp.switch

        if switch_state is True:
            # If the switch is ON (True), convert Celsius to Fahrenheit
            fahrenheit_temp = cel_to_fahr(current_celsius)
            # Print the Fahrenheit temperature, formatted to two decimal places
            print(f"Temperature F: {fahrenheit_temp:.2f}")
        else:
            # If the switch is OFF (False), print the temperature in Celsius

            print(f"Temperature C: {current_celsius:.2f}")


        time.sleep(0.5)
    else:

        time.sleep(0.05)
