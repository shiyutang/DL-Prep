import copy
class Solution:
    def calculateMinimumHP(self, dungeon):
        minNowLife = copy.deepcopy(dungeon)
        if dungeon[0][0]<0:
            minNowLife[0][0] = [-dungeon[0][0]+1,0]
        else:
            minNowLife[0][0] = [1,dungeon[0][0]]
        print(minNowLife)
        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if not (i==0 and j==0):
                    if i-1<0:
                        lifebase = minNowLife[i][j-1]
                    elif j-1<0:
                        lifebase = minNowLife[i-1][j]
                    else:
                        if dungeon[i][j]<0:
                            if minNowLife[i][j-1][0]-(minNowLife[i][j-1][1] + dungeon[i][j])\
                                <minNowLife[i-1][j][0]-(minNowLife[i-1][j][1] + dungeon[i][j]):
                                lifebase = minNowLife[i][j-1]
                            else:
                                lifebase = minNowLife[i-1][j]
                        else:
                            if minNowLife[i][j-1][0]<minNowLife[i-1][j][0]:
                                lifebase = minNowLife[i][j-1]
                            elif minNowLife[i][j-1][0]==minNowLife[i-1][j][0]:
                                if minNowLife[i][j-1][1]<=minNowLife[i-1][j][1]:
                                    lifebase = minNowLife[i-1][j]
                                else:
                                    lifebase = minNowLife[i][j-1]
                            else:
                                lifebase = minNowLife[i-1][j]
                    print(lifebase)
                    minNowLife[i][j] = [0,0]
                    if dungeon[i][j]>=0:
                        minNowLife[i][j][1] = lifebase[1]+dungeon[i][j]
                        minNowLife[i][j][0] = lifebase[0]
                    else:
                        if lifebase[1]+dungeon[i][j]>=0:
                            minNowLife[i][j][1] = lifebase[1]+dungeon[i][j]
                            minNowLife[i][j][0] = lifebase[0]
                        else:
                            minNowLife[i][j][0] = lifebase[0] -(lifebase[1] + dungeon[i][j])
                            minNowLife[i][j][1] = 0
                    print(minNowLife[i][j])
                    print(minNowLife)
        print(minNowLife[len(dungeon)-1][len(dungeon[0])-1])
        return minNowLife[len(dungeon)-1][len(dungeon[0])-1][0]

sol = Solution()
# sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
sol.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
