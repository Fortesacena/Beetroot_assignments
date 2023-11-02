def convertToFahrenheit(number:float)->float:
    """This converts celsius to fahrenheit"""
    return number * (9/5) +32
    
def convertToCelsius(number:float)->float:
    """This converts fahrenheit to celsius"""
    return (number - 32) * (5/9)
