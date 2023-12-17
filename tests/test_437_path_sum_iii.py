import pytest

from solutions.problem_437_path_sum_iii import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([10,5,-3,3,2,None,11,3,-2,None,1], 8), 3),
        (([5,4,8,11,None,13,4,7,2,None,None,5,1], 22), 3),
        # my checks
        (([], 8), 0),
        (([], 0), 0),
        (([0], 8), 0),
        (([8], 8), 1),
        (([8, 8], 8), 2),
        (([8, 8, 8], 8), 3),
        (([4, 4, 4], 8), 2),
        (([8, -8, None, 8], 8), 3),
    ],
)
def test_solution(input_data, output):
    assert output == instance.pathSum(list_to_tree(input_data[0]), input_data[1])
