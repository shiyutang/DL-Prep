# 整数数组 -》bool几乎
# 调整依次就有序，子数组颠倒
# one-swap -> sorted   OR
# one-reverse -> sorted
# 1 5 3 4 2 6
# 1 5 4 3 2 6

# 排除多次异常
class task:
    def solve(self, array):
        first, second = None, None
        continuous = None
        # find first and second(index)
        for j, ele in enumerate(array):
            if j == 0:
                continue
            else:
                if ele < array[j - 1]:
                    if not first:  # 第一次异常
                        first = j - 1
                    elif not second:  # 第二次向下（连续/断开）
                        second = j
                    else:  # 已经有第二次向下
                        if second == j - 1:  # 只记录连续
                            continuous = True
                            second = j
                        else:  # 否则需要多次不能实现
                            return False
                else:
                    continue

        # whether solid after swap
        if first and second:
            if continuous:  # continuous: check boundarys
                if second + 1 < len(array) and first - 1 >= 0:
                    return array[first] <= array[second + 1] and array[second] >= array[first - 1]
                elif second + 1 < len(array):
                    return array[first] <= array[second + 1]
                elif first - 1 >= 0:
                    return array[second] >= array[first - 1]
                else:
                    return True
            else:  # swap: check in and out
                if second + 1 < len(array) and first - 1 >= 0:
                    return array[second - 1] <= array[first] <= array[second + 1] and array[first + 1] >= array[
                        second] >= \
                           array[first - 1]
                elif second + 1 < len(array):
                    return array[second - 1] <= array[first] <= array[second + 1] and array[second] <= array[first + 1]
                elif first - 1 >= 0:
                    return array[first + 1] >= array[second] >= array[first - 1] and array[first] >= array[second - 1]
                else:
                    return array[first + 1] >= array[second] and array[first] >= array[second - 1]
        else:
            if not first and not second:
                print("This is a sorted array already~")
                return True
            else:
                return False


t = task()
print(t.solve([1, 5, 3, 4, 2, 6]))  # true
print(t.solve([1, 7, 3, 4, 2, 6]))  # False
print(t.solve([1, 5, 4, 3, 2, 6]))  # true
print(t.solve([1, 5, 4, 3, 2, 1, 0, 6]))  # False
print(t.solve([1, 5, 4, 3, 2, 6, 7, 2]))  # False
