import pytest

from solutions.problem_3_longest_substring_without_repeating_characters import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        ('abcabcbb', 3),
        ('abcabcbb', 3),
        ('abcabcbb', 3),
        ('', 0),
        ('a', 1),
        ('abcdefg', 7),
        ('aba', 2),
        # wrong answers
        ('pwwkew', 3),
    ],
)
def test_solution(input, output):
    assert instance.lengthOfLongestSubstring(input) == output
