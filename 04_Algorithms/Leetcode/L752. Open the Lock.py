from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        start = '0000'
        deadends = set(deadends)
        if start in deadends:
            return -1

        def neighbors(numstr):
            for i in range(4):
                yield numstr[:i] + str((int(numstr[i]) + 1) % 10) + numstr[i + 1:]
                yield numstr[:i] + str((int(numstr[i]) - 1) % 10) + numstr[i + 1:]

        visited = set(start)
        steps = deque()
        steps.append((start, 0))
        while steps:
            point, cur_step = steps.popleft()
            if point == target:
                return cur_step

            for neighbor in neighbors(point):
                if not neighbor in deadends and not neighbor in visited:
                    # print(neighbor)
                    steps.append((neighbor, cur_step + 1))
                    visited.add(neighbor)
            # print(point, cur_step)

        return -1


# a fast way  不太懂怎么排除 dead 的，如果中间结点在 dead 怎么办？

class Solution:
    def openLock(self, deadends, target):
        def dist(code):
            return sum(min(int(c), 10 - int(c)) for c in code)

        def neighbors(code):
            for i in range(4):
                pre = code[:i]
                x = int(code[i])
                sur = code[i:]
                yield code[:i] + str((x - 1) % 10) + code[i + 1:]
                yield code[:i] + str((x + 1) % 10) + code[i + 1:]

        dead = set(deadends)
        if '0000' in dead or target in dead:
            return -1
        last_moves = set(neighbors(target)) - dead
        if not last_moves:
            return -1
        ans = dist(target)
        for code in last_moves:  # 的确走了lastmove
            if dist(code) < ans:
                return ans
        return ans + 2


sol = Solution()
# deadends, target = ["0201", "0101", "0102", "1212", "2002"], "0202"
# deadends, target = ["8889", "8887", "7888","9888","8788","8988","8878","8898"], "8888"
# deadends, target = ["8889", "8887", "7888","9888","8788","8988","8878","8898"], "0009"
deadends, target = ["0000"], "8888"
res = sol.openLock(deadends, target)
print(res)
