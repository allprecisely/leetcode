import pytest

from solutions.problem_215_kth_largest_element_in_an_array import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(nums = [3,2,1,5,6,4], k = 2), 5),
        (dict(nums = [3,2,3,1,2,4,5,5,6], k = 4), 4),
        # my checks
        (dict(nums = [1], k = 1), 1),
        (dict(nums = [1, 2], k = 2), 1),
        (dict(nums = [1, 2], k = 1), 2),
        (dict(nums = [2, 1], k = 1), 2),
        (dict(nums = [2, 1], k = 2), 1),
        (dict(nums = [1, 2, 3], k = 1), 3),
        (dict(nums = [1, 2, 3], k = 2), 2),
        (dict(nums = [1, 2, 3], k = 3), 1),
        (dict(nums = [1, 1, 2, 2], k = 1), 2),
        (dict(nums = [1, 1, 2, 2], k = 2), 2),
        (dict(nums = [1, 1, 2, 2], k = 3), 1),
    ],
)
def test_solution(input_data, output):
    assert output == instance.findKthLargest(**input_data)
