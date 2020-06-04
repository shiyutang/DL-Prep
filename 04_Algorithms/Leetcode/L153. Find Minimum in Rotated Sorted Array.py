class Solution:
    def findMin(self, nums):
        start,end = 0,len(nums)-1
        if nums[-1] > nums[0]:
            return nums[0]
        elif end == start:
            return nums[0]
        self.nums = nums
        
        def findPit(start,end):
            print('start,end',start,end)
            if end-start == 1:
                return end
            elif end-start >=2:
                median = (start+end)//2
                if self.nums[start] > self.nums[median]:
                    if self.nums[median-1]>self.nums[median]:
                        return median
                    else:
                        return findPit(start,median-1)
                    
                elif self.nums[median] >self.nums[end]:
                    if self.nums[median]>self.nums[median+1]:
                        return median+1
                    else:
                        return findPit(median+1,end)
            else: 
                print(start)
                
        idx = findPit(start,end)

        return nums[idx]

sol = Solution()
print(sol.findMin([4,5,6,7,8,9,0,2,3]))