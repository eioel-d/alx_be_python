FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temprature = int(input("Enter the temprature to convert: "))
type_of_temprature = input("Is this temprature in Celsius or Fahrenheit? (C/F): ").lower()

if type_of_temprature == "c":
    print(f"{temprature}C is {convert_to_fahrenheit(temprature)}F")
elif type_of_temprature == "f":
    print(f"{temprature}F is {convert_to_celsius(temprature)}C")
else:
    print("Invalid temprature")
