print("Please enter hours:")
hours = int(input())

print("Please enter minutes:")
minutes = int(input())

print("Please enter seconds:")
seconds = int(input())

# Convert to seconds
totalInSeconds = (hours*3600) + (minutes*60) + seconds
print(f"The total time in seconds is {totalInSeconds} seconds.")

