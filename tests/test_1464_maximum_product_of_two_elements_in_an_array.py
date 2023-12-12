import pytest

from solutions.problem_1464_maximum_product_of_two_elements_in_an_array import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        ([3,4,5,2], 12),
        ([1,5,4,5], 16),
        ([1,5,4,5], 16),
        ([3,7], 12),
        # my checks
    ],
)
def test_solution(input, output):
    assert output == instance.maxProduct(input)
