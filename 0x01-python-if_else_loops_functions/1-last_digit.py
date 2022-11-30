#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = str(number)[-1]
if number < 0:
    ld = f"-{ld}"
if int(ld) > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif int(ld) == 0:
    print(f"Last digit of {number} is {ld} and is 0")
elif int(ld) < 6 and ld != 0:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
