#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print("last digit of %d is greater than 5" %(number))
elif number % 10 == 0:
    print("last digit of %d is 0" %(number))
elif number % 10 < 6 != 0:
    print("last digit of %d is less than 6 and not 0" %(number))
