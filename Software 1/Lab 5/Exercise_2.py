# Exercise 2

# request input and place in variable called weekly_hours
weekly_hours = float(input("Please enter your weekly hours worked: "))

# output error message if radius is less then or equal to zero:
if weekly_hours <= 0:
    print("Hours worked must be greater than zero.")
else:
    # create a variables for pay, overtime pay, tax, gross pay and net pay
    pay = 0.00
    overtime = 0.00
    tax = 0.00
    gross = 0.00
    net_pay = 0.00
    if weekly_hours <= 39:
        pay += round(weekly_hours * 35 * 52, 2)
        tax += round((pay - 18000) * 21/100, 2)
        net_pay += pay - tax
        print("-----------------------")
        print(f"Hours worked: {weekly_hours}")
        print(f"Standard pay amount: €{pay}")
        print("Overtime pay amount: €0.00")
        print(f"Gross pay: €{pay}")
        print("-----------------------")
        print(f"Total tax: €{tax}")
        print("-----------------------")
        print(f"Net pay: €{net_pay}")
    else:
        pay += round(39 * 35 * 52, 2)
        overtime += round((weekly_hours - 39) * 50 * 52, 2)
        gross += pay + overtime
        tax += round((gross - 18000) * 21/100, 2)
        net_pay += gross - tax
        print("-----------------------")
        print(f"Hours worked: {weekly_hours}")
        print(f"Standard pay amount: €{pay}")
        print(f"Overtime pay amount: €{overtime}")
        print(f"Gross pay: €{gross}")
        print("-----------------------")
        print(f"Total tax: €{tax}")
        print("-----------------------")
        print(f"Net pay: €{net_pay}")


# TEST
# Input 40, expected output: "Net pay: €61908.20"
    

    
