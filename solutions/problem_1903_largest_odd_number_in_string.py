# https://leetcode.com/problems/largest-odd-number-in-string/description/
# 1 try

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = {'1', '3', '5', '7', '9'}
        for i in range(len(num) - 1, -1, -1):
            if num[i] in odds:
                return num[:i + 1]
        return ''
