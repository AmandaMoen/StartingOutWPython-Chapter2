# Programming Exercise 2.3 Land Calculation
# April 12th, 2010
# CS110
# Amanda L. Moen
# 3. Land Calculation
# One acre of land is equivalent to 43,560 square feet.
# Write a program that asks the user to enter the total square feet in a tract
# of land and calculates the number of acres in the tract.
# Hint: divide the amount entered by 43,560 to get the number of acres.

# Get the number of square feet in a tract of land.
sq_feet = input('How many square feet are in this tract of land? ')

# Calculate the land size in acres.
land_size = sq_feet / 43560.0

# Display the result.
print "That's equal to %.2f" % land_size, "acres."
