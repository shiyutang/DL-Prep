class Solution:
    def rob(self, root) -> int:
        memoi = {}

        def helper(node, state):  # calculate the max val this node'child can gain
            # print(node, state)
            def util(node, states):
                if node:
                    if (node, state) in memoi:
                        return memoi[(node, state)]

                    val1, val2 = helper(node, 'w'), node.val + helper(node, 'b')
                    tmp = [val1, max(val1, val2)]['w' in states]
                    memoi[(node, state)] = tmp
                    return tmp
                return 0

            res1, res2 = util(node.left, state), util(node.right, state)
            # print('res1, res2,memoi', res1, res2, memoi)

            return res1 + res2

        if root and root.val is not None:   # 0 放在判断也是否定
            return max(helper(root, 'w'), root.val + helper(root, 'b'))
        elif root is None:
            return 0
        else:
            return
