class Solution:
    def isPalindrome(self, x) :
    	if x<0:
    		return False
    	else:
    		x = str(x)
    		xlen = len(x) 
    		print(xlen)
    		stop = xlen//2
    		for i in range(stop):
    			if x[i] != x[-(1+i)]:
    				return False
    		return True

# palindrome is the one same as the it reverse self
class Solution:
    def isPalindrome(self, x) :
        if x<0:
            return False
        else:
            x = str(x)
            return x == x[::-1]



sol = Solution()
res = sol.isPalindrome(122222222222222222222222222222222222222222221)
# res = sol.isPalindrome(123)
print(res)