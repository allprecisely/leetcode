# https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.values()) == len(set(counter.values()))
        