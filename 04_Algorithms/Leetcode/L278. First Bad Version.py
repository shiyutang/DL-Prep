# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start,end = 0,n
        while start <end:
        	mid = (start + end)//2
        	if not isBadVersion(mid):
        		start = mid+1
        	else:
        		end = mid
        
        return start
        