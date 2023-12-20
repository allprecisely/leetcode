# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_potions = sorted(potions)
        return [len(potions) - bisect_left(sorted_potions, success/ spell) for spell in spells]
        
            
        