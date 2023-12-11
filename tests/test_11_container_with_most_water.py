import pytest

from solutions.problem_11_container_with_most_water import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        # my checks
        ([1,100], 1),
        ([5,100, 20, 5], 20),
        ([1, 2, 3, 4, 5, 6], 9),

    ],
)
def test_solution(input_data, output):
    assert output == instance.maxArea(input_data)
