import pytest

from solutions.problem_700_search_in_a_binary_search_tree import Solution
from utils import find_node, list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data',
    [
        (dict(root = [4,2,7,1,3], val = 2)),
        (dict(root = [4,2,7,1,3], val = 5)),
        # my checks
        (dict(root = [1], val = 1)),
        (dict(root = [1], val = 2)),
        (dict(root = [1,None,2], val = 2)),
        (dict(root = [1,None,2], val = 1)),
    ],
)
def test_solution(input_data):
    input_data['root'] = list_to_tree(input_data['root'])
    node_to_find = find_node(input_data['root'], input_data['val'])
    assert node_to_find == instance.searchBST(**input_data)
