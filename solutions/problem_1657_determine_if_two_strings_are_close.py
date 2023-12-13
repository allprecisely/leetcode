# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or (len(word1) == 1 and word1 != word2):
            return False

        word1_dict = defaultdict(int)
        for c in word1:
            word1_dict[c] += 1
        
        word2_dict = defaultdict(int)
        for c in word2:
            word2_dict[c] += 1
        
        if word1_dict.keys() != word2_dict.keys():
            return False
        
        occurances_dict = defaultdict(int)
        for v in word1_dict.values():
            occurances_dict[v] += 1
        
        for v in word2_dict.values():
            occurances_dict[v] -= 1
        
        for v in occurances_dict.values():
            if v != 0:
                return False
        return True
        

        