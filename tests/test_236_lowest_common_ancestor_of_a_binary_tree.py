import pytest

from solutions.problem_236_lowest_common_ancestor_of_a_binary_tree import Solution
from utils import find_node, list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1), 3),
        (dict(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4), 5),
        (dict(root = [1,2], p = 1, q = 2), 1),
        # my checks
        (dict(root = [1,2,3], p = 1, q = 3), 1),
        (dict(root = [1,2,3], p = 2, q = 3), 1),
        (dict(root = [1,2,3,4,None,None,5], p = 4, q = 5), 1),
    ],
)
def test_solution(input_data, output):
    input_data['root'] = list_to_tree(input_data['root'])
    input_data['p'] = find_node(input_data['root'], input_data['p'])
    input_data['q'] = find_node(input_data['root'], input_data['q'])
    assert output == instance.lowestCommonAncestor(**input_data).val
