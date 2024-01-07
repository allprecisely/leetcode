import pytest

from solutions.problem_338_counting_bits import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(n = 2), [0,1,1]),
        (dict(n = 5), [0,1,1,2,1,2]),
        # my checks
        (dict(n = 6), [0,1,1,2,1,2,2]),
        (dict(n = 7), [0,1,1,2,1,2,2,3]),
        (dict(n = 0), [0]),
        (dict(n = 1), [0, 1]),
    ],
)
def test_solution(input_data, output):
    assert output == instance.countBits(**input_data)
