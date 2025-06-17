# SPDX-FileCopyrightText: 2024 Google LLC
# SPDX-License-Identifier: Apache-2.0

import time

from adafruit_circuitplayground import cp


# --- Temperature Conversion Functions ---
def cel_to_fahr(celsius):
    # Converts a temperature from Celsius to Fahrenheit.

    return (celsius * 1.8) + 32


def fahr_to_cel(fahrenheit):
    # Converts a temperature from Fahrenheit to Celsius.

    return (fahrenheit - 32) / 1.8


# Inform the user that the program has started and where to look for output.
print("--- CPX Temperature Reader Started ---")
print("Connect to the serial console to see temperature readings.")
print("Toggle the slide switch to change between Celsius (OFF) and Fahrenheit (ON).")
print("Place your finger on the gold temperature sensor (near the thermometer icon) to see changes!")
print("-" * 30)

while True:
    # Read the raw temperature in Celsius from the CPX's onboard sensor.
    # The 'cp.temperature' property returns the temperature in degrees Celsius.
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
        # Print the Celsius temperature, formatted to two decimal places
        print(f"Temperature C: {current_celsius:.2f}")

    time.sleep(3)
