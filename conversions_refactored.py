#!/usr/bin/env python
# -*- coding: utf-8 -*-


symbol = u"\u00b0" # This line of code allows the degree symbol, °, to be accessible.


print ('     For Temperature:')
print ('         celsius')
print ('         fahrenheit')
print ('         kelvin')
print ("Example: conversioncalcs('celsius', 'kelvin', 21)\n")
print ('     For Length:')
print ('         meters')
print ('         miles')
print ('         yards')
print ("Example: conversioncalcs('miles', 'yards', 8)\n")
print ('ONLY USE ARGUMENTS WITHIN THE SAME CATEGORIES FOR CONVERSION\n')


class ConversionNotPossible():
    pass


def convert(fromUnit, toUnit, value):

    if fromUnit.lower() == 'celsius' and toUnit.lower() == 'kelvin':
        kelvin = (float(value) + 273.15)
        return round(kelvin,4)
    
    elif fromUnit.lower() == 'celsius' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (((float(value) *9) / 5) + 32)
        return round(fahrenheit,4)
    
    elif fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'celsius':
        celsius = (((float(value) - 32) * 5) / 9)
        return round(celsius,4)
    
    elif fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'kelvin':
        kelvin = (((float(value) + 459.67) * 5) / 9)
        return round(kelvin,4)
    
    elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'celsius':
        celsius = (float(value) - 273.15)
        return round(celsius,4)
    
    elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (((float(value) * 9) / 5) - 459.67)
        return round(fahrenheit,4)


    elif fromUnit.lower() == 'miles' and toUnit.lower()== 'yards':
        yards = (float(value) * 1760)
        return round(yards,4)
    
    elif fromUnit.lower() == 'miles' and toUnit.lower()== 'meters':
        meters = (float(value) / 0.00062137)
        return round(meters,4)
    
    elif fromUnit.lower() == 'meters' and toUnit.lower()== 'miles':
        miles = (float(value) * 0.00062137)
        return round(miles,4)
        
    elif fromUnit.lower() == 'meters' and toUnit.lower()== 'yards':
        yards = (float(value) * 1.0936)
        return round(yards,4)
    
    elif fromUnit.lower() == 'yards' and toUnit.lower()== 'miles':
        miles = (float(value) * 0.00056818)
        return round(miles,4)
    
    elif fromUnit.lower() == 'yards' and toUnit.lower()== 'meters':
        meters = (float(value) / 1.0936)
        return round(meters,4)


    elif fromUnit.lower() == toUnit.lower():
        print ("     No conversion necessary. Converting {} to {} will yield same value, {:.4f}.\n".format(fromUnit, toUnit, float(value)))

    else:
        print ("     This conversion cannot be processed: Please try again using the appropriate arguments\n")
