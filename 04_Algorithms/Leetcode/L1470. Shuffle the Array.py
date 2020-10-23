class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        def helper(idx):
            if idx < n:
                return 2 * idx
            else:
                return 2 * (idx - n) + 1

        for i in range(len(nums)):
            if nums[i] < 0 or i == 0:
                continue
            gotoidx = helper(i)
            nextnum = -nums[i]
            while nums[gotoidx] > 0:
                # print(nums, nextnum, gotoidx)
                nextnum, nums[gotoidx] = -nums[gotoidx], nextnum
                gotoidx = helper(gotoidx)
        for i in range(1, len(nums)):
            nums[i] = -nums[i]

        return nums


sol = Solution()
print(sol.shuffle([2, 5, 1, 3, 4, 7], 3))
print(sol.shuffle([1,2,3,4,4,3,2,1], 4))
print(sol.shuffle([1,1,2,2], 2))
