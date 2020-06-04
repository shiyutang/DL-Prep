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


# Len = 10 #get_number()
# res = ''.join(['yY' for _ in range(Len//2)])

# if Len %2 == 1:
#     res+='y'

# print(res)


import random
Len =  get_number()
res = ''
for i in range(Len):
    idx = random.randint(0,1)
    res += ['Y','y'][idx == 1]

print(res)