class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        leastcost = []

        def helper(slist, num):
            """
            find the first number that is bigger than num
            :param slist:
            :param num:
            :return:
            """
            low, high = 0, len(slist) - 1
            mid = (low + high) // 2
            while low < high:
                if num > slist[mid]:
                    low = mid + 1
                elif num == slist[mid]:
                    return mid
                else:
                    if slist[mid - 1] < num:
                        return mid
                    else:
                        high = mid          # 注意这里不能-1 因为可能跳过第一位，即前面没有小于他的也需要替代
                mid = (low + high) // 2

                # print(low, high, mid, slist[mid])

            return mid

        for num in nums:
            if not leastcost or num > leastcost[-1]:
                leastcost.append(num)
            else:
                idx = helper(leastcost, num)
                leastcost[idx] = num
            # print(leastcost)

        return len(leastcost)


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101]))
print(sol.lengthOfLIS([]))
print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))
