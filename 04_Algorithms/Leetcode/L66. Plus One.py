class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1] += 1
        else:
            ca,pos = 1,1
            while ca == 1:
                digits[-pos] = 0
                if pos == len(digits):
                    digits.insert(0,1)
                    break
                if not digits[-(pos+1)] == 9:
                    ca = 0
                    digits[-(pos+1)] += 1
                else:
                    pos+=1
        return digits
        