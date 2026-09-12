# Write a python program using function to convert Celsius to Fahrenheit

def CelsiusToFahrenheit(C):
    result = ((C * 9/5) + 32)
    return result

C = int(input("Enter temperature in C : "))
f = CelsiusToFahrenheit(C)
print(f"Temperature : {round(f,2)} °F") ## round give value 2 decimal point