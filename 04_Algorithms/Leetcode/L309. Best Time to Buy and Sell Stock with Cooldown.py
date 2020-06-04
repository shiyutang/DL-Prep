## Unsolved

class Solution:
	def maxProfit(self, prices):
		profit = []
		for i in range(len(prices)):
			if i == 0:
				continue
			else:
				profit.append(prices[i]-prices[i-1])
		print(profit)
		totalProfit = 0
		jump = False
		coolDown = False
		for i in range(len(profit)):
			if jump == True:
				jump = False
				continue
			# print(profit[i])
			if profit[i]>=0:
				totalProfit += profit[i]
			else:
				if i+1<len(profit) and i-1>=0:
					if profit[i-1]> 0 and profit[i+1]>0: 
						if coolDown:
							tmpProfit0 = profit[i+1]+profit[i]
							tmpProfit1 = profit[i+1]-profit[i-1]  # cool down 
							
							print(tmpProfit0,tmpProfit1)
							totalProfit += max(tmpProfit1,tmpProfit0,0)
							if tmpProfit1>0 and tmpProfit1>tmpProfit0:
								coolDown = True
							else:
								coolDown = False
						else:
							totalProfit += profit[i+1]
						jump = True
			print('i,totalProfit',i,totalProfit)

		return totalProfit

sol = Solution()
# print(sol.maxProfit([1,4,2]))  # 3
# print(sol.maxProfit([2,1,2,0,2]))# 2
# print(sol.maxProfit([2,1,4])) # 3
# print(sol.maxProfit([6,1,3,2,4,7]))# 6
# print(sol.maxProfit([2,1,4,5,2,9,7])) #10
# print(sol.maxProfit([1,7,2,4])) # 6
print(sol.maxProfit([2,6,8,7,8,7,9,4,1,2,4,5,8])) #15
