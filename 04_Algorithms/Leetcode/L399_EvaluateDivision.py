import copy
class Solution:
    def calcEquation(self, equations, values, queries):
        node = {}
        flag = 0
        equa = copy.deepcopy(equations)
        val = copy.deepcopy(values)
        i = 0
        equalen = len(equa)
        while equa:
            if i>=len(equa):
                i = 0
                if len(equa) == equalen:
                    break
                equalen = len(equa)
            # if len(equa[i][0])>1:

            if (not equa[i][0] in node) and (not equa[i][1] in node) and not node.keys():
                node[equa[i][1]] = 1, flag
                node[equa[i][0]] = values[i], flag
                val.pop(equa.index(equa[i]))
                equa.remove(equa[i])
                continue
            elif (not equa[i][0] in node) and (not equa[i][1] in node):
                i += 1
                continue
            elif not equa[i][0] in node:
                node[equa[i][0]] = node[equa[i][1]][0]*val[i],node[equa[i][1]][1]
                val.pop(equa.index(equa[i]))
                equa.remove(equa[i])
                continue
            elif not equa[i][1] in node:
                node[equa[i][1]] = node[equa[i][0]][0]/val[i],node[equa[i][0]][1]
                val.pop(equa.index(equa[i]))
                equa.remove(equa[i])
                continue

        if (not equations[i][0] in node) and (not equations[i][1] in node):
            flag += 1
            node[equations[i][1]] = 1,flag
            node[equations[i][0]] = values[i],flag
        res = []
        for j in range(len(queries)):
            if (not node.__contains__(queries[j][0])) or (not node.__contains__(queries[j][1])):
                res.append(-1.0)
            else:
                if node[queries[j][0]][1] != node[queries[j][1]][1]:
                    res.append(-1.0)
                else:
                    res.append(node[queries[j][0]][0]/node[queries[j][1]][0])
        return res


sol = Solution()
# res = sol.calcEquation([["a","b"],["b","c"]],[2.0,3.0],
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
# print(res)
# res = sol.calcEquation([["a","b"],["c","b"],["f","g"]],[2.0,3.0,3.9],
# [["a","c"],["b","a"],["a","e"],["a","f"],["f","g"]])
# print(res)
res = sol.calcEquation(
[["a","b"],["e","f"],["b","e"]],
[3.4,1.4,2.3],
[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]])
print(res)