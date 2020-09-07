class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for pointer in range(len(nums) - 1, 0, -1):
            if nums[pointer] > nums[pointer - 1]:
                flag = True
                break
        if not flag:
            nums.reverse()
        else:
            # 找到下一个比当前数大的最小数，并交换
            p1 = pointer - 1
            p2 = pointer
            minval = nums[pointer]
            for i, ele in enumerate(nums[pointer + 1:]):
                if nums[pointer - 1] < ele < minval:
                    minval = ele
                    p2 = pointer + 1 + i
            nums[p1], nums[p2] = nums[p2], nums[p1]
            # print(nums)

            # 后面需要再排序
            tmp = nums[p1 + 1:]
            tmp.sort()
            nums[p1+1:] = tmp

        print(nums)


sol = Solution()
sol.nextPermutation([1, 3, 2])
sol.nextPermutation([2, 3, 1])
sol.nextPermutation([2, 3, 1, 3, 3])
sol.nextPermutation([5, 4, 3])
sol.nextPermutation([1, 7, 3])
sol.nextPermutation([1, 5, 7, 6])
