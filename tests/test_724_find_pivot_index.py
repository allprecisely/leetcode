import pytest

from solutions.problem_724_find_pivot_index import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(nums = [1,7,3,6,5,6]), 3),
        (dict(nums = [1,2,3]), -1),
        (dict(nums = [2,1,-1]), 0),
        #dict(num =  my check)s
        (dict(nums = [0]), 0),
        (dict(nums = [10]), 0),
        (dict(nums = [2, 2]), -1),
        (dict(nums = [2, 0]), 0),
        (dict(nums = [0, 1]), 1),
        (dict(nums = [5, 5, 5]), 1),
        (dict(nums = [5, 5, 5, 5]), -1),
        (dict(nums = [10, 0, 0, 0, 0]), 0),
        (dict(nums = [0, 0, 0, 0, 10]), 4),
    ],
)
def test_solution(input, output):
    assert output == instance.pivotIndex(**input)
