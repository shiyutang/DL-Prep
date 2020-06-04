import random

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

tescNum = get_number()
for i in range(tescNum):
    Bigger0 = False

    string = input().split()
    stringList = list(string[0])
    # print('stringList',stringList)
    if stringList[0] == stringList[-1]:
        i = 1
        while stringList[i] == stringList[-1]:
            i+=1
        stringList = stringList[i:]+stringList[0:i]
    # print(stringList)
    letterDict = {}
    for i,letter in enumerate(stringList):
        if not letter in letterDict:
            letterDict[letter] = i
        elif i-letterDict[letter]==1 :
            letterDict[letter] = i
        else:
            Bigger0 = True
            break
        # print('letter,letterSet',letter,letterDict)

    if not Bigger0:
        print(0)
    else:
        minval = 1
        maxVal = len(stringList)//2
        # print(minval,maxVal)
        print(random.randint(minval,maxVal))