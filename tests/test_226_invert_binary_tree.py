import pytest

from solutions.problem_226_invert_binary_tree import Solution
from utils import list_to_tree, tree_to_list

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2,1,3], [2,3,1]),
        ([], []),
        # my checks
        ([1], [1]),
        # ([1, 2], [1, 2]),
    ],
)
def test_solution(input_data, output):
    assert output == tree_to_list(instance.invertTree(list_to_tree(input_data)))
