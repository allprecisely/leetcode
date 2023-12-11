import pytest

from solutions.problem_605_can_place_flowers import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([1,0,0,0,1], 1), True),
        (([1,0,0,0,1], 2), False),
        # my checks
        (([0], 1), True),
        (([1], 1), False),
        (([1], 0), True),
        (([0, 0], 1), True),
        (([0, 0], 2), False),
        (([0, 0, 0], 2), True),
        (([1, 0, 0], 1), True),
        (([0, 1, 0], 1), False),
    ],
)
def test_solution(input_data, output):
    assert output == instance.canPlaceFlowers(*input_data)
