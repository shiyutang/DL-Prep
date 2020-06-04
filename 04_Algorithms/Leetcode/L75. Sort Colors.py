class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return nums
        zeroList,onelist,twolist = [],[],[]
        for num in nums:
        	if num == 0:
        		zeroList.append(0)
        	elif num == 1:
        		onelist.append(1)
        	else:
        		twolist.append(2)

        nums[:] = zeroList+onelist+twolist
        print(nums)


sol =Solution()
sol.sortColors([2,0,2,1,1,0])
