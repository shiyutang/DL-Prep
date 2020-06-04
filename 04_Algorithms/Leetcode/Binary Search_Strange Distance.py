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

# read input
N,K = get_number(),get_number()
point = []
for i in range(N):
    x,y = get_number(),get_number()
    point.append((x,y))
keepRecord = []
for i in range(len(point)-1):
    for j in range(i+1,len(point)):
        dis = min((abs(point[i][0]-point[j][0]),abs(point[i][1]-point[j][1])))
        keepRecord.append(dis)

keepRecord.sort()
print(keepRecord[K-1])