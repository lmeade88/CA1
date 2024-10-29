# Request input from the user and assign this to variable called engine_size
engine_size = int(input("Please enter the engine size:  "))

# if engine_size is <= 1000, display price
if engine_size <= 1000:
    print("Price is €150.")

# else if for rest of the engine sizes...
elif engine_size > 1000 and engine_size < 1200:
    print("Price is €175.")
elif engine_size > 1200 and engine_size < 1400:
    print("Price is €200.")
elif engine_size > 1400 and engine_size < 1600:
    print("Price is €250.")
elif engine_size > 1600 and engine_size < 1800:
    print("Price is €300.")
elif engine_size > 1800 and engine_size < 2000:
    print("Price is €350.")
else:
    print("Price is €500.")


# TESTS
# input 1650, output "Price is €300."

https://colab.research.google.com/drive/1eDzYkuMIYglFR1--XvO-NjVXEMEPyZew?usp=sharing