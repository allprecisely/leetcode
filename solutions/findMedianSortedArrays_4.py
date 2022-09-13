# 4. Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = i2 = 0
        len_nums1, len_nums2 = len(nums1), len(nums2)
        num_ammount = len_nums1 + len_nums2
        is_odd = num_ammount % 2
        half = num_ammount // 2 - (not is_odd)
        half_answer = None
        while True:
            if i1 == len_nums1:
                i, nums = i2, nums2
                break
            elif i2 == len_nums2:
                i, nums = i1, nums1
                break

            if nums1[i1] <= nums2[i2]:
                if i1 + i2 >= half:
                    if is_odd:
                        return nums1[i1]
                    if half_answer is not None:
                        return (half_answer + nums1[i1]) / 2
                    half_answer = nums1[i1]
                i1 += 1
            else:
                if i1 + i2 >= half:
                    if is_odd:
                        return nums2[i2]
                    if half_answer is not None:
                        return (half_answer + nums2[i2]) / 2
                    half_answer = nums2[i2]
                i2 += 1

        if i1 + i2 >= half:
            if is_odd:
                return nums[i]
            if half_answer is not None:
                return (half_answer + nums[i]) / 2
        half = abs(len_nums2 - len_nums1) // 2 - (not is_odd)
        return nums[half] if is_odd else (nums[half] + nums[half + 1]) / 2

