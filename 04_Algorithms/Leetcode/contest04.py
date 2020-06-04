## wrong answer

class Solution:
    def bonus(self, n, leadership, operations):
        leaderDict = {}
        coins = [0 for _ in range(n)]
        result = []
        for relation in leadership:
        	if relation[0] in leaderDict:
        		leaderDict[relation[0]].append(relation[1])
        	else:
        		leaderDict[relation[0]] = [relation[1]]
        for i in range(1,n+1):
        	if not i in leaderDict:
        		leaderDict[i] = None
        # print('leaderDict',leaderDict)

        for operation in operations:
        	# print('operation',operation)
        	if operation[0] == 1:
        		coins[operation[1]-1] += operation[2]
        	elif operation[0] == 2:
        		coins[operation[1]-1] += operation[2]
        		if leaderDict[operation[1]]:
	        		for sub in leaderDict[operation[1]]:
	        			if not sub == None:
	        				coins[sub-1] += operation[2]
        	else:
        		res = coins[operation[1]-1]
        		stack = [leaderDict[operation[1]]]
        		# print(stack)
        		while stack:
        			subs = stack.pop(0)
        			# print('subs',subs)
        			if subs:
        				for subpeople in subs:
        					res += coins[subpeople-1]
        					if leaderDict[subpeople]:
        						stack.append(leaderDict[subpeople])
        			else:
        				continue
        		res = res%(1000000007)
        		result.append(res)
        	# print('coins',coins)

        return result




sol = Solution()
print(sol.bonus(n = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]))