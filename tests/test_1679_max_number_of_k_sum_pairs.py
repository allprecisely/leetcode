import pytest

from solutions.problem_1679_max_number_of_k_sum_pairs import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([1,2,3,4], 5), 2),
        (([3,1,3,4,3], 6), 1),
        # my checks
        (([1], 1), 0),
        (([1], 2), 0),
        (([1, 1], 1), 0),
        (([3, 4], 2), 0),
        (([1, 1, 1, 2], 2), 1),
        (([1, 1, 1, 2], 3), 1),
        (([1, 1, 1, 2], 4), 0),
        # after wrong
        (([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3), 4)
    ],
)
def test_solution(input_data, output):
    assert output == instance.maxOperations(*input_data)
