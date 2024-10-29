print("please enter Temperature in F:")
temp = float(input())

tempInCel = round((5/9) * (temp-32), 2)

print(f"Temp in Celsius is {tempInCel}")