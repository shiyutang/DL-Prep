## 单调栈stack，通过让栈中元素始终都维持递增，得到
## 数组中某个元素两侧比它小的值

class Solution(object):
    def largestRectangleArea(self, height):
        if height == None:
            return 0
        stack = []
        #添加-1是为了判断是不是进行到了最后一个
        height.append(-1)
        ans = 0
        for i in range(len(height)):
            cur = height[i]
            #如果栈为空或者当前柱比栈顶柱要高，入栈
            if len(stack) == 0 or cur >= height[stack[-1]]:
                stack.append(i)
            else:
            #如果栈不为空并且当前柱比栈顶柱要低，出栈，更新结果。
                while len(stack) != 0 and cur <= height[stack[-1]]:
                    h = height[stack.pop()]
                    left = stack[-1] if len(stack)!=0 else -1
                    right = i 
                    ans = max(ans,h*(right-left-1))
                stack.append(i)
        return ans