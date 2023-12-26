import pytest

from solutions.problem_1137_n_th_tribonacci_number import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(n = 4), 4),
        (dict(n = 25), 1389537),
        # my checks
        (dict(n = 0), 0),
        (dict(n = 1), 1),
        (dict(n = 2), 1),
        (dict(n = 3), 2),
    ],
)
def test_solution(input_data, output):
    assert output == instance.tribonacci(**input_data)
