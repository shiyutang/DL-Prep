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


A,S,K,X,Y = get_number(),get_number(),get_number(),get_number(),get_number()

res = (S-A+K*Y)//(X+Y)
if A +res*X == S+ (K-res)*Y:
    print(res)
else:
    print(-1)