import math


def CelToFahr(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    """
    return (celsius * 9/5) + 32

# testing
try:
    celsius = float(input("Enter temperature in Celsius: "))
    result = CelToFahr(celsius)
    print(f"{celsius}°C is equal to {result}°F")
except ValueError:
    print("Please enter a valid number.")

def min(a, b):
    """
    Return the smaller of two numbers.

    """
    return a if a <= b else b

# testing
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = min(num1, num2)
    print(f"The smaller number is: {result}")
except ValueError:
    print("Please enter valid numbers.")



def VolumeOfSphere(radius):
    """
    Calculate the volume of a sphere given its radius.

    """
    if radius < 0:
        return 0  # Return 0 for invalid negative radius
    return (4/3) * math.pi * (radius ** 3)

# testing
try:
    radius = float(input("Enter the radius of the sphere: "))
    result = VolumeOfSphere(radius)
    print(f"The volume of the sphere is: {result:.5f} cubic units")
except ValueError:
    print("Please enter a valid number.")
