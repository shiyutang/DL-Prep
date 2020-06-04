# 使用 Pascal 递推公式计算，有点慢

import collections


def choose_k_from_n(n, k):
    """求取组合数（n, k）"""
    C = collections.defaultdict(int)
    for row in range(n + 1):
        C[row, 0] = 1
        print(C)
        for col in range(1, min(row + 1, k + 1)):
            C[row, col] = C[row - 1, col - 1] + C[row - 1, col]  # 递推公式，同时保存运算结果
            print(C)
    return C[n, k]


print(choose_k_from_n(10, 3))
