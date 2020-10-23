class Solution2:
    def stoneGameV(self, stoneValue) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            ans = 0
            total = hashmap[j + 1] - hashmap[i]
            left = 0
            for idx in range(i, j):
                left += stoneValue[idx]
                right = total - left
                if left < right:
                    ans = max(ans, left + dp(i, idx))
                elif right < left:
                    ans = max(ans, right + dp(idx + 1, j))
                else:
                    ans = max(ans, left + max(dp(i, idx), dp(idx + 1, j)))
            return ans

        hashmap = [0]
        for ele in stoneValue:
            hashmap.append(hashmap[-1] + ele if len(hashmap) > 0 else ele)
        print(hashmap)
        return dp(0, len(stoneValue) - 1)


class Solution:
    def stoneGameV(self, stoneValue) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            ans = 0
            total = hashmap[j] - hashmap[i - 1]
            left = 0
            for idx in range(i, j):
                left += stoneValue[idx]
                right = total - left
                if left >= total // 2:
                    if right == 0:
                        tt = [(left - stoneValue[idx], right + stoneValue[idx], idx - 1)]
                    elif left - stoneValue[idx] == 0:
                        tt = [(left, right, idx)]
                    else:
                        tt = [(left - stoneValue[idx], right + stoneValue[idx], idx - 1), (left, right, idx)]

                    for left, right, index in tt:
                        if left < right:
                            ans = max(ans, left + dp(i, index))
                        elif right < left:
                            ans = max(ans, right + dp(index + 1, j))
                        else:
                            ans = max(ans, left + max(dp(i, index), dp(index + 1, j)))
                print(left,right,total,ans)

            return ans

        hashmap = {-1: 0}
        for i in range(len(stoneValue)):
            hashmap[i] = hashmap[i - 1] + stoneValue[i]
        print(hashmap)
        return dp(0, len(stoneValue) - 1)


sol = Solution()
# print(sol.stoneGameV([6, 2, 3, 4, 5, 5]))
# print(sol.stoneGameV([7, 7, 7, 7, 7, 7, 7]))
# print(sol.stoneGameV([7]))
print(sol.stoneGameV([98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))
