# https://leetcode.com/problems/guess-number-higher-or-lower/description/

def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            if guess(middle) == 1:
                left = middle + 1
            else:
                right = middle
        return left
