import pytest

from solutions.problem_17_letter_combinations_of_a_phone_number import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(digits = "23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        (dict(digits = ""), []),
        (dict(digits = "2"), ["a","b","c"]),
        # my checks
        (dict(digits = "22"), ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]),
    ],
)
def test_solution(input_data, output):
    assert set(output) == set(instance.letterCombinations(**input_data))
    assert set(output) == set(instance.letterCombinationsDfs(**input_data))
