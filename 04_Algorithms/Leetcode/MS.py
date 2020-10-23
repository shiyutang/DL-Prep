# A -> B -> C -> D -> E
# N = 2
#
# A -> B -> D -> C -> E
import heapq


class task:
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



