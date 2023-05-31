"""Write a program that converts currency , specifically euros to U.S dollars. Prompt for the amount of money in euros,
and prompt for current exchange rate of the euro. Prnt out the new amount in US dollar."""

amount_from = int(input("How many euros are you exchanging? "))
rate_from = float(input("What is the exchange rate from euros to U.S. dollars? "))
rate_to = float(input("What is the exchange rate from U.S. dollars? "))
amount_to = "{:.2f}".format(float((amount_from * rate_from) / rate_to))
print(f"{amount_from} euros at an exchange rate of {rate_from} is {amount_to} U.S. dollars.")