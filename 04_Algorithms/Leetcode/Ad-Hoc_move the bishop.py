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


R1,C1,R2,C2 = get_number(),get_number(),get_number(),get_number()
rowDiff = abs(R2-R1)
if C2 == C1 and rowDiff == 0:
    res = 0
else:
    C1tmp = [C1-rowDiff,C1+rowDiff][C2>C1]
    if C2 == C1tmp: 
        res =  1
    elif (C2-C1tmp)% 2 == 0:
        res =  2
    else:
        res = -1

print(res)