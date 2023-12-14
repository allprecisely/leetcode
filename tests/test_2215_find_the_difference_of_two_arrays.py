import pytest

from solutions.problem_2215_find_the_difference_of_two_arrays import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(nums1 = [1,2,3], nums2 = [2,4,6]), [[1,3],[4,6]]),
        (dict(nums1 = [1,2,3,3], nums2 = [1,1,2,2]), [[3],[]]),
        # my checks
        (dict(nums1 = [1], nums2 = [1]), [[],[]]),
        (dict(nums1 = [1], nums2 = [2]), [[1],[2]]),
        (dict(nums1 = [1, 2], nums2 = [2, 1]), [[],[]]),
        (dict(nums1 = [-1, -2, -1, -2], nums2 = [-2, -2, -1, -1]), [[],[]]),
    ],
)
def test_solution(input, output):
    assert output == instance.findDifference(**input)
