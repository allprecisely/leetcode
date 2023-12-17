import pytest

from solutions.problem_104_maximum_depth_of_binary_tree import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2),
        # my checks
        ([], 0),
        ([1], 1),
        ([1,1,None,1,None,1], 4),
    ],
)
def test_solution(input_data, output):
    assert output == instance.maxDepth(list_to_tree(input_data))
    assert output == instance.maxDepthIterable(list_to_tree(input_data))
