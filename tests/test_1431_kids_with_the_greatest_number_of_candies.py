import pytest

from solutions.problem_1431_kids_with_the_greatest_number_of_candies import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([2,3,5,1,3], 3), [True,  True,  True,  False,  True]),
        (([4,2,1,1,2], 1), [True, False, False, False, False]),
        (([12,1,12], 10), [True, False, True]),
        # my checks
        (([1, 1, 1], 10), [True, True, True]),
        (([1, 2, 3], 10), [True, True, True]),
        (([1, 2], 1), [True, True]),
        (([1, 3], 1), [False, True]),
    ],
)
def test_solution(input_data, output):
    assert output == instance.kidsWithCandies(*input_data)
