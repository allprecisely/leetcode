import pytest

from solutions.problem_199_binary_tree_right_side_view import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(root = [1,2,3,None,5,None,4]), [1,3,4]),
        (dict(root = [1,None,3]), [1,3]),
        (dict(root = []), []),
        # my checks
        (dict(root = [1]), [1]),
        (dict(root = [1,2]), [1,2]),
        (dict(root = [1,2,None,3]), [1,2,3]),
    ],
)
def test_solution(input_data, output):
    input_data['root'] = list_to_tree(input_data['root'])
    assert output == instance.rightSideView(**input_data)
    assert output == instance.rightSideViewRecursive(**input_data)
