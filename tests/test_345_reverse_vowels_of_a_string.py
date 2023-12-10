import pytest

from solutions.problem_345_reverse_vowels_of_a_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ('hello', 'holle'),
        ('leetcode', 'leotcede'),
        # my checks
        ('a', 'a'),
        ('ab', 'ab'),
        ('bc', 'bc'),
        ('aOA', 'AOa'),
        ('aOoA', 'AoOa'),
    ],
)
def test_solution(input_data, output):
    assert output == instance.reverseVowels(input_data)
