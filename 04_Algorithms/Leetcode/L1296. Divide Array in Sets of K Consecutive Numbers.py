from collections import defaultdict


class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        if len(nums) % k != 0:
            return False
        else:
            cur_ele, length = [], []
            nums.sort()
            for ele in nums:
                if ele - 1 in cur_ele:
                    idx = cur_ele.index(ele - 1)
                    if length[idx] < k:
                        if length[idx] + 1 == k:
                            length.pop(idx)
                            cur_ele.pop(idx)
                        else:
                            cur_ele[idx] = ele
                            length[idx] += 1
                        continue
                cur_ele.append(ele)
                length.append(1)

            return len(length) == 0


# 连续整数，利用长度相除，必然能到连续相同位置（0，1，2 等）,但是到 注意避免不连续的部分也可以，需要添加连续的判断
from collections import defaultdict

class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        if len(nums) % k != 0:
            return False
        counts = defaultdict(int)
        for n in nums:
            counts[n % k] += 1

        # print(counts)
        return len(set(counts.values())) == 1


sol = Solution()
# data = [1, 2, 3, 3, 4, 4, 5, 6], 4
# data = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3
# data = [1, 2, 3, 4], 3
# data = [1], 3
data = [2, 4, 6], 3
res = sol.isPossibleDivide(data[0], data[1])
print(res)
