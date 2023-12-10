import pytest

from solutions.problem_238_product_of_array_except_self import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        # my checks
        ([1, 2], [2, 1]),
        ([0, 0, 10, 20, 30, 40], [0, 0, 0, 0, 0, 0]),
        ([2, 2], [2, 2]),
    ],
)
def test_solution(input_data, output):
    assert instance.productExceptSelf(input_data) == output
