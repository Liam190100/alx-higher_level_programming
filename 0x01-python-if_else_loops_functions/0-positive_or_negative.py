#!/usr/bin/python3
import random
num = random.randint(-10, 10)
print(num, end=" ")
if num > 0:
    print("is positive")
elif num == 0:
    print("is zero")
else:
    print("is negative")
