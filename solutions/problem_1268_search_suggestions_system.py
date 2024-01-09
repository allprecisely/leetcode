# https://leetcode.com/problems/search-suggestions-system/description/
import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            j = bisect.bisect_left(products, searchWord[:i + 1])
            for k in range(3):
                if j + k < len(products) and products[j + k].startswith(searchWord[:i + 1]):
                    result[i].append(products[j + k])
        return result
