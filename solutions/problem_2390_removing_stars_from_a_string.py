# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        result = ''
        stars = 0
        for c in s[::-1]:
            if c == '*':
                stars += 1
            else:
                if stars > 0:
                    stars -= 1
                else:
                    result += c
        return result[::-1]