# this don't constrain the number we choose

import copy
class Solution:
    def combinationSum3(self, k, n):
        if sum([i for i in range(1,k+1)])>n:
            return []
        element = [0]*k
        element[1] = 1
        element[k-1] = k
        result = []
        while 3*element[0]+2 <= n:  # stop process
            element[0] += 1
            if result != []:
                result.pop()
                element[k-1] = 100
                element[1] = element[0]
            while element[k-1] > element[k-2]: #stop every loop
                element[1] += 1
                for i in range(2,k-1):
                    element[i] = element[i-1]+1
                element[k-1] = 0
                element[k-1] = n-sum(element)
                elements = copy.deepcopy(element)
                result.append(elements)
        result.pop()
        print(result)
        return result

sol = Solution()
sol.combinationSum3(3,17)
