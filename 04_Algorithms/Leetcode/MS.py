# A -> B -> C -> D -> E
# N = 2
#
# A -> B -> D -> C -> E
import heapq


class task0:
    def solve(root, N):
        if not root or N <= 0:
            return root

        def switch(node):
            lastNp1 = node.next
            lastN = lastNp1.next
            lastNm1 = lastN.next

            node.next = node.next.next
            lastN.next = lastNp1
            lastNp1.next = lastNm1

        cur, lastNp2 = root, root
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
            if cnt > N + 2:
                lastNp2 = lastNp2.next
                cnt = N + 2

        # link is no long enough

        if cnt < N + 2:
            if cnt == N + 1:
                lastNp1 = lastNp2
                lastN = lastNp1.next
                lastNm1 = lastN.next

                lastN.next = lastNp1
                lastNp1.next = lastNm1
                return lastN
            else:
                return root
        else:
            switch(lastNp2)
            return root


# 循环数组
# 连续子数组和最大
# [1,2,3,-1,3,2]
# sum
# [1, 2, 3, -4, -2 , 1, 2]
# [1, 2, 3, -1, 3, -4, 2, 3]
a = [13, 22, 3, 1, 4, 15]
heapq.heapify(a)
print(heapq.heappop(a))
print(heapq.heappop(a))
print(heapq.heappop(a))
print(heapq.heappop(a))
print(heapq.heappop(a))
print(heapq.heappop(a))


##########
# round2 #
##########

# int array A -> res
# 3sum=0
# [-1,-0, 1] == [1,0,-1]
# [1,1,1,0,0,-1,-1,-2]

class task:
    def solve(self, array: list) -> list:
        array.sort()
        print(array)
        ret = []
        for i, first in enumerate(array[:-2]):
            remain = 0 - first
            p1, p2 = i + 1, len(array) - 1
            while p1 < p2:
                if array[p1] + array[p2] < remain:
                    p1 += 1
                elif array[p1] + array[p2] == remain:
                    if not ret or (ret and ret[-1] != [first, array[p1], array[p2]]):
                        ret.append([first, array[p1], array[p2]])

                    while p1 < p2 and array[p1 + 1] == array[p1]:
                        p1 += 1
                    p1 += 1
                    p2 -= 1
                else:
                    p2 -= 1

        return ret


# t = task()
# print(t.solve([1, 1, 1, 0, 0, 0, 0, -1, -1, -2, 2]))


# array [ai] ai>0 -> 不能由任意一个子集求和的最小正整数
# [1,1,2,6,7,8]-> 1,2,3,4 -> 5

class task2:
    def solve(self, array):
        prevfill = 0
        array.sort()

        # 计算所有子集可能和
        for index in range(len(array)):
            if index == 0:
                if array[index] > 1:
                    return 1
                else:
                    prevfill = 1
            else:
                if prevfill + 1 < array[index]:
                    return prevfill + 1
                else:
                    prevfill = array[index] + prevfill

        return prevfill + 1


t2 = task2()
print(t2.solve([1, 1, 2, 6, 7, 8]))




