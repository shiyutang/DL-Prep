class Solution:
    def getStrongest(self, arr: list, k: int) -> list:
        if k == len(arr):
            return arr
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        ret = []
        head, tail = 0, len(arr) - 1
        while len(ret) < k:
            abshead = abs(arr[head] - median)
            abstail = abs(arr[tail] - median)
            print(arr,median, head, tail, abshead, abstail, ret)
            if abstail >= abshead:
                ret.append(arr[tail])
                tail -= 1
            else:
                ret.append(arr[head])
                head += 1
        return ret


sol = Solution()
# print(sol.getStrongest(arr=[1, 2, 3, 4, 5], k=2))
# print(sol.getStrongest(arr=[1, 1, 3, 5, 5], k=2))
print(sol.getStrongest(arr=[6, 7, 11, 7, 6, 8], k=5))
# print(sol.getStrongest([6, -3, 7, 2, 11], k=3))
print(sol.getStrongest(arr=[-7, 22, 17, 3], k=2))
