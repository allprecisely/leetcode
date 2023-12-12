import pytest

from solutions.problem_643_maximum_average_subarray_i import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([1,12,-5,-6,50,3], 4), 12.75),
        (([5], 1), 5),
        # my checks
        (([5, 5], 2), 5),
        (([5, 7], 1), 7),
        (([7, 5], 1), 7),
        (([7, 5, 7], 2), 6),
        (([7, 7, 5], 2), 7),
        (([7, 7, 5], 3), 6.333333333333333),
    ],
)
def test_solution(input_data, output):
    assert output == instance.findMaxAverage(*input_data)
