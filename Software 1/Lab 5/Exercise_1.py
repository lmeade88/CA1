# Exercise 1

# request input and place in variable called radius
radius = float(input("Please enter the radius of the circle: "))

# output error message if radius is less then or equal to zero:
if radius <= 0:
    print("Radius must be greater than 0.")
else:
    # display the area of this circle using the formula and round to 2 decimal places for clarity
    area = round(22/7 * radius ** 2, 2)
    print(f"{area} is the area of the circle.")

    # display the sphere volume using the formula and round to 2 decimal places for clarity
    sphere_volume = round(4/3 * 22/7 * radius ** 3, 2)
    print(f"{sphere_volume} is the volume of the sphere.")


# TEST
# input 5, expected output "78.57 is the area of the circle." and "523.81 is the volume of the sphere."