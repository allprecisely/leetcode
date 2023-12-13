import pytest

from solutions.problem_1493_longest_subarray_of_1s_after_deleting_one_element import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(nums = [1,1,0,1]), 3),
        (dict(nums = [0,1,1,1,0,1,1,0,1]), 5),
        (dict(nums = [1,1,1]), 2),
        # my checks
        (dict(nums = [0]), 0),
        (dict(nums = [1]), 0),
        (dict(nums = [0, 0]), 0),
        (dict(nums = [0, 1]), 1),
        (dict(nums = [1, 0]), 1),
        (dict(nums = [1, 1]), 1),
        (dict(nums = [0, 1, 0]), 1),
        (dict(nums = [1, 0, 1]), 2),
        (dict(nums = [1, 1, 0]), 2),
    ],
)
def test_solution(input, output):
    assert output == instance.longestSubarray(**input)
