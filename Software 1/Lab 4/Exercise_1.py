# Request input from the user and assigns this to variable called num
num = int(input("Please enter an integer greater than 0:  "))

# if input is zero, request a number greater than zero
if num == 0:
    print("Please enter a number greater than zero.")
# if number divided by 2 has no remainder, it is even, else it is odd.
else:
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")


# TESTS
# input 0, expected result "Please enter a number greater than zero."
# input 8, expected result "8 is an even number."
# input 13, expected result "13 is an odd number."

https://colab.research.google.com/drive/1eDzYkuMIYglFR1--XvO-NjVXEMEPyZew?usp=sharing