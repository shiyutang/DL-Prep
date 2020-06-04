class Solution:
    def ForceWin(self,numToChoose,desiredTotal):
        print(numToChoose)
        print(desiredTotal)
        if max(numToChoose)>=desiredTotal:  # I will win this turn
            print("total reachable")
            return True
        else:
            result = []
            for i,num in enumerate(numToChoose):
                # besides this  number I choose and remove my choosed number from total to pass it to my rival
                res = self.ForceWin(numToChoose[:i]+numToChoose[i+1:],desiredTotal-num)
                if not res: # one choice will make me win
                    print('returnTrue')
                    return True
                result.append(res)
            if all(result):  # all choice will make my rival win and I lose
                print('returnFalse')
                return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        numToChoose = [i for i in range(1,maxChoosableInteger+1)]
        if sum(numToChoose)<desiredTotal:  # if no one can win
            return False
        CanWin = self.ForceWin(numToChoose,desiredTotal)
        print(CanWin)
        return CanWin

sol = Solution()
res = []
for i in range(30,60,1):
    res.append(sol.canIWin(10,i))
print(res)