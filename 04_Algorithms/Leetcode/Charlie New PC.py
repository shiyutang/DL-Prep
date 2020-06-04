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


numTest = get_number()
for i in range(numTest):
    maxBudget,numComtype = get_number(),get_number()
    numEachType = [get_number() for _ in range(numComtype)]
    print('maxBudget,numComtype,numEachType', maxBudget,numComtype,numEachType)
   
    cost,maxPerType,minPerType = [None for _ in range(numComtype)],[],[]
    for i in range(numComtype):
        # cost[i] = sorted(list(set([get_number() for tt in range(numEachType[i])])))
        cost[i] = [get_number() for tt in range(numEachType[i])]
        # print('cost[i]',i,cost[i])
        maxPerType.append(max(cost[i]))
        minPerType.append(min(cost[i]))

    print('maxPerType,minPerType', maxPerType,minPerType)
    maxSuffix,minSuffix = [maxPerType[-1]],[minPerType[-1]]
    for i in range(numComtype-2,-1,-1):
        maxval,minval = maxSuffix[0]+maxPerType[i],minSuffix[0]+minPerType[i]
        maxSuffix.insert(0,maxval)
        minSuffix.insert(0,minval)
        print('minSuffix,maxSuffix',minSuffix,maxSuffix)

    res,result = [cost[0]],-1
    if minSuffix[0]>maxBudget:
        result = 0
    elif maxSuffix[0] <maxBudget:
        result = maxSuffix[0]

    if result == -1:
        for i in range(1,numComtype):
            restmp = []
            if result == maxBudget:
                break
            for prevres in res[-1]: # i-1 层           
                if result == maxBudget:
                    break
                    
                if prevres + maxSuffix[i] <maxBudget:
                    result = max(result,prevres+maxSuffix[i]) 
                elif prevres + minSuffix[i] >maxBudget:
                    continue
                elif prevres + minSuffix[i] == maxBudget or \
                    prevres + maxSuffix[i] == maxBudget:
                    result = maxBudget
                    break
                else:
                    for j in range(len(cost[i])):
                        val = prevres+cost[i][j]
                        if val<=maxBudget:
                            restmp.append(val)
                        elif val == maxBudget:
                            result = maxBudget
                            break
            print('restmp',restmp)
            res = [restmp]

        if res[-1]!= []:
            resultfinal = max(res[-1])
            resultfinal = max(resultfinal,result)
        else:
            resultfinal = result
        print(resultfinal)
    else:
        print(result)



# 1
# 100
# 10
# 11 12 3 4 6 6 6 6 6 7
# 19 29 1 3 2 2 3 1 31 3 20
# 2 3 14 1 3 2 2 3 1 31 3 20
# 21 32 23
# 4 24 2 1 
# 2 9 33 13 23 1 
# 12 29 3 13 23 1 
# 2 3 14 13 23 1 
# 2 9 13 13 23 1 
# 2 19 3 13 23 1 
# 12 9 3 13 23 1 8