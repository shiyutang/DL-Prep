class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        head, tail = 0, len(array) - 1
        while head < tail:
            while tsum - array[head] < array[tail]:
                tail -= 1
            if tsum - array[head] == array[tail]:
                return array[head], array[tail]
            else:
                head += 1
        return []


sol = Solution()
print(sol.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
