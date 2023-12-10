import pytest

from solutions.problem_334_increasing_triplet_subsequence import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
        # my checks
        ([1], False),
        ([1, 2], False),
        ([1, 2, 3], True),
        ([1, 2, 2], False),
        ([10, 20, 5, 30, 25], True),
        ([10, 20, 5, 15, 12], False),
        # after wrong
        ([1,1,-2,6], False),
        # after 2nd wrong
        ([0, -1, 0, 2], True),
    ],
)
def test_solution(input_data, output):
    assert instance.increasingTriplet(input_data) == output
