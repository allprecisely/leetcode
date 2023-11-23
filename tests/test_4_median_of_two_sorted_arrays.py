import pytest

from solutions.problem_4_median_of_two_sorted_arrays import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (([1, 3], [2]), 2),
        (([1, 2], [3, 4]), 2.5),
        # my checks
        (([1], []), 1),
        (([1, 1], []), 1),
        (([1, 2], []), 1.5),
        (([1, 2, 3], []), 2),
        (([1, 2, 3, 100], []), 2.5),
        (([], [1]), 1),
        (([1], [1]), 1),
        (([1], [2]), 1.5),
        (([1, 2, 3, 18, 19, 20], [10, 11]), 10.5),
        (([1, 2, 3, 11, 19, 20], [10, 18]), 10.5),
        (([-111, 111], [-20, -10]), -15),
        (([-1], [0]), -0.5),
        # wrong answers
        (([0, 0], [0, 0]), 0),
        (([2], [1, 3, 4, 5, 6]), 3.5),
    ],
)
def test_solution(input, output):
    assert output == instance.findMedianSortedArrays(*input)
