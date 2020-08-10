import functools


class Solution:
    def minNumber(self, data: list[int]) -> str:
        def mycompare(a, b):
            if a + b > b + a:
                return 1
            elif a + b == b + a:
                return 0
            else:
                return -1

        data = list(map(str, data))
        data.sort(key=functools.cmp_to_key(mycompare))

        ret = ''.join(data)
        return ret


class Solution:
    def minNumber(self, nums: list) -> str:
        def fast_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)


sol = Solution()
print(sol.arrange(['3', '32', '321']))
print(sol.arrange(['03', '032', '321']))
print(sol.arrange(['', '', '']))
