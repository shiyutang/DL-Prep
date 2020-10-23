# ok * 1
# 注意动态规划时，需要对每个星星都在可以加入时，选择加入或者不加入，并创建一个新的状态用于后续的累计
# 对于每一个新的时间，只需要在之前的时间中选择权值最大的加入即可

class Solution:
    def solve(self, s):
        memo = set()
        for i, ele in enumerate(s):
            start, end, w = ele
            if i == 0:
                memo.add((0, 0))
                memo.add((w, end))  # weight,end
            else:
                maxtmp = None
                for ele in memo:
                    if ele[1] < start:
                        tmp = (w + ele[0], end)
                        if not maxtmp:
                            maxtmp = tmp
                        elif tmp[0] > maxtmp[0]:
                            maxtmp = tmp
                if maxtmp:
                    memo.add(maxtmp)
            # print(memo)
        ret = 0
        for ele in memo:
            ret = max(ret, ele[0])

        return ret


stars = int(input())
s = []
for _ in range(stars):
    s.append(list(map(int, input().split(' '))))

s.sort(key=lambda x: (x[0], -x[2]), reverse=False)
# print(s)
sol = Solution()
print(sol.solve(s))


# 而不是在每个状态就直接选择，因为中间状态的选择会影响后续状态
# class Solution:
#     def solve(self, s):
#         memo = [[(0, 0) for _ in range(2)] for _ in range(len(s))]
#         for i, ele in enumerate(s):
#             start, end, w = ele
#             # print(start,end,cnt,1 in self.timeline[start:end+1])
#             if i == 0:
#                 memo[i][1] = (w, end)  # weight,end
#             else:
#                 if memo[i - 1][0][0] > memo[i - 1][1][0]:
#                     tmp = memo[i - 1][0]
#                     tmp2 = (memo[i - 1][0][0] + w, end)
#                 else:
#                     tmp = memo[i - 1][1]
#                     tmp2 = (memo[i - 1][1][0] + w, end)
#
#                 memo[i][0] = tmp
#                 if memo[i - 1][1][1] < start and memo[i - 1][0][1] < start:  # 上一个增加了的最后一位小于当前
#                     memo[i][1] = tmp2
#                 elif memo[i - 1][0][1] < start:
#                     memo[i][1] = (memo[i - 1][0][0] + w, end)
#                 elif memo[i - 1][1][1] < start:
#                     memo[i][1] = (memo[i - 1][1][0] + w, end)
#                 else:
#                     memo[i][1] = memo[i][0]
#             # print(memo)
#
#         return max(memo[-1][0][0], memo[-1][1][0])
#
#
# stars = int(input())
# s = []
# for _ in range(stars):
#     s.append(list(map(int, input().split(' '))))
#
# s.sort(key=lambda x: (x[0], -x[2]), reverse=False)
# # print(s)
# sol = Solution()
# print(sol.solve(s))
