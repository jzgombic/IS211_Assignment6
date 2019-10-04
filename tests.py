#!user/bin/env python
# -*- coding: utf-8 -*-


import conversions
import unittest


deg = u"\u00b0" # This line of code allows the degree symbol, °, to be accessible.


class KnownValues(unittest.TestCase):
    '''
    The below values are listed in order as follows:

        (Celsius, Fahrenheit, Kelvin)

    And their positions are as follows:

        ( [0], [1], [2])
    '''

    knownValues =   ((500.00, 932.00, 773.15),
                     (350.00, 662.00, 623.15),
                     (190.00, 374.00, 463.15),
                     (30.00, 86.00, 303.15),
                     (-130.00, -202.00, 143.15),
                     (-273.15, -459.67, 0.00))
    

    def testConvertCelsiusToKelvin(self):
        print ("\n\n\nNow testing the conversion from Celsius to Kelvin using the function convertCelsiusToKelvin() from conversions.py:\n")

        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertCelsiusToKelvin(self.knownValues[i][0])
            kelvin = float(self.knownValues[i][2])
            self.assertEqual(kelvin, conversion)
            print ("     Now testing whether {:.4f}{}C is equal to {:.4f}{}K; After testing, {:.4f}{}C is in fact {:.4f}{}K; This conversion has passed the test.".format(self.knownValues[i][0], deg, kelvin, deg, self.knownValues[i][0], deg, conversion, deg))


    def testConvertCelsiusToFahrenheit(self):
        print ("\n\n\nNow testing the conversion from Celsius to Fahrenheit using the function convertCelsiusToFahrenheit() from conversions.py:\n")

        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertCelsiusToFahrenheit(self.knownValues[i][0])
            fahrenheit = self.knownValues[i][1]
            self.assertEqual(fahrenheit, conversion)
            print ("     Now testing whether {:.4f}{}C is equal to {:.4f}{}F; After testing, {:.4f}{}C is in fact {:.4f}{}F; This conversion has passed the test.".format(self.knownValues[i][0], deg, fahrenheit, deg, self.knownValues[i][0], deg, conversion, deg))


    def testConvertFahrenheitToCelsius(self):
        print ("\n\n\nNow testing the conversion from Fahrenheit to Celsius using the function convertFahrenheitToCelsius() from conversions.py:\n")

        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertFahrenheitToCelsius(self.knownValues[i][1])
            celsius = self.knownValues[i][0]
            self.assertEqual(celsius, conversion)
            print ("     Now testing whether {:.4f}{}F is equal to {:.4f}{}C; After testing, {:.4f}{}F is in fact {:.4f}{}C; This conversion has passed the test.".format(self.knownValues[i][1], deg, celsius, deg, self.knownValues[i][1], deg, conversion, deg))


    def testConvertFahrenheitToKelvin(self):
        print ("\n\n\nNow testing the conversion from Fahrenheit to Kelvin using the function convertFahrenheitToKelvin() from conversions.py:\n")

        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertFahrenheitToKelvin(self.knownValues[i][1])
            kelvin = self.knownValues[i][2]
            self.assertEqual(kelvin, conversion)
            print ("     Now testing whether {:.4f}{}F is equal to {:.4f}{}K; After testing, {:.4f}{}F is in fact {:.4f}{}K; This conversion has passed the test.".format(self.knownValues[i][1], deg, kelvin, deg, self.knownValues[i][1], deg, conversion, deg))

    def testConvertKelvinToCelsius(self):
        print ("\n\n\nNow testing the conversion from Kelvin to Celsius using the function convertKelvinToCelsius() from conversions.py:\n")
        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertKelvinToCelsius(self.knownValues[i][2])
            celsius = self.knownValues[i][0]
            self.assertEqual(celsius, conversion)
            print ("     Now testing whether {:.4f}{}K is equal to {:.4f}{}C; After testing, {:.4f}{}K is in fact {:.4f}{}C; This conversion has passed the test.".format(self.knownValues[i][2], deg, celsius, deg, self.knownValues[i][2], deg, conversion, deg))

        
    def testConvertKelvinToFahrenheit(self):
        print ("\n\n\nNow testing the conversion from Kelvin to Fahrenheit using the function convertKelvinToFahrenheit() from conversions.py:\n")
        for i in range(0, len(self.knownValues)):
            conversion = conversions.convertKelvinToFahrenheit(self.knownValues[i][2])
            fahrenheit = self.knownValues[i][1]
            self.assertEqual(fahrenheit, conversion)
            print ("     Now testing whether {:.4f}{}K is equal to {:.4f}{}F; After testing, {:.4f}{}K is in fact {:.4f}{}F; This conversion has passed the test.".format(self.knownValues[i][2], deg, fahrenheit, deg, self.knownValues[i][2], deg, conversion, deg))


if __name__ == "__main__":
    unittest.main()
