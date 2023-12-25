# https://leetcode.com/problems/combination-sum-iii/description/

from typing import List, Tuple


class Solution:
    def combinationSum3(self, k: int, n: int, used: Tuple[int, ...] = ()) -> List[List[int]]:
        if k == 1:
            return [[n]] if n < 10 and n not in used else []
        
        result = []
        for i in [j for j in range(1, 10) if j not in used and n - j > 0]:
            used += (i,) 
            for combination in self.combinationSum3(k - 1, n - i, used):
                result.append(combination + [i])

        return result
                

        
