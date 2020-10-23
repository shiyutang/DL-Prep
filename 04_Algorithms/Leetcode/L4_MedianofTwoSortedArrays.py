class Solution(object):
    """delete one max and one min in two lists in turn to left the median
	be carful of the index out of bound error on both side
	since you are deleting"""

    def findMedianSortedArrays(self, nums1, nums2):
        totalcnt = len(nums2) + len(nums1)
        if (totalcnt) % 2 == 0:
            finalcnt = 2
        else:
            finalcnt = 1
        flag = 0  # cut tail
        for i in range(totalcnt - finalcnt):
            if flag == 0:
                if len(nums2) == 0 or (len(nums1) != 0 and nums1[-1] > nums2[-1]):
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
                flag = 1
            else:
                if len(nums2) == 0 or (len(nums1) != 0 and nums1[0] < nums2[0]):
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                flag = 0
            print(nums1, nums2)
        avnum = sum(nums1) + sum(nums2)
        return avnum / finalcnt


sol = Solution()
res = sol.findMedianSortedArrays(nums1=[3], nums2=[-2, -1])
# res = sol.findMedianSortedArrays(nums1 = [1,3,5,6,9,23,54,64],nums2 = [2,4,5,6,7,12,15,35])

print(res)
