# Write a program to evenly divide  pizza, prompt for number of people, pizzas, and slices per pizza

People = int(input("How many people are there? "))
Pizza = int(input("How many pizzas are there? "))
Slices_per_Pizza = int(input("How many slices are there in a pizza? "))
Pizza_pieces_per_person = int((Pizza * Slices_per_Pizza) / People)
leftovers = int(Pizza_pieces_per_person * Pizza / People)
print(f"{People} people with {Pizza} pizzas ")
print(f"Each person gets {Pizza_pieces_per_person} pieces of pizza.")
print(f"There are {leftovers} leftover pieces.")
