class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pnum1 = m - 1
        plist = m + n - 1
        pnum2 = n - 1
        while pnum1 >= 0 and pnum2 >= 0:
            if nums2[pnum2] > nums1[pnum1]:
                nums1[plist] = nums2[pnum2]
                pnum2 -= 1
            else:
                nums1[plist] = nums1[pnum1]
                pnum1 -= 1
            plist -= 1

        if pnum2 >= 0:
            nums1[:pnum2 + 1] = nums2[:pnum2 + 1]
        print(nums1)


sol = Solution()
print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(sol.merge([0, 0, 0], 0, [2, 5, 6], 3))
print(sol.merge([1, 2, 3], 3, [], 0))
print(sol.merge([], 0, [], 0))
