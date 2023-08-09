#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Print the randomly generated number
print("The number", number, end=" ")

# Check if the number is positive, zero, or negative
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

