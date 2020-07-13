# not finished

import copy
class Solution:
    def conflict(self,index,Qpos):
        for i,pos in enumerate(Qpos[:index]):
            if pos == Qpos[index] or (abs(Qpos[index]-pos) == abs(index-i)):
                return True

    def recursion(self,Qpos,Qnum):
        result = []
        while Qpos[Qnum - 1] < len(Qpos) and self.conflict(Qnum - 1, Qpos):  # if pos is valid but conflict
            Qpos[Qnum - 1] += 1
        if Qpos[Qnum - 1] < len(Qpos):
            if Qnum == len(Qpos):
                Qposc = copy.deepcopy(Qpos)
                print("result is {}".format(Qposc))
                Qpos[Qnum - 1] = Qpos[Qnum - 1] + 1
                result.append(self.recursion(Qpos,Qnum))
                return
            else:
                self.recursion()

    def prettyformat(self, results, n):
        res = []
        subres = []
        baseform = '.'
        for _ in range(n - 1):
            baseform += '.'
        for result in results:
            for i in range(len(result)):
                subres.append(baseform[:result[i]] + 'Q' + baseform[result[i] + 1:])
            res.append(subres)
            subres = []
        return res

    def solveNQueens(self, n):
        Qpos = [-1 for _ in range(n)]
        Qnum = 1
        Qpos[0] = 0
        result = self.recursion(Qpos,Qnum)
        return self.prettyformat(result,n)
