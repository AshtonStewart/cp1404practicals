"""cp1404 Ashton Stewart
Program to get a temperature from the user that is then converted between Farenheit and Celcius
"""

def Ctof(temperature):
    temperature = (temperature * 1.8) + 32
    print(f"Result: {temperature:.2f} F")

def Ftoc(temperature):
    temperature = (temperature - 32) / 1.8
    print(f"Result: {temperature:.2f} C")

Ftoc(32)
Ctof(10)