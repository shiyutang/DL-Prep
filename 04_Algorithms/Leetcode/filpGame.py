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

def MoreZero(listItem):
    cnt = 0
    for item in listItem:
        if item == 0:
            cnt += 1
    return cnt>len(listItem)-cnt


N,M = get_number(),get_number()
matrix = [[0 for j in range(M)] for i in range(N)]
filp = [False for _ in range(N)] 
for i in range(N):
    for j in range(M):
        matrix[i][j] = get_number()
        if j == 0 and matrix[i][j] == 0:
            # print('i,j,matrix[i][j]',i,j,matrix[i][j])
            filp[i] = True
# print('matrix',matrix,filp)

for i,item in enumerate(filp):
    if item:
        for j in range(M):
            matrix[i][j] = 1 - matrix[i][j]

# print('matrix after flip1',matrix)


for j in range(1,M):
    if MoreZero([matrix[i][j] for i in range(N)]):
        for i in range(N):
            matrix[i][j] = 1 - matrix[i][j]
# print('matrix after flip2',matrix)


res = (2**(M-1))*N
# print('res', res)
for j in range(1,M):
    for i in range(N):
        if matrix[i][j] == 1:
            res += 2**(M-j-1)
            # print('i,j,2**(j-1)', i,j,2**(j-1))

print(res)