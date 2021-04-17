import math

number_one = int(input())

number_two = int(input())

if number_two <= 1:
    print(round(math.log(number_one), 2))
else:
    print(round(math.log(number_one, number_two), 2))
