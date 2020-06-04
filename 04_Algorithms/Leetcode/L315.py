class Solution:
    def sort(self,nums):
        if len(nums) == 1:
            return nums
        center = int(len(nums)/2)
        sortleft = self.sort(nums[:center])
        sortright = self.sort(nums[center:])
        sortres = []
        while sortright or sortleft:
            if sortright == []:
                sortres.extend(sortleft)
                sortleft = []
            elif sortleft == []:
                sortres.extend(sortright)
                sortright = []
            else:
                if sortright[0]<sortleft[0]:
                    for key in sortleft:
                        self.count[key] += 1
                    sortres.append(sortright.pop(0))
                else:
                    sortres.append((sortleft.pop(0)))
        return sortres


    def countSmaller(self, nums):
        self.count = []
        self.sort(nums)
        return self.count





sol = Solution()
s = sol.countSmaller([5,2,6,5,7,7,8,3,5,2,7,1])
print(s)