import copy
class Solution:
    def conflict(self,index,Qpos):
        for i,pos in enumerate(Qpos[:index]):
            if pos == Qpos[index] or (abs(Qpos[index]-pos) == abs(index-i)):
                return True

    def prettyformat(self,results,n):
        res = []
        subres = []
        baseform = '.'
        for _ in range(n-1):
            baseform += '.'
        for result in results:
            for i in range(len(result)):
                subres.append(baseform[:result[i]]+'Q'+baseform[result[i]+1:])
            res.append(subres)
            subres = []
        return res

    def solveNQueens(self, n):
        Qpos = [-1 for _ in range(n)]
        Qnum = 1
        result = []
        Qpos[0] = 0
        while Qnum>0:  # not back to root
            while Qpos[Qnum-1]<n and self.conflict(Qnum-1,Qpos): #if pos is valid but conflict
                Qpos[Qnum - 1] += 1
            print(Qpos)
            if Qpos[Qnum-1] < n:  #if position is valid and not conflict
                if Qnum == n:      # if this is the last queen
                    Qposc = copy.deepcopy(Qpos)
                    result.append(Qposc)
                    print("result is {}".format(result))
                    Qpos[Qnum-1] = Qpos[Qnum-1]+1
                else:              # if this is not the last Queen
                    Qnum +=1
                    Qpos[Qnum - 1] = 0
                    print(Qnum)
                    print(Qpos)
            else:              # if the position is not valid
                Qnum -= 1      # put the queen back and try previous queen
                Qpos[Qnum-1] = Qpos[Qnum-1]+1  # previous queen move back
                print(Qnum)
                print(Qpos)
        print(result)
        print("res len= {}".format(len(result)))
        resultpretty = self.prettyformat(result,n)
        print(resultpretty)
        return  resultpretty

sol = Solution()
sol.solveNQueens(8)