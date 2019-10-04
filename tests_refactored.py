#!user/bin/env python
# -*- coding: utf-8 -*-


import conversions
from conversions_refactored import convert
import unittest


symbol = u"\u00b0" # This line of code allows the degree symbol, °, to be accessible.


class KnownValues(unittest.TestCase):
    '''
    The below values are listed in order as follows:

        (Celsius, Fahrenheit, Kelvin)

    And their positions are as follows:

        ( [0], [1], [2])
    '''

    knownValuesTemp =   ((500, 932, 773.15),
                        (350, 662, 623.15),
                        (190, 374, 463.15),
                        (30, 86, 303.15),
                        (-130, -202, 143.15),
                        (-273.15, -459.67, 0))

    '''
    The below values are listed in order as follows:

        (Meters, Miles, Yards)

    And their positions are as follows:

        ( [0], [1], [2])
    '''
    
    knownValuesLength = ((16093, 10, 17600),
                        (32187, 20, 35200),
                        (48280, 30, 52800),
                        (64374, 40, 70400),
                        (80467, 50, 88000),
                        (96561, 60, 105600))
    

    def testConvertCelsiusToKelvin(self):
        print ("\n\n\nNow testing the conversion from Celsius to Kelvin using the function convertCelsiusToKelvin() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertCelsiusToKelvin(self.knownValuesTemp[i][0])
            kelvin = float(self.knownValuesTemp[i][2])
            self.assertEqual(kelvin, conversion)
            print ("     Now testing whether {:.4f}{}C is equal to {:.4f}{}K; After testing, {:.4f}{}C is in fact {:.4f}{}K; This conversion has passed the test.".format(self.knownValuesTemp[i][0], symbol, kelvin, symbol, self.knownValuesTemp[i][0], symbol, conversion, symbol))


    def testConvertCelsiusToFahrenheit(self):
        print ("\n\n\nNow testing the conversion from Celsius to Fahrenheit using the function convertCelsiusToFahrenheit() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertCelsiusToFahrenheit(self.knownValuesTemp[i][0])
            fahrenheit = self.knownValuesTemp[i][1]
            self.assertEqual(fahrenheit, conversion)
            print ("     Now testing whether {:.4f}{}C is equal to {:.4f}{}F; After testing, {:.4f}{}C is in fact {:.4f}{}F; This conversion has passed the test.".format(self.knownValuesTemp[i][0], symbol, fahrenheit, symbol, self.knownValuesTemp[i][0], symbol, conversion, symbol))


    def testConvertFahrenheitToCelsius(self):
        print ("\n\n\nNow testing the conversion from Fahrenheit to Celsius using the function convertFahrenheitToCelsius() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertFahrenheitToCelsius(self.knownValuesTemp[i][1])
            celsius = self.knownValuesTemp[i][0]
            self.assertEqual(celsius, conversion)
            print ("     Now testing whether {:.4f}{}F is equal to {:.4f}{}C; After testing, {:.4f}{}F is in fact {:.4f}{}C; This conversion has passed the test.".format(self.knownValuesTemp[i][1], symbol, celsius, symbol, self.knownValuesTemp[i][1], symbol, conversion, symbol))


    def testConvertFahrenheitToKelvin(self):
        print ("\n\n\nNow testing the conversion from Fahrenheit to Kelvin using the function convertFahrenheitToKelvin() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertFahrenheitToKelvin(self.knownValuesTemp[i][1])
            kelvin = self.knownValuesTemp[i][2]
            self.assertEqual(kelvin, conversion)
            print ("     Now testing whether {:.4f}{}F is equal to {:.4f}{}K; After testing, {:.4f}{}F is in fact {:.4f}{}K; This conversion has passed the test.".format(self.knownValuesTemp[i][0], symbol, kelvin, symbol, self.knownValuesTemp[i][0], symbol, conversion, symbol))

    def testConvertKelvinToCelsius(self):
        print ("\n\n\nNow testing the conversion from Kelvin to Celsius using the function convertKelvinToCelsius() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertKelvinToCelsius(self.knownValuesTemp[i][2])
            celsius = self.knownValuesTemp[i][0]
            self.assertEqual(celsius, conversion)
            print ("     Now testing whether {:.4f}{}K is equal to {:.4f}{}C; After testing, {:.4f}{}K is in fact {:.4f}{}C; This conversion has passed the test.".format(self.knownValuesTemp[i][2], symbol, celsius, symbol, self.knownValuesTemp[i][2], symbol, conversion, symbol))

        
    def testConvertKelvinToFahrenheit(self):
        print ("\n\n\nNow testing the conversion from Kelvin to Fahrenheit using the function convertKelvinToFahrenheit() from conversions.py:\n")

        for i in range(0, len(self.knownValuesTemp)):
            conversion = conversions.convertKelvinToFahrenheit(self.knownValuesTemp[i][2])
            fahrenheit = self.knownValuesTemp[i][1]
            self.assertEqual(fahrenheit, conversion)
            print ("     Now testing whether {:.4f}{}K is equal to {:.4f}{}F; After testing, {:.4f}{}K is in fact {:.4f}{}F; This conversion has passed the test.".format(self.knownValuesTemp[i][2], symbol, fahrenheit, symbol, self.knownValuesTemp[i][2], symbol, conversion, symbol))


    def testConvertMetersToMiles(self):
        print ("\n\n\nNow testing the conversion from Meters to Miles using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            meters = float(self.knownValuesLength[i][0])
            miles = float(self.knownValuesLength[i][1])
            conversion = float(convert('meters', 'miles', meters))
            self.assertEqual(miles, conversion)
            print ("     Now testing whether {:.4f} meters is equal to {:.4f} miles; After testing, {:.4f} meters is in fact {:.4f} miles; This conversion has passed the test.".format(meters, conversion, meters, conversion))
            

    def testConvertMetersToYards(self):
        print ("\n\n\nNow testing the conversion from Meters to Yards using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            meters = float(self.knownValuesLength[i][0])
            yards = float(self.knownValuesLength[i][2])
            conversion = float(convert('meters', 'yards', meters))
            self.assertEqual(yards, conversion)
            print ("     Now testing whether {:.4f} meters is equal to {:.4f} miles; After testing, {:.4f} meters is in fact {:.4f} miles; This conversion has passed the test.".format(meters, conversion, meters, conversion))


    def testConvertMilesToMeters(self):
        print ("\n\n\nNow testing the conversion from Miles to Meters using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            miles = float(self.knownValuesLength[i][1])
            meters = float(self.knownValuesLength[i][0])
            conversion = float(convert('miles', 'meters', miles))
            self.assertEqual(meters, conversion)
            print ("     Now testing whether {:.4f} miles is equal to {:.4f} meters; After testing, {:.4f} miles is in fact {:.4f} meters; This conversion has passed the test.".format(miles, conversion, miles, conversion))


    def testConvertMilesToYards(self):
        print ("\n\n\nNow testing the conversion from Miles to Yards using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            miles = float(self.knownValuesLength[i][1])
            yards = float(self.knownValuesLength[i][2])
            conversion = float(convert('miles', 'yards', miles))
            self.assertEqual(yards, conversion)
            print ("     Now testing whether {:.4f} miles is equal to {:.4f} yards; After testing, {:.4f} miles is in fact {:.4f} yards; This conversion has passed the test.".format(miles, conversion, miles, conversion))


    def testConvertYardsToMeters(self):
        print ("\n\n\nNow testing the conversion from Yards to Meters using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            yards = float(self.knownValuesLength[i][2])
            meters = float(self.knownValuesLength[i][0])
            conversion = float(convert('yards', 'meters', yards))
            self.assertEqual(meters, conversion)
            print ("     Now testing whether {:.4f} yards is equal to {:.4f} meters; After testing, {:.4f} yards is in fact {:.4f} meters; This conversion has passed the test.".format(yards, conversion, yards, conversion))


    def testConvertYardsToMiles(self):
        print ("\n\n\nNow testing the conversion from Yards to Miles using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            yards = float(self.knownValuesLength[i][2])
            miles = float(self.knownValuesLength[i][1])
            conversion = float(convert('yards', 'miles', yards))
            self.assertEqual(miles, conversion)
            print ("     Now testing whether {:.4f} yards is equal to {:.4f} miles; After testing, {:.4f} yards is in fact {:.4f} miles; This conversion has passed the test.".format(yards, conversion, yards, conversion))


    def testConvertYardsToYards(self):
        print ("\n\n\nNow testing the conversion from Yards to Yards using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            yards = float(self.knownValuesLength[i][2])
            conversion = float(convert('yards', 'yards', yards))
            self.assertEqual(yards, conversion)
            print ("     Now testing whether {:.4f} yards is equal to {:.4f} yards; After testing, {:.4f} yards is in fact {:.4f} yards; This conversion has passed the test.".format(yards, conversion, yards, conversion))


    def testConvertYardsToCelsius(self):
        print ("\n\n\nNow testing the conversion from Yards to Celsius using the function convert() from conversions_refactored.py:\n")

        for i in range(0, len(self.knownValuesLength)):
            yards = float(self.knownValuesLength[i][2])
            celsius = self.knownValuesTemp[i][0]
            conversion = float(convert('yards', 'celsius', yards))
            self.assertEqual(yards, conversion)
            print ("     Now testing whether {:.4f} yards is equal to {:.4f}{}C; After testing, {:.4f} yards is in fact {:.4f}{}C; This conversion has passed the test.".format(yards, conversion, symbol, yards, conversion, symbol))


if __name__ == "__main__":
    unittest.main()
