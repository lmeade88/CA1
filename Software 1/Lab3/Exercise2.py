# Write a program that reads a value representing a number of seconds. Print the equivalent amount of time in hours, minutes, and seconds.
import math

print("Please enter seconds:")
seconds = int(input())
total = 0 + seconds

hours = math.floor(seconds / 3600)
if hours > 0: 
    total -= hours*3600


minutes = math.floor(total / 60)
if minutes > 0: 
    total -= (minutes*60)


secondsLeft = total

print(f"The total time is {hours} hours, {minutes} minutes and {secondsLeft} seconds.")