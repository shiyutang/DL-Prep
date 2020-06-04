import math
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


N,A,B = get_number(),get_number(),get_number()
# N,A,B = 4,2,3
# N,A,B = 59,8,10
# N,A,B = 10,6,9


shortestLen = math.ceil(N/B) 

SEQ = []
if N<A or N<shortestLen*A:
    res = 'NO'
else:
    res = 'YES'
    start,end = 0,shortestLen
    while end>=start:
        mid = (start+end)//2
        # print('shortestLen,start,end,mid,A,B',shortestLen, start,end,mid,A,B)
        # print('A*(mid+1)+B*(shortestLen-mid-1),A*mid + B*(shortestLen-mid),N',
            # A*(mid+1)+B*(shortestLen-mid-1),A*mid + B*(shortestLen-mid),N)
        if A*(mid+1)+B*(shortestLen-mid-1) == N:
            # print('1')
            SEQ = [A for _ in range(mid+1)] + [B for tt in range(shortestLen-mid-1)]
            break

        elif A*(mid+1)+B*(shortestLen-mid-1) <= N:

            if A*mid + B*(shortestLen-mid) >= N:
                # print('2')

                C = N-(A*(mid+1)+B*(shortestLen-mid-1))+A
                SEQ = [A for _ in range(mid)] +[C] +[B for tt in range(shortestLen-mid-1)]
                break

            elif A*mid+ B*(shortestLen-mid) == N:
                # print('3')

                SEQ = [A for _ in range(mid)] + [B for tt in range(shortestLen-mid)]
                break
            
            else:
                # print('4')

                end = mid-1
        else:
            start = mid+1

if res == 'NO':
    print(res)
else:
    print(res)
    for i,item in enumerate(SEQ):
        if i == len(SEQ)-1:
            print(item)
        else:
            print(item,end = ' ')
