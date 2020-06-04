class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '' or s == ' ':
            return 0
        count,sLen = 0,len(s)
        lastStep = 0
        while s[sLen-1-lastStep] == ' ':
            lastStep += 1
            if lastStep == sLen -1 :
                break
        print(lastStep)

        while not s[sLen-count-1-lastStep] == ' ':
            count += 1
            if count == sLen:
                return count
            
        return count 


sol = Solution()
print(sol.lengthOfLastWord('    a            '))