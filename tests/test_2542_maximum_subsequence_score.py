import pytest

from solutions.problem_2542_maximum_subsequence_score import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), 12),
        (dict(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1), 30),
        # my checks
        (dict(nums1 = [1], nums2 = [1], k = 1), 1),
        (dict(nums1 = [1, 100], nums2 = [1, 0], k = 1), 1),
        (dict(nums1 = [1, 100], nums2 = [1, 0], k = 2), 0),
        (dict(nums1 = [1, 100, 2], nums2 = [1, 0, 2], k = 2), 3),
        # after wrong
        (dict(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3), 168),
    ],
)
def test_solution(input_data, output):
    assert output == instance.maxScore(**input_data)
