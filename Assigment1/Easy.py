
def convert_to_fahrenheit(celcius):
    calculation = (celcius * 9 / 5) + 32

    print(f'{celcius} celsius is {calculation} fahrenheit.')

def convert_to_celcius(fahrenheit):
    calculation = (fahrenheit -32 ) * 5/9

    print(f'{fahrenheit} fahrenheit is {calculation} celsius.')

convert_to_fahrenheit(55)

convert_to_celcius(131)