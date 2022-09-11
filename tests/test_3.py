import pytest

from solutions.lengthOfLongestSubstring_3 import Solution

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
