# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin(c := (a | b) ^ c).count('1') + bin(a & b & c).count('1')