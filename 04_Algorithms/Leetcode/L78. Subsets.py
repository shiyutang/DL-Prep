class Solution:
	def subsets(self, nums):
		nums = list(set(nums))
		subsets = [[]]
		for n in nums:
		    subsets += [s + [n] for s in subsets]
		return subsets




sol = Solution()
print(sol.subsets([1,1,3,2,1,2,1,1,2,1]))