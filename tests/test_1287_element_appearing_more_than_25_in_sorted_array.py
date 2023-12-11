import pytest

from solutions.problem_1287_element_appearing_more_than_25_in_sorted_array import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,2,2,6,6,6,6,7,10], 6),
        ([1,1], 1),
        # my checks
        ([1, 1, 1], 1),
        ([1, 1, 2, 3, 4, 5, 6], 1),
        ([1, 2, 2, 3, 4, 5, 6], 2),
        ([1, 2, 3, 3, 4, 5, 6], 3),
        ([1, 2, 3, 4, 4, 5, 6], 4),
        ([1, 2, 3, 4, 5, 5, 6], 5),
        ([1, 2, 3, 4, 5, 6, 6], 6),
        ([1, 1, 2, 2, 3, 3, 4, 4, 4], 4),
    ],
)
def test_solution(input_data, output):
    assert output == instance.findSpecialInteger(input_data)
