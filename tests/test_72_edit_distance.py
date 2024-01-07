import pytest

from solutions.problem_72_edit_distance import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(word1 = "horse", word2 = "ros"), 3),
        (dict(word1 = "intention", word2 = "execution"), 5),
        # my checks
        (dict(word1 = "", word2 = ""), 0),
        (dict(word1 = "a", word2 = ""), 1),
        (dict(word1 = "ab", word2 = ""), 2),
        (dict(word1 = "", word2 = "a"), 1),
        (dict(word1 = "", word2 = "ab"), 2),
        (dict(word1 = "ab", word2 = "ab"), 0),
        (dict(word1 = "a", word2 = "a"), 0),
        (dict(word1 = "a", word2 = "aaa"), 2),
        (dict(word1 = "aaa", word2 = "a"), 2),
        (dict(word1 = "ba", word2 = "ab"), 2),
        (dict(word1 = "abba", word2 = "baab"), 3),
        # after wrong
        (dict(word1 = "ate", word2 = "sea"), 3),
        (dict(word1 = "sea", word2 = "ate"), 3),

    ],
)
def test_solution(input_data, output):
    assert output == instance.minDistance(**input_data)
