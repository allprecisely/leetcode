import pytest

from solutions.problem_1657_determine_if_two_strings_are_close import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(word1 = "abc", word2 = "bca"), True),
        (dict(word1 = "a", word2 = "aa"), False),
        (dict(word1 = "cabbba", word2 = "abbccc"), True),
        # my check
        (dict(word1 = "a", word2 = "b"), False),
        (dict(word1 = "a", word2 = "a"), True),
        (dict(word1 = "ab", word2 = "aa"), False),
        (dict(word1 = "ab", word2 = "ba"), True),
        (dict(word1 = "ab", word2 = "ab"), True),
        (dict(word1 = "aaab", word2 = "aabb"), False),
        (dict(word1 = "aaab", word2 = "bbab"), True),
        (dict(word1 = "xxc", word2 = "aax"), False),
    ],
)
def test_solution(input, output):
    assert output == instance.closeStrings(**input)
