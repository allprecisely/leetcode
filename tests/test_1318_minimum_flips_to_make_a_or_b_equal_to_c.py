import pytest

from solutions.problem_1318_minimum_flips_to_make_a_or_b_equal_to_c import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(a = 2, b = 6, c = 5), 3),
        (dict(a = 4, b = 2, c = 7), 1),
        (dict(a = 1, b = 2, c = 3), 0),
        # my checks
    ],
)
def test_solution(input_data, output):
    assert output == instance.minFlips(**input_data)
