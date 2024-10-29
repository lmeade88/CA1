# Request input from the user and assign this to variable called item_cost
item_cost = float(input("Please enter the cost of the item:  €"))

# if item_cost is more than €5000, display a message
if item_cost > 5000:
    print("The purchaser must go to tender.")

# if item_cost is between €500 and €5000 inclusive, display a message
elif item_cost >= 500 and item_cost <= 5000:
    print("The purchaser must get quotes from three different suppliers.")

# else if item_cost is less than €500, display a message
else:
    print("The purchaser can order the item.")


# TESTS
# input 5000.50, expected result "The purchaser must go to tender."
# input 4999, expected result "The purchaser must get quotes from three different suppliers."
# input 200, expected result "The purchaser can order the item."


https://colab.research.google.com/drive/1eDzYkuMIYglFR1--XvO-NjVXEMEPyZew?usp=sharing


