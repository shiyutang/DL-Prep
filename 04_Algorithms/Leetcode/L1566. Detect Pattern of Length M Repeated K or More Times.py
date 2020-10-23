class Solution:
    def containsPattern(self, arr: list, m: int, k: int) -> bool:
        if m > len(arr):
            return False
        elif m == len(arr):
            if k != 1:
                return False
            else:
                return True
        else:
            arr = ''.join(list(map(str,arr)))
            prevset = set()
            for i in range(len(arr) - m + 1):
                pat = arr[i:m + i]
                if pat in prevset:
                    continue
                else:
                    if pat*k in arr:
                        return True
                    prevset.add(pat)
                # print(prevset)

            return False


sol = Solution()
print(sol.containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(sol.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(sol.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
print(sol.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(sol.containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
print(sol.containsPattern(arr=[2, 2], m=1, k=2))
print(sol.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
