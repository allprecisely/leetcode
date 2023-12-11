# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
# 1 try; slightly improved

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr_len = len(arr)

        def binary_search(target: int, last_occurence: bool) -> int:
            left, right = -1, arr_len
            while left + 1 < right:
                middle = (right + left) // 2
                if target > arr[middle] or (last_occurence and target == arr[middle]):
                    left = middle
                else:
                    right = middle
            return left if last_occurence else right

        quarter_length = arr_len // 4
        if arr[0] == arr[quarter_length]:
            return arr[0]
        for el_index in range(quarter_length + 1, arr_len, quarter_length + 1):
            el = arr[el_index]
            if binary_search(el, True) - binary_search(el, False) >= quarter_length:
                return el
