
# 把偶数位置插入排序后的较大部分，但是注意中间值会相近导致相邻不满足条件，因此就将大和较大，小和较小匹配
class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            a = nums[:]
            a.sort(reverse=True)
            start = len(nums) // 2

            nums[::2], nums[1::2] = a[start:], a[:start]

        print(nums)


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    nums = [1, 4, 1, 5, 1, 6]
    nums = [2, 17, 13, 2, 7, 9, 10, 5, 14, 15]
    nums = [2, 3, 2, 2, 3, 3, 2, 3, 2]
    # nums = [1, 2, 1, 2, 1, 1, 2, 2, 1]
    print(nums, end=' ')
    sol.wiggleSort(nums)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)
            print(nums, end=' ')
            sol.wiggleSort(nums)


test(Solution, True)
