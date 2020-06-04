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

# 将点分为内外的点：
# 内部的点： 两两配对都可以获得正确的结果
# 外部的点：检查两两之间是否交叉，如果和polygon上直线交叉，结果-1



a = get_number()
b = get_number()

res = a + b
print(res)