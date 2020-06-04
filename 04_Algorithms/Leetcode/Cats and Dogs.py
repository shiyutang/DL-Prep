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



catN,dogM = get_number(),get_number()
cat,dog = [],[]
for i in range(catN):
    cat.append([get_number(),get_number()])
for j in range(dogM):
    dog.append([get_number(),get_number()])


dogCnt = [0 for i in range(catN)]
for adog in dog:
    minDis,minIdx = 4*(10**5),100
    for i,acat in enumerate(cat):
        if (acat[0]-adog[0])**2 + (acat[1]-adog[1])**2 <minDis:
            minIdx = i
            minDis = (acat[0]-adog[0])**2 + ((acat[1]-adog[1])**2)
        elif (acat[0]-adog[0])**2 + (acat[1]-adog[1])**2 == minDis:
            # print('equal distance')
            if acat[0]+acat[1] < cat[i][0]+cat[i][1]:
                minIdx = i
    # print(adog,minIdx)
    dogCnt[minIdx] += 1

# print('dogCnt',dogCnt)

res = 0
for item in dogCnt:
    if item == 1:
        res += 1

print(res)

