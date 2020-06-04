class Solution:
    def splitArray(self, nums, m):
        l,h = max(nums),sum(nums)
        if m == len(nums):
        	return l

        self.nums = nums

        def CountOfMedian(median):
        	numsum,cnt = 0,0
        	for num in nums:
        		numsum += num
        		# print('numsum',numsum)
        		if numsum>median:
        			cnt += 1
        			numsum = num 
        	return cnt+1

        while l<h:
        	median = (l+h)//2
        	# print('l,h,median,CountOfMedian(median),m',l,h,median,CountOfMedian(median),m)
        	if CountOfMedian(median) > m:
        		l = median+1
        	else:
        		h = median

        return l

sol = Solution()
# print(sol.splitArray([7,2,5,10,8],3))
print(sol.splitArray([7,5,6],3))

