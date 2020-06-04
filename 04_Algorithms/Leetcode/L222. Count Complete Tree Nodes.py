class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        stack,cnt = [root],1
        while stack:
            tmp = stack.pop(0)
            if tmp.left:
                stack.append(tmp.left)
                cnt += 1
            if tmp.right:
                stack.append(tmp.right)
                cnt += 1
        return cnt