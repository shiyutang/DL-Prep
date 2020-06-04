class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:#后面是不是比前面小
                h = height[stack.pop()] #小的话就拿出前面的高度，乘以累计几个高
                w = i - stack[-1] - 1
                print(h*w)
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

def test():
    sol = Solution()
    res = sol.largestRectangleArea([2,1,5,6,2,3])
    print(res)

    sol = Solution()
    res = sol.largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0])
    print(res)

test()
