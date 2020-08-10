# 使用set 统计词频，然后将词频加入到长度为k的优先队列进行排序
import heapq

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        freqset = dict()
        for word in words:
            if word not in freqset.keys():
                freqset[word] = 1
            else:
                freqset[word] += 1

        h = [(-freqset[ele], ele) for ele in freqset]
        heapq.heapify(h)
        ret = []
        while len(ret) < k:
            ret.append(heapq.heappop(h)[1])

        return ret


sol = Solution()
print(sol.topKFrequent(["a", "day", "is", "sunny", "a", "a", "sunny", "is", "is"], 4))
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
