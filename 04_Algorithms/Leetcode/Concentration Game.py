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

numKind = get_number()
finished = False
cardIdxDict = {}
matched,pairIdx = 0,1
while not finished:
    print('{} {}'.format(pairIdx,pairIdx+1))
    res = input().split()

    if len(res) == 1:
        if res[0] == '-1':
            finished = True
        else:
            matched += 1
    else:
        if not res[0] in cardIdxDict:
            cardIdxDict[res[0]] = [pairIdx]
        else:
            cardIdxDict[res[0]].append(pairIdx)
        if not res[1] in cardIdxDict:
            cardIdxDict[res[1]] = [pairIdx+1]
        else:
            cardIdxDict[res[1]].append(pairIdx+1)
    pairIdx += 2
    if pairIdx > 2*numKind or matched == numKind:
        finished = True
for key in cardIdxDict:
    print('{} {}'.format(cardIdxDict[key][0],cardIdxDict[key][1]))
    res = input().split()
print('-1')