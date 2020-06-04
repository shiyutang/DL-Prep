# a simple parser for python. use get_number() and get_word() to read
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

# numpy and scipy are available for use
import numpy
import scipy

n,m = get_number(),get_number()
matrix = [[0 for j in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(n):
        matrix[i][j] == get_number()%3

print(matrix)
for i in range(m)

res = a + b
print(res)