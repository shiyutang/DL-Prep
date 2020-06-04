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

numTest = get_number()
for i in range(numTest):
    numAlphabet,queIdx = get_number(),get_number()+1
    
    blocknum,res = 1,0
    while res<X:
        res += numAlphabet**blocknum
        blocknum += 1
    blocknum,res = blocknum - 1,res-numAlphabet**blocknum
    blockLen = numAlphabet**blocknum
    queIdx -= res
    inStringPos = queIdx%blocknum
    inBlockPos = queIdx//blocknum
     

    
b = get_number()


res = a + b
print(res)