#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("%d is positive" %(number))
elif number == 0:
    print("%d is 0" %(number))
else:
    print("%d is negative" %(number))
