import math

def grayCode(n: int):
    for bit in range(0, 1 << n):
        yield str(bin(bit ^ (bit >> 1))[2:]).zfill(n)

def commonDigit(d1, d2):
    tmp = d1 ^ d2
    cnt = 0
    while tmp:
        if tmp % 2 == 1:
            cnt += 1
        tmp = tmp >> 1
    return cnt


ncase = int(input().strip())
betsWinning, betDis = {}, {}
for i in range(ncase):
    bet = input().strip()
    betsWinning[bet] = 0
    betDis[bet] = [int(bet, base=2), None]
betlen = len(bet)

for idx, ele in enumerate(grayCode(betlen)):
    intele = int(ele, base=2)
    maxcnt, maxbet = -1, None
    found = True
    if idx == 0:
        for key in betDis:
            cnt = betlen - commonDigit(intele, betDis[key][0])
            betDis[key][1] = cnt
            if cnt > maxcnt:
                maxcnt, maxbet = cnt, key
                found = True
            elif cnt == maxcnt:
                found = False
    else:
        diffbit = int(betlen - math.log2(intele ^ previous) - 1)
        for key in betDis:
            cnt = betDis[key][1] + 1 if ele[diffbit] == key[diffbit] else betDis[key][1] - 1
            betDis[key][1] = cnt
            if cnt > maxcnt:
                maxcnt, maxbet = cnt, key
                found = True
            elif cnt == maxcnt:
                found = False

    previous = intele
    if found:
        betsWinning[maxbet] += 1
    # print(ele, betsWinning, betDis)

minres = None
for key in betsWinning:
    if not minres:
        minres = betsWinning[key]
    else:
        if betsWinning[key] < minres:
            minres = betsWinning[key]

print(minres)
