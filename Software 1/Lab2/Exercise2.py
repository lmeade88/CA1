print("Please enter yard width and length:")
yWidth = float(input())
yLength = float(input())

print("Please enter house width and length:")
hWidth = float(input())
hLength = float(input())

grassArea = (yWidth*yLength) - (hWidth*hLength)
timeToCut = grassArea / 2
timeToCutMinutes = round(timeToCut / 60, 2)
print(f"The time to cut the grass will be {timeToCutMinutes} minutes")