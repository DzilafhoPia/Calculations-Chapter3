"""Create a program that computes simple interest. Prompt for the principal amount, rate as percentage and time. display
the amount accrued"""

P = float(input("Enter the principal: "))
Rate = float(input("Enter the rate: "))
R = float(Rate/100)
Y = int(input("Enter the number of years: "))
A = int(P * (int(1) + (R * Y)))
print(f"After {Y} years at {Rate}%, the investment will be worth ${A}.")