import itertools

class Solution:
    def permuteUnique(self, nums):
        res = set()
        if nums == []:
            return [[]]

        for i in itertools.permutations(nums, len(nums)):
            if not i in res:
            	res.add(i)

        s = []
        for val in res:
        	s.append(list(val))
            
        return s

sol = Solution()
# result = sol.permuteUnique([1,1,1,2,2])
result = sol.permuteUnique("eat")
print(result)        