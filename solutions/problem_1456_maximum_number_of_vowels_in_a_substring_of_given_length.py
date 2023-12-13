# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowels_count = 0
        for c in s[:k]:
            if c in vowels:
                vowels_count += 1
        result = vowels_count
        for i, c in enumerate(s[k:]):
            if s[i] in vowels:
                vowels_count -= 1
            if c in vowels:
                vowels_count += 1
                result = max(result, vowels_count)
        return result

