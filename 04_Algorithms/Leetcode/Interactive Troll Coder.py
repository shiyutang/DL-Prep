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


queryNum = get_number()
queryBit = [0 for _ in range(queryNum)]
res = None
for i in range(-1,queryNum):
    if i != -1:
        queryBit[i] = 1-queryBit[i]

    query ='Q ' 
    for bit in queryBit:
        query = query + '{} '.format(bit)
    print(query)
    recieveRes = get_number()
    # print('res,recieveRes',res,recieveRes)
    if not res:
        res = recieveRes
    elif recieveRes<res:
        # print('shouldn''t change bit' )
        queryBit[i] = 1-queryBit[i]
    else:
        res = recieveRes
        # print('should change bit' )


finalRes = 'A '
for bit in queryBit:
    finalRes += '{} '.format(bit)
print(finalRes)