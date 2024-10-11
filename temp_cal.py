def calsius_to_fahrenheit(calsicus):
    return (calsicus * 9/5) + 32
def calsicud_to_kelvin(calsicus):
    return calsicus + 273.15

def fahrenheit_to_calsicus(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/98 + 273.15

def kelvin_to_calsius(kelvin):
    return kelvin - 273.15 
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
print("Temprature Converter")
print("1. Calsius to fahrenheit")
print("2. Calsius to kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to celsius")
print("6. kelvin to fhrenheit")

choice = input("Enter your choice (1/2/3/4/5/6): ")

if choice in ['1', '2']:
    calsius = float(input("Enter temprature in calsius: "))
    if choice == '1':
        print(f"{calsius}^C is {calsius_to_fahrenheit(calsius)}^F")
    else:
        print(f"{calsius}^C is {calsicud_to_kelvin(calsius)}K")
elif choice in ['3', '4']:
    fahrenheit = float(input("enter temprature in fahrenheit: "))
    if choice == '3':
        print(f"{fahrenheit}^F is {fahrenheit_to_calsicus(fahrenheit)}^C")
    else:
        print(f"{fahrenheit}^F is {fahrenheit_to_kelvin(fahrenheit)}K")
elif choice in ['5', '6']:
    kelvin = float(input("Enter temprature in kelvin: "))
    if choice == '5':
        print(f"{kelvin}K is {kelvin_to_calsius(kelvin)}^C")
    else:
        print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin)}^F")   
else:
    print("invalid choice ")
