# Programming Exercise 2.7 Miles-per-Gallon
# April 16th, 2010
# CS110
# Amanda L. Moen
# 7. Miles-per-Gallon
# A car's miles-per-gallon (MPG) can be calculated with the following formula:
#   MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the
# gallons of gas used.  It should calculate the car's miles-per-gallon
# and display the result.

# Get the number of miles driven for the last tank of gas
miles = input('How many miles did you drive on the last tank of gas? ')

# Get the number of gallons of gas used to fill the tank
gallons = input('How many gallons did you use to fill the gas tank? ')

# Calculate the mpg using 'mpg=miles/gallons'
miles_per_gallon = float (miles) / float (gallons)

# Display the result
print 'You will have gotten ', miles_per_gallon, 'mpg on your last tank of gas.'
