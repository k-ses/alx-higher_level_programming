#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = str(number)[-1]
lastDigit = int(lastDigit)
if lastDigit > 5:
    print(f"last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"last digit of {number} is {lastDigit} and is 0")
elif lastDigit != 0 < 6:
    print(f"last digit of {number} is {lastDigit} and is less than 6 and not 0")
