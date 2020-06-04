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

def commonDigit(d1,d2):
    tmp = d1^d2
    cnt = 0
    while tmp:
        if tmp%2 ==1:
            cnt+=1
        tmp = tmp>>1
    return cnt


ncase = get_number()
betsWinning = {}
for i in range(ncase):
    bet =input().split()[0]
    NumCoins = len(list(bet))
    bet = int(bet,2)
    betsWinning[bet] = 0

maxVal = 2**NumCoins

for i in range(0,maxVal):
    # print(i,betsWinning)
    if i in betsWinning:
        betsWinning[i] += 1
        continue
    else:
        res = []
        maxCommon = 0
        for bet in betsWinning:
            common  = commonDigit(bet,i)
            if common>=maxCommon:
                res.append([common,bet])
                maxCommon = common
        if len(res) == 1 or res[-1][0]!=res[-2][0]:
            betsWinning[res[-1][1]] += 1
# print('bets', betsWinning)
minres = -1
for key in betsWinning:
    if betsWinning[key]>minres:
        minres = betsWinning[key]


print(minres)
