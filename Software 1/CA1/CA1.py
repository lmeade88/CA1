# Liam Meade X00229895
# Link to colab: https://colab.research.google.com/drive/1_ql396B959P-YJYmFgxFGpR2o7QqiJY8?usp=sharing

# Basic salary is €12345.43 and basic salary for manager is €36589.65.

# Algorithm
# 1. Request input and create variables for name, ID, position and hours worked.
# 2. From this info. create another variable called salary, calculating based on hours worked and %.
# 3. Conditional: If manager, add an extra 10% to salary.
# 4. Display results in a clear manner.


# Initial basic salary
basic_salary = 12345.43
basic_manager = 36589.65

# Request input and store info in variables
name = input("Please enter employee name: ")
ID = input("Please enter employee ID: ")
# for position, disregard capital letters
position = input("Please enter employee position: ").lower()
hours = int(input("Please enter hours worked: "))

# Calculate salary based on % rubric, using conditional statement
# Include 10% extra if manager
if position.lower() != "manager":
    if hours < 10:
        salary = round(basic_salary * 9/10, 2)
    elif hours < 31:
        salary = round(basic_salary, 2)
    elif hours < 36:
        salary = round(basic_salary * 105/100, 2)
    elif hours < 46:
        salary = round(basic_salary * 110/100, 2)
    else:
        salary = round(basic_salary * 120/100, 2)
else:
    if hours < 10:
        salary = round(basic_manager * 9/10, 2)
    elif hours < 31:
        salary = round(basic_manager, 2)
    elif hours < 36:
        salary = round(basic_manager * 105/100, 2)
    elif hours < 46:
        salary = round(basic_manager * 110/100, 2)
    # 10% added
    else:
        salary = round(basic_manager * 120/100 * 110/100, 2)

# Print salary
print("----------Employee Details----------")
print(f"Employee Name: {name}")
print(f"Employee ID: {ID}")
print(f"Position: {position}")
if position.lower() != "manager":
    print(f"Salary: €{basic_salary}")
else:
    print(f"Salary: €{basic_manager}")
print(f"Hours worked: {hours}")
print(f"Total Salary: €{salary}")
