# Request input from the user and assign this to variable called new_password
new_password = input("Please enter a new password:  ")

# Request input from the user and assign this to variable called confirm_password
confirm_password = input("Please confirm new password:  ")

# notify if passwords match or not
if new_password == confirm_password:
    print("New password is successful.")
else:
    print("Passwords do not match, please try again.")


# TEST
# input "Hello" and "Hello", output "New password is successful."
# input "Hello" and "Goodbye", output "Passwords do not match, please try again."


https://colab.research.google.com/drive/1eDzYkuMIYglFR1--XvO-NjVXEMEPyZew?usp=sharing