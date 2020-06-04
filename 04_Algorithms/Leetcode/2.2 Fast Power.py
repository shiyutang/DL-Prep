import time


def fast_pow(under, exp):
    if under == 0:
        return 0
    else:
        if exp == 1:
            return under
        elif exp == 0:
            return 1
        elif exp % 2 == 1:
            res = under * fast_pow(under, (exp - 1) / 2) ** 2
        else:
            res = fast_pow(under, exp / 2) ** 2
        return res


def pow_iterative(under, exp):
    res = 1
    while exp:
        if exp % 2 == 1:  # while it's odd or at end
            res *= under
        under = under * under
        exp = int(exp / 2)
    return res


# test
a = range(1, 3, 1000000000)
n = range(0, 1000000, 3)


def test(method):
    t1 = time.time()
    result = []
    for ai in a:
        for ni in n:
            if "fast" in method:
                result.append(fast_pow(ai, ni))
            elif "normal" in method:
                result.append(ai ** ni)
            else:
                result.append(pow_iterative(ai, ni))
    t2 = time.time()

    return result, t2 - t1


result1, time1 = test("normal")
result2, time2 = test("fast")
result3, time3 = test("iter")

if not result1 == result3:
    print("result1 is {} \nresult2 is {}".format(result1, result3))
else:
    print("normal power needs {} secs; fast version only needs {} secs".format(time1, time3))
