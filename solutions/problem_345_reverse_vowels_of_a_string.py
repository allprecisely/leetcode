# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left_index, right_index = 0, len(s) - 1
        while left_index < right_index:
            while left_index < right_index and s[left_index] not in vowels:
                left_index += 1
            while left_index < right_index and s[right_index] not in vowels:
                right_index -= 1
            list_s[left_index], list_s[right_index] = s[right_index], s[left_index]
            left_index += 1
            right_index -= 1
        return ''.join(list_s)
