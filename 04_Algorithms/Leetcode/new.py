# I have a few lucky numbers between 0 to 9. And given a large integer N, find the largest integer that only contains my lucky numbers, and not bigger than N.
#
# N can be very big, like an integer contains thousands of digits. 正数
#
# 3 5 7
# 777 -> 777
# 864 -> 777
# 764 -> 757
# 712 -> 577
# 大数
# 77712 -> 77577
# #
class task:
    def solve(self, N, luckynums):
        N = str(N)
        luckynums.sort()
        luckynums = list(map(str, luckynums))

        previssmall = False
        ret = ''
        for i, ele in enumerate(N):
            if not previssmall:
                index = len(luckynums) - 1
                while index >= 0 and int(luckynums[index]) > int(ele):
                    index -= 1
                if index == -1:  # there is no match in luckynum
                    if i == 0:
                        ret += '0'
                        if 0 < int(ele):
                            previssmall = True
                    else:
                        j = i - 1
                        while j >= 0 and ret[j] >= luckynums[0]:
                            if ret[j] == luckynums[0]:
                                if j == 0:
                                    ret = '0' + luckynums[-1]*i
                                    previssmall = True
                                    break
                                else:
                                    j -= 1
                                    continue
                            else:
                                k = len(luckynums) - 1
                                while k >= 0 and luckynums[k] >= ret[j]:
                                    k -= 1
                                if j == 0:
                                    ret = luckynums[k] + luckynums[-1] * (i)
                                else:
                                    ret = ret[:j] + luckynums[k]
                                    ret += luckynums[-1] * (i - len(ret) + 1)
                                previssmall = True
                                break
                            j -= 1

                        if j == -1:
                            print("there is no fit")
                            return
                else:
                    # match and there is match for next one
                    ret += str(luckynums[index])
                    if int(luckynums[index]) < int(ele):
                        previssmall = True
            else:
                ret += str(luckynums[-1])

        return ret


t = task()
print(t.solve(732, [3, 5, 7]))  # 577
print(t.solve(332, [3, 5, 7]))  # 077
print(t.solve(77712, [3, 5, 7]))  # 77577
print(t.solve(764, [3, 5, 7]))  # 757
print(t.solve(864, [3, 5, 7]))  # 777
print(t.solve(777, [3, 5, 7]))
print(t.solve(712, [3, 5, 7]))
print(t.solve(312, [3, 5, 7]))
print(t.solve(75411, [3, 5, 7]))
print(t.solve(77127, [3, 5, 7]))
