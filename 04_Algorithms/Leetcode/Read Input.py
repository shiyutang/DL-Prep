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


a = get_word()
d, s, swws, dws, f = get_number(), get_number(), get_number(), get_number(), get_number()
ad, ss, dss, wdws, qf = get_number(), get_word(), get_word(), get_number(), get_number()

print(a)
print(d, s, swws, dws, f)
print(ad, ss, dss, wdws, qf)
