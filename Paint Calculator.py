"""Calculate gallons of paint needed to paint the ceiling of a room. Prompt for length and width, and assume that
one gallon covers 350 square feet. Display the number of gallons needed to paint the ceiling as a whole number"""
import math

length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))
# 1 gallon covers 350 square feet
area = length * width
area_per_gallon = float(1/350)
gallon = area * area_per_gallon
number_of_gallons = math.ceil(gallon)
print(f"You will need to purchase {number_of_gallons} gallon of paint to cover {area} square feet.")
