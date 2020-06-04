import math
import random

def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

num1 = get_number()
num2 = get_number()
# num1,num2 = 4,3

if num2 == 0 or num1 == 0:
    res = 0
elif num1>2*num2 or num2>2*num1:
    res = min(num1,num2)
else:
    maxval = math.floor((num1+num2)//3)
    minVal = math.ceil(max(num2,num1)//2)
    res = random.randint(minVal,maxval)
print(res)