#!/usr/bin/env python
# -*- coding: utf-8 -*-


def convertCelsiusToKelvin(degrees):
    """
    This function converts a given temperature from Celsius to Kelvin.

    Args:
        degrees (float): The temperature in Celsius.

    Returns:
        The temperature value converted to Kelvin.

    Example:
        >>> convertCelsiusToKelvin(21)
        294.15
    """

    celsius = float(degrees)
    kelvin = celsius + 273.15
    return round(kelvin,4)


def convertCelsiusToFahrenheit(degrees):
    """
    This function converts a given temperature from Celsius to Fahrenheit.

    Args:
        degrees (float): The temperature in Celsius.

    Returns:

        The temperature value converted to Fahrenheit.

    Example:
        >>> convertCelsiusToFahrenheit(21)
        69.8
   """

    celsius = float(degrees)
    fahrenheit = ((celsius * 9) / 5) + 32
    return round(fahrenheit,4)


def convertFahrenheitToCelsius(degrees):
    """
    This function converts a given temperature from Fahrenheit to Celsius.

    Args:
        degrees (float): The temperature in Fahrenheit.

    Returns:

        The temperature value converted to Celsius.

    Example:
        >>> convertFahrenheitToCelsius(69.8)
        21.0
   """

    fahrenheit = float(degrees)
    celsius = (((fahrenheit - 32) * 5) / 9)
    return round(celsius,4)


def convertFahrenheitToKelvin(degrees):
    """
    This function converts a given temperature from Fahrenheit to Kelvin.

    Args:
        degrees (float): The temperature in Fahrenheit.

    Returns:

        The temperature value converted to Kelvin.

    Example:
        >>> convertFahrenheitToKelvin(69)
        293.7056
    """

    fahrenheit = float(degrees)
    kelvin = (((fahrenheit + 459.67) * 5) / 9)
    return round(kelvin,4)


def convertKelvinToCelsius(degrees):
    """
    This function converts a given temperature from Kelvin to Celsius.

    Args:
        degrees (float): The temperature in Kelvin.

    Returns:

        The temperature value converted to Celsius.

    Example:
        >>> convertKelvinToCelsius(294.15)
        21.0
    """

    kelvin = float(degrees)
    celsius = (kelvin - 273.15)
    return round(celsius,2)


def convertKelvinToFahrenheit(degrees):
    """
    This function converts a given temperature from Kelvin to Fahrenheit.

    Args:
        degrees (float): The temperature in Kelvin.

    Returns:

        The temperature value converted to Fahrenheit.

    Example:
        >>> convertKelvinToFahrenheit(293.7056)
        69.0
    """

    kelvin = float(degrees)
    fahrenheit = (((kelvin * 9) / 5) - 459.67)
    return round(fahrenheit,2)
