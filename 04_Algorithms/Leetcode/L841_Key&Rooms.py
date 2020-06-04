class Solution:
    def canVisitAllRooms(self, rooms):
        startPoint = 0
        stack = []
        stack.append(startPoint)
        mark = []
        while stack:
            idx = stack.pop()
            # print(idx)
            mark.append(idx)
            for roomidx in rooms[idx]:
                if not roomidx>=len(rooms):
                    if not roomidx in mark:
                        stack.append(roomidx)
        if len(mark) < len(rooms):
            # print(False)
            return False
        else:
            # print(True)
            return True

sol = Solution()
sol.canVisitAllRooms([[1],[2],[3],[]])
sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
sol.canVisitAllRooms([[0]])
sol.canVisitAllRooms([[1],[4,5,3],[1,],[4]])

