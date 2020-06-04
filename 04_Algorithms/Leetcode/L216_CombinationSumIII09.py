class Solution:
    def combinationSum3(self, k, n):
        result = []
        if k == 1 and n<=9:
            return n
        elif (k==1 and n>9) or (k==2 and n>=18):
            return []
        elif n<18 and k==2:
            if n/2%1>=0.5:
                upper = int(n/2)+1
            else:
                upper = int(n/2)
            for i in range(max(1,n-9),upper):
                result.append([i,n-i])
        elif k>=3:
            for m in range(1,10):
                if sum([m+i for i in range(k)]) <=n:
                    rest = self.combinationSum3(k-1,n-m)
                    print(rest)
                    for element in rest:
                        if m in element:
                            continue
                        else:
                            element.insert(0, m)
                            element.sort()
                            if not (element in result):
                                result.append(element)
                else:
                    break
        return result

sol = Solution()
res = sol.combinationSum3(2,13)
print(res)
