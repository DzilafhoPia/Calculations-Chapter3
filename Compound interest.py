"""Write a program to compute the value of an investment compounded over time. The program should ask for the principal,
number of years  to invest, interest rate, and the number of periods per year to compound."""

P = float(input("what is the principal amount? "))
Rate = float(input("What is the rate? "))
t = int(input("What is the number of years? "))
n = int(input("What is the number of times the interest is compounded per year? "))
R = float(Rate/100)
A = "{:.2f}".format(float(P*(int(1) + R/n) ** (n * t)))
print(f"${P} invested at {Rate}% for {t} years compounded {n} times per year is ${A}.")
