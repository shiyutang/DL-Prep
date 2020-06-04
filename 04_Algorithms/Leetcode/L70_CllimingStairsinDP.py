# 1-d dynamic programming
# find number of ways to sum up to a number using given element
#

# assume key1<key2<key3 and keyi != m*keyj(i!=j) and keys alrealdy known
def WaysToSumUp(number,key1,key2):
    basicSol = [[0] for i in range(key2+1)]
    basicSol[key1] = 1
    basicSol[key2] = 2
    basicSol[0] = 1
    if number<0:
        return 0
    elif number ==0 or number == key1 or number == key2:
        return basicSol[number]
    else:
        return WaysToSumUp(number-key1,key1,key2)+ \
               WaysToSumUp(number-key2,key1,key2)

def test():
    key1,key2 = 1,2
    res = WaysToSumUp(10,key1,key2)
    print(res)


test()




