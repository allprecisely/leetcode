# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        return result + word1[i + 1:] + word2[i + 1:]
