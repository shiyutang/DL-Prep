# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers: list):
        if not numbers:
            return ''
        
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'

            class K:
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0

                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0

                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0

                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0

                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0

            return K

        def helper(a, b):
            return int(str(a) + str(b)) - int(str(b) + str(a))

        numbers.sort(key=cmp_to_key(helper))
        print(numbers)
        ret = ''
        for num in map(str, numbers):
            ret += num
        return int(ret)




sol = Solution()
print(sol.PrintMinNumber([3, 32, 321]))
