class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    	def findCombo(candidates,target,index,combo):
    		for i in range(index,len(candidates)):
    			if candidates[i] > target:
    				break
    			return findCombo(candidates,target-candidates[i], i,combo)



    	candidates = sorted(candidates)
    	print(candidates)
    	return findCombo