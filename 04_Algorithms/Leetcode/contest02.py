### past if given the special case n==1

import math

class Solution:
    def fraction(self, cont):
        if len(cont) == 1:
            return [cont[-1],1]

        self.res = []
        def getChildren(num):
            isZhishu = True
            i = 2
            square = int(math.sqrt(num)) + 1
            while i <= square:
                if num % i == 0:
                    self.res.append(i)
                    isZhishu = False
                    getChildren(num // i)
                    i += 1
                    break
                i += 1
            if isZhishu:
                self.res.append(num)

        def plusReverse(n,m,zhengshu):
            n += zhengshu*m
            return m,n


        n,m = 1,cont[-1]
        for i in range(len(cont)-2,-1,-1):
            n,m = plusReverse(n,m,cont[i])
            if i == 0:
                n,m = m,n
            # print('n,m',n,m,cont[i])

        # divisorm,divisorn = getChildren(m),getChildren(n)
        # if divisorm and divisorn:
        #     if len(divisorm) >=len(divisorn):
        #         for i,item in range(len(divisorn)-1,-1,-1):
        #             if item in divisorm:
        #                 divisorm.remove(item)
        #                 del divisorn[i]
        #     else:
        #         for i,item in range(len(divisorm)-1,-1,-1):
        #             if item in divisorn:
        #                 divisorn.remove(item)
        #                 del divisorm[i]

        #     n,m = 1,1
        #     for element in divisorn:
        #         n *= element
        #     for elementm in divisorm:
        #         m *= elementm
        # else:
        #     return [n,m]


        return [n,m]

sol = Solution()
# print(sol.fraction([3, 2, 0, 2]))
# print(sol.fraction([0, 0, 3]))
print(sol.fraction([1,1,7,1,1, 1]))






            
        