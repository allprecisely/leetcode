# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        combinations = list(letters[digits[0]]) if digits else []
        for digit in digits[1:]:
            new_combinations = []
            for combination in combinations:
                new_combinations += [combination + letter for letter in letters[digit]]
            combinations = new_combinations
        return combinations

    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinationsDfs(self, digits: str) -> List[str]:
        if len(digits) <= 1:
            return list(self.letters[digits]) if digits else []
        return [
            path + letter 
            for path in self.letterCombinationsDfs(digits[:-1]) 
            for letter in self.letters[digits[-1]]
        ]
