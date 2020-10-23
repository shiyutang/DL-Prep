class Solution_slow:
    def findLatestStep(self, arr, m: int) -> int:
        start, end, length = [], [], []
        findlength, ret = False, None
        for idx, ele in enumerate(arr):
            try:
                startidx = start.index(ele + 1)
            except:
                startidx = -1
            try:
                endidx = end.index(ele - 1)
            except:
                endidx = -1

            if startidx != -1 and endidx != -1:
                head, tail = start[endidx], end[startidx]
                start[startidx] = head
                end[startidx] = tail
                appendlen = tail - head + 1
                length[startidx] = appendlen
                start.pop(endidx);
                end.pop(endidx);
                length.pop(endidx)
            elif startidx != -1:
                start[startidx] = ele
                appendlen = length[startidx] + 1
                length[startidx] = appendlen
            elif endidx != -1:
                end[endidx] = ele
                appendlen = length[endidx] + 1
                length[endidx] = appendlen
            else:
                start.append(ele)
                end.append(ele)
                appendlen = 1
                length.append(1)
            findlength = findlength or appendlen == m
            if findlength and m not in length:
                ret = idx
                findlength = False
            # print(idx, ele, findlength, m in length)

        if not ret:
            if not findlength:
                return -1
            else:
                return len(arr)
        else:
            return ret


class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        length, recoder = [], [(-1, -1) for _ in range(len(arr))]
        mcnt = 0
        findlength, ret = False, None
        for i, ele in enumerate(arr):
            ele = ele-1
            start, end = ele, ele
            if ele - 1 >= 0 and recoder[ele - 1] != (-1, -1):
                start = recoder[ele - 1][0]
                if recoder[ele - 1][1] - recoder[ele - 1][0] + 1 == m:
                    mcnt -= 1

            if ele + 1 < len(arr) and recoder[ele + 1] != (-1, -1):
                end = recoder[ele + 1][1]
                if recoder[ele + 1][1] - recoder[ele + 1][0] + 1 == m:
                    mcnt -= 1

            recoder[ele], recoder[start], recoder[end] = (start, end), (start, end), (start, end)
            if end - start + 1 == m:
                mcnt += 1
            findlength = findlength or (mcnt > 0)
            if findlength and mcnt == 0:
                ret = i
                findlength = False
            # print(i, ele, findlength, mcnt, recoder)

        if not ret:
            if not findlength:
                return -1
            else:
                return len(arr)
        else:
            return ret


sol = Solution()
print(sol.findLatestStep([10, 6, 9, 4, 7, 8, 5, 2, 1, 3], 1))
print(sol.findLatestStep([9, 7, 8, 3, 1, 6, 5, 2, 10, 4], 5))
print(sol.findLatestStep([3, 5, 1, 2, 4], 1))
print(sol.findLatestStep([3, 5, 1, 2, 4], 2))
print(sol.findLatestStep([1, 2], 2))
print(sol.findLatestStep([1], 1))
