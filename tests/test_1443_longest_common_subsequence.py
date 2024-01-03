import pytest

from solutions.problem_1443_longest_common_subsequence import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(text1 = "abcde", text2 = "ace"), 3),
        (dict(text1 = "abc", text2 = "abc"), 3),
        (dict(text1 = "abc", text2 = "def"), 0),
        # my checks
        (dict(text1 = "a", text2 = "a"), 1),
        (dict(text1 = "a", text2 = "b"), 0),
        (dict(text1 = "aaa", text2 = "a"), 1),
        (dict(text1 = "ab", text2 = "b"), 1),
        (dict(text1 = "b", text2 = "ab"), 1),
        (dict(text1 = "a", text2 = "aaa"), 1),
        (dict(text1 = "abcd", text2 = "bedf"), 2),
        (dict(text1 = "bedf", text2 = "abcd"), 2),
        # after wrong
        (dict(text1 = "ezupkr", text2 = "ubmrapg"), 2),
    ],
)
def test_solution(input, output):
    assert output == instance.longestCommonSubsequence(**input)
