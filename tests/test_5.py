import pytest

from solutions.longestPalindrome_5 import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        # my checks
        ("a", "a"),
        ("aa", "aa"),
        ("ab", "a"),
        ("abb", "bb"),
        ("aab", "aa"),
        ("abaa", "aba"),
        ("aaba", "aba"),
        ("aabaa", "aabaa"),
        ("123321", "123321"),
        ("123321", "123321"),
        ("abcbabcb", "bcbabcb"),
        # wrong answers
        ("aaaa", "aaaa"),
    ],
)
def test_solution(input, output):
    assert output == instance.longestPalindrome(input)
