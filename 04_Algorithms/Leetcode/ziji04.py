n, m = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    num = num % m


# nums.sort()
def helper(i, cursum):
    global res
    res = max(res, cursum % m)
    if i <= n - 1:
        if nums[i] == 0:
            helper(i + 1, cursum)
        else:
            helper(i + 1, cursum)
            helper(i + 1, cursum + nums[i])
    else:
        return


res = 0
helper(0, 0)
print(res)
