def f(length):
    base = [0,0,0,0,0,1,1,2,2,2]
    if length<len(base):
        return base[length]
    else:
        return f(int(length/2))+f(length-int(length/2))

def relation(length):
    result = 0
    for k in range(3,length+1):
        result += length-k+1 + f(k)
    while length/2>3:
        for k in range(3,int(length/2)+1):
            result += int(length/2)-k +length-int(length/2)-k
        length = length/2
    print(result)

for i in range(3,11):
    relation(i)
