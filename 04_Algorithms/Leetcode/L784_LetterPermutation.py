import copy
class Solution:
    def dp(self,s,i):
        if i>len(s)-1:
            self.b.append(s)
            print(s)
        else:
            print('inelse')
            if not s[i].isdigit():
                print('isletter')
                string = copy.deepcopy(s[i])
                if s[i]==string.lower():
                    print("islowerletter")
                    self.dp(s,i+1)
                    self.dp(s[:i]+s[i].upper()+s[i+1:],i+1)
                else:
                    print("isupperletter")
                    self.dp(s,i+1)
                    self.dp(s[:i]+s[i].lower()+s[i+1:],i+1)
            else:
                print("isdigit")
                self.dp(s,i+1)
        return self.b

    def letterCasePermutation(self, S):
        self.b=[]
        result = self.dp(S,0)
        print(result)
        return result

sol = Solution()
sol.letterCasePermutation("a1b2")
