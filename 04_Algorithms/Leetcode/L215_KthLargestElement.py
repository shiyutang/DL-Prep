class Solution(object):
    def findKthLargest(self, nums, k):
        realidx = len(nums) - k
        pivot = nums[0]
        pivotidx = 0
        right = []
        left = []
        for i in range(1, len(nums)):
            if nums[i] <= pivot:
                left.append(nums[i])
                pivotidx += 1
            else:
                right.append(nums[i])
        # print(pivotidx)
        if pivotidx == realidx:
            # print(pivot)
            return pivot
        elif pivotidx < realidx:
            # print('find the right part')
            # print(right)
            res = self.findKthLargest(right, k)
        else:
            # print('find the left part')
            # print(left)
            # print(k-len(nums[pivotidx:]))
            res = self.findKthLargest(left, k - len(right) - 1)
        return res


sol = Solution()
# res = sol.findKthLargest([3,2,3,1,2,4,5,5,6],4)
# print(res)
# res = sol.findKthLargest([3,2,1,5,6,4],2)
# print(res)
res = sol.findKthLargest([3, 4, 3, 2, 1, 45, 6, 3, 6, 2, 43, 53, 3, 2, 2], 3)
print(res)
