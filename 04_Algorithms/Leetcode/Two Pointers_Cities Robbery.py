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

# N,X,K = 4, 0, 3
# pos = [-4,-1,1,4]
# val = [10,1,1,10]

# N,X,K = 4, 0, 4
# pos = [-4,-1,1,4]
# val = [10,1,1,10]

# N,X,K = 4, 3,7
# pos = [0,4,5,7]
# val = [9,1,5,8]

def EnoughGas(point1,point2,xpos,K,pos):
    # print(point1,point2,xpos,K,pos)
    if xpos-pos[point1]>=0 and pos[point2] - xpos>=0:
        distance = [xpos-pos[point1],pos[point2]-xpos][pos[point2]-xpos<xpos-pos[point1]] \
                    + pos[point2]-pos[point1]
        # print('distance',distance)

    return distance<=K

def findIdxBS(pos,target,start,end): # the target must exist
    if start == end:
        return start
    elif end-start == 1:
        if pos[end] == target:
            return end
        else:
            return start
    else:
        median = (start+end)//2
        if pos[median]>target:
            findIdxBS(pos,target,start,median-1)
        elif pos[median]==target:
            return median
        else:
            findIdxBS(pos,target,median+1,end)


N,X,K = get_number(),get_number(),get_number()
pos,val = [],[]
for i in range(N):
    position,value = get_number(),get_number()
    pos.append(position)
    val.append(value)

if X + K < pos[0] or X-K >position:
    print(0)

elif X < pos[0]:
    resulttmp,start,end,target = 0,0,len(pos),X+K
    idx = findIdxBS(pos,target,start,end)
    for i in range(idx+1):
        restmp+=val[i]
    print(resulttmp)

elif X>position:
    resulttmp,start,end,target = 0,0,len(pos),X-K
    idx = findIdxBS(pos,target,start,end)
    for i in range(idx,end,1):
        resulttmp+=val[i]
    print(resulttmp)

else:
    xpos = -1
    while pos[xpos+1]<X :
        xpos += 1
        if xpos == len(pos)-1:
            break
    pos.insert(xpos+1,X)
    val.insert(xpos+1,0)

    point1,point2 = xpos,len(pos)-1
    maxResult,restmp = 0,0
    for point1 in range(xpos,-1,-1):
        if point2>=xpos:
            while point2 > xpos and not EnoughGas(point1,point2,X,K,pos):
                point2-=1

            if restmp ==  0:
                lastp2,lastp1 = point2,point1
                for index in range(point1,point2+1):
                    restmp += val[index]
            else:
                restmp += val[point1]
                while lastp2 > point2:
                    restmp -= val[lastp2]
                    lastp2 -= 1
            if point2 > xpos and EnoughGas(point1,point2,X,K,pos):
                # print('point1,point2,restmp',point1,point2,restmp)
                maxResult = [maxResult,restmp][restmp>maxResult]
        else:
            break
    print(maxResult)