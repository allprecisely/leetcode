import pytest

from solutions.problem_1456_maximum_number_of_vowels_in_a_substring_of_given_length import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(s = "abciiidef", k = 3), 3),
        (dict(s = "aeiou", k = 2), 2),
        (dict(s = "leetcode", k = 3), 2),
        # my checks
        (dict(s = "a", k = 1), 1),
        (dict(s = "a", k = 3), 1),
        (dict(s = "aaa", k = 1), 1),
        (dict(s = "aaa", k = 2), 2),
        (dict(s = "aaa", k = 3), 3),
        (dict(s = "aaa", k = 5), 3),
        (dict(s = "b", k = 1), 0),
        (dict(s = "abejajajajajaja", k = 2), 1),

    ],
)
def test_solution(input_data, output):
    assert output == instance.maxVowels(**input_data)
