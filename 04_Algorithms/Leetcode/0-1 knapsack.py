def knapsack(C, value_list, weight_list):
    """
              C : 背包容量
     value_list : 商品价值列表
    weight_list ：商品重量列表

    """
    n = len(value_list)
    dp = [[0 for _ in range(C + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            # 如果当前背包容量还够装下当前商品
            if j >= weight_list[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight_list[i - 1]] + value_list[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][C]


# test
import random

test_time = 20
for _ in range(test_time):
    C = random.randint(0, 100)
    items = random.randint(1, 20)

    valueL, weightL = [], []
    for _ in range(items):
        valueL.append(random.randint(0, 10))
        weightL.append(random.randint(1, 20))

    res = knapsack(C, valueL, weightL)
    print("The knapsack with volume {} will contain items "
          "worth {} when values are {} and weights are {}".format(C, res, valueL, weightL))
