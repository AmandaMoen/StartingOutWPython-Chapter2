# Programming Exercise 2.9 Celsius to Fahrenheit Temperature Converter
# April 16th, 2010
# CS110
# Amanda L. Moen
# 9. Celsius to Fahrenheit Temperature Converter
# Write a program that converts Celsius to Fahrenheit temperatures.
# The formula is as follows:
#   F = 9/5 C + 32
# The program should ask the user to enter a temperature in Celsius,
# and then display the temperature converted to Fahrenheit.

# F = 1.8 * C + 32

# Get the temperature in Celsius
celsius = input('Enter the temperature in Celsius: ')

# Convert the temperature from Celsius to Fahrenheit
fahrenheit = 1.8 * celsius + 32.0

# Display the result
print 'The temperature', celsius, 'degrees celsius converts to', fahrenheit, 'degrees fahrenheit.'
