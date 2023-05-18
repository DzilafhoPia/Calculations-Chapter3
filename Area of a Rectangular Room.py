# Create a program that calculates the area of a room, display the area in both square feet and square meters.

print("What is the length of the room? ")
length = input()
print("What is the width of the room? ")
width = input()
print("You entered dimensions of " + length + " feet by " + width + " feet.")
print("The area is ")
area = int(length) * int(width)
print(str(area) + " square feet")
square_meters = area * round(float(0.09290304), 6)
print(str(square_meters) + " square meters")