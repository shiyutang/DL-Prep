# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


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


r, c = get_number(), get_number()
matrix = [[0 for j in range(c)] for i in range(r + 1)]
for i in range(r):
    for j in range(c):
        matrix[i][j] = get_number()
# print('1 matrix',matrix)


bloodMat = [[0 for j in range(c)] for i in range(r)]
matrix[r][:] = [10 ** 6 for j in range(c)]
matrix[r - 1][c - 1] = 1

# print('2 matrix',matrix)


for i in range(r - 1, -1, -1):
    for j in range(c - 1, -1, -1):
        # print('i,j',i,j)
        if i == r - 1 and j == c - 1:
            continue
        if j + 1 <= c - 1:
            matrix[i][j] = max(min(matrix[i + 1][j], matrix[i][j + 1]) - matrix[i][j], 1)
        else:
            matrix[i][j] = max(matrix[i + 1][j] - matrix[i][j], 1)
        # print('3 matrix',matrix)

print(matrix[0][0])
