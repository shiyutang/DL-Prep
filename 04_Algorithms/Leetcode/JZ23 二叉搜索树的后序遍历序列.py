# -*- coding:utf-8 -*-
class Solution1:
    def VerifySquenceOfBST(self, sequence):
        def helper(seq):
            if 0 < len(seq) < 2:
                return True
            elif len(seq) == 0:
                return False
            else:
                pivot = seq[-1]
                place = -1
                small, big = False, False
                for idx, num in enumerate(seq[:-1]):
                    if num < pivot:
                        idx += 1
                        if big:
                            return False
                    elif num > pivot:
                        if place == -1:
                            place = idx
                        big = True
                    else:
                        return False

            return helper(seq[:place]) and helper(seq[place:-1])

        return helper(sequence)


# -*- coding:utf-8 -*-
# 根据跟左右分成左右两部分呢，只要右边都大于跟就可以
class Solution:
    def VerifySquenceOfBST(self, sequence):
        def helper(seq):
            if 0 <= len(seq) < 2:
                return True
            pivot = seq[-1]
            place = len(seq) - 1
            for idx, num in enumerate(seq[:-1]):
                if num > pivot:
                    place = idx
                    break
                elif num == pivot:
                    return False

            for num in seq[place:-1]:
                if num <= pivot:
                    return False

            return helper(seq[:place]) and helper(seq[place:-1])

        if not sequence:
            return False
        return helper(sequence)


sol = Solution()
print(sol.VerifySquenceOfBST([4, 7, 5, 12, 10]))
print(sol.VerifySquenceOfBST([4, 9, 3, 12, 10]))
print(sol.VerifySquenceOfBST([4, 8, 6, 12, 16, 14, 10]))
print(sol.VerifySquenceOfBST([5, 4, 3, 2, 1]))
