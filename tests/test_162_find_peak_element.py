import pytest

from solutions.problem_162_find_peak_element import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(nums = [1,2,3,1]), 2),
        (dict(nums = [1,2,1,3,5,6,4]), 5),
        # my checks
        (dict(nums = [1,2,3]), 2),
        (dict(nums = [3, 2, 1]), 0),
    ],
)
def test_solution(input_data, output):
    assert output == instance.findPeakElement(**input_data)
