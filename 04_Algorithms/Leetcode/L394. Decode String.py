class Solution:
    def decodeString(self, s: str) -> str:
        cnt = 0
        stack = []
        res = ''
        for c in s:
            if c.isdigit():
                cnt = cnt * 10 + int(c)
            elif c == '[':
                stack.append((cnt, res))
                cnt = 0
                res = ''
            elif c == ']':
                cur_cnt, last_res = stack.pop()
                res = last_res + cur_cnt * res

            else:
                res += c

        return res

# 使用栈来取代递归可以节省很多复杂的参数传输和位置计算等，只要过一遍就可以得到结果
class Solution:
    def decodeString(self, s: str) -> str:
        num = ''
        str_in = ''
        stack = []

        for idx in range(len(s)):
            if s[idx].isdigit():
                num += s[idx]

            elif s[idx] == '[':
                stack.append((num, str_in))
                num, str_in = '', ''

            elif s[idx] == ']':
                prevnum, prev_str = stack.pop()

                str_in = prev_str + str_in * int(prevnum)
                num = ''

            else:
                str_in += s[idx]
            # print('s[idx],idx, num', s[idx], idx, num)
            # print('str_in', str_in)

        return str_in


# test
def test(method):
    sol = method()
    # s = "2[abc]3[cd]ef"
    s = "3[a]2[bc]"
    # s = "abc3[cd]xyz"
    s = "a2[bc3[c2[d]]xy]z"
    # s = ''
    print(s, end=' ')
    res = sol.decodeString(s)
    print(' and the res is ', res)


test(Solution)
