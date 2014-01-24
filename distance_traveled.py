# Programming Exercise 2.5 Distance Traveled
# April 16th, 2010
# CS110
# Amanda L. Moen
# 5. Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels
# down the interstate can be calculated with the following formula:
#   Distance = Speed x Time
# A car is traveling at 60 miles per hour.
# Write a program that displays the following:
#   The distance the car will travel in 5 hours
#   The distance the car will travel in 8 hours
#   The distance the car will travel in 12 hours

# Assign a value to the speed variable.
speed = 60

# Assign a value to the time variable.
time1 = 5
time2 = 8
time3 = 12

# Get the distance traveled.
distance1 = speed * time1
distance2 = speed * time2
distance3 = speed * time3

print "Traveling at 60 miles per hour..."
print "after 5 hours you will have traveled ", distance1, "miles."
print "after 8 hours you will have traveled ", distance2, "miles."
print "after 12 hours you will have traveled ", distance3, "miles."
