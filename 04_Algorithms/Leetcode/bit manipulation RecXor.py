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


def calc(n):
    r = n % 4
    if r == 0: return n
    if r == 1: return 1
    if r == 2: return n + 1
    if r == 3: return 0


def calc_seg(l, r):
    return calc(l - 1) ^ calc(r)


N = get_number()
for i in range(N):
    l, h, t, d1, d2 = get_number(), get_number(), get_number(), get_number(), get_number()

    rst = calc_seg(t, l * h + t - 1)
    # print("rst", rst)
    d1 = d1 - t
    d2 = d2 - t
    ll = abs(d1 % l - d2 % l)
    hh = abs(d1 // l - d2 // l) + 1
    dstart = d1 // l * l + min(d1 % l, d2 % l) + t
    # print("ll, hh, dstart", ll, hh, dstart)
    for i in range(hh):
        rst = rst ^ calc_seg(dstart + i * l, dstart + i * l + ll)
        # print("dstart + i*l, dstart + i*l + ll", dstart + i*l, dstart + i*l + ll)
    print(rst)
