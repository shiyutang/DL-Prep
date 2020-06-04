import copy
class Solution:
    def isMonotonic(self, A):
        d = copy.deepcopy(A)
        A.sort()
        sortA =  copy.deepcopy(A)
        A.sort(reverse = True)
        resortA = copy.deepcopy(A)
        if d == sortA or d == resortA:
            return True
        else:
            return False
sol = Solution()
sol.isMonotonic([1,2,2,3])