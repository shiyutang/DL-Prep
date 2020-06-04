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

N,M,S = get_number(),get_number(),get_number()
# N,M,S = 4,1,2

travelCost = (N-1)*M
start,end,cnt = 2,N,0
# Binary search 
while start<=end:
    mid = (start+end)//2
    start = mid+1
    cnt += 1
    print('start,end,mid',start,end,mid)
print('cnt',cnt)
res = cnt*S

print(res+travelCost)