class Solution:
    def fix(self, damages, actions):
        # for each non-overlap damage: find the suitable match, for each catch, remove
        damages = self.removeOL(damages)
        cost = [[] for _ in range(min(2,len(damages)))]  # (end, totalcost)
        idx = 0

        if damages[0][0] < actions[0][0]:
            return -1

        act = actions.pop(0)
        while idx < len(damages):
            while act[0] <= damages[idx][0]:
                if idx == 0:
                    cost[0].append((act[1], act[2]))
                else:
                    save = (None, float('inf'))
                    for a in cost[0]:
                        if act[0] < a[0] and act[2] + a[1] < save[1]:
                            save = (act[1], act[2] + a[1])
                    cost[1].append(save)
                act = actions.pop(0)
            else:
                if idx != 0:
                    cost[0], cost[1] = cost[1], []
                idx += 1
        else:
            while actions or act:
                save = (None, float('inf'))
                for a in cost[0]:
                    if act[0] < a[0] and act[2] + a[1] < save[1]:
                        save = (act[1], act[2] + a[1])
                cost[1].append(save)
                act = actions.pop(0)


        minres = float('inf')
        for ele in cost[0]:
            minres = min(ele[1],minres)

        return -1 if minres == float('inf') else minres

    def removeOL(self, array):
        # remove overlap
        i = 0
        while i < len(array):
            if i == 0:
                i += 1
                continue
            else:
                if array[i][0] > array[i - 1][1]:
                    i += 1
                else:
                    maxR = max(array[i][1], array[i - 1][1])
                    array.pop(i)
                    array[i - 1][1] = maxR
        return array


N, M, S = list(map(int, input().split(' ')))
damages = []
for _ in range(N):
    damages.append(list(map(int, input().split(' '))))
damages.sort(key=lambda x: (x[0], x[1]))

# collect SP actions and sort
actions = []
for _ in range(M):
    actions.append(list(map(int, input().split(' '))))
actions.sort(key=lambda x: (x[0], x[1]))

sol = Solution()
print(sol.fix(damages, actions))
