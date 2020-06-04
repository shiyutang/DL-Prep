# class Solution(object):
# 	"""docstring for Solution"""
# 	def calculateMinimumHP(self, dungeon):
# 		n = len(dungeon[0])
# 		need = [2**31] * (n-1) + [1]
# 		print(need)
# 		for row in dungeon[::-1]:
# 			print(row)
# 			for j in range(n)[::-1]:
# 				print('need[j:j+2] ,row[j]',need[j:j+2],row[j])
# 				need[j] = max(min(need[j:j+2]) - row[j], 1)
# 				print('need[j]',need[j])

# 		return need[0]

class Solution:
	def calculateMinimumHP(self, dungeon):
		cols = len(dungeon[0])
		need = [2**15]*(cols-1) + [1]  # 2**15 is the maximum need that will show up decided by you 
		for row in dungeon[::-1]:
			for col in range(cols-1,-1,-1):
				need[col] = max(min(need[col:col+2])-row[col],1)

		return need[0]

sol = Solution()

res = sol.calculateMinimumHP([[-2,-8,3],[-5,-10,1],[10,30,-5]])
res = sol.calculateMinimumHP([[5,23,-48,-21,-72,-62,-19,-55,-3,-93,-84,14,-34,46,-82,-46,39,26,47,-71,-46,-3,-59,-93,-13,-72,19,-43,-51,-2,-6,-53,12,-40,15,-94,37,-3,-32,-97]])
print(res)
