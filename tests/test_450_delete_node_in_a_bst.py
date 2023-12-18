import pytest

from solutions.problem_450_delete_node_in_a_bst import Solution
from utils import list_to_tree, tree_to_list

instance = Solution()


@pytest.mark.parametrize(
    'input_data,output_data',
    [
        (dict(root = [5,3,6,2,4,None,7], key = 3), [5,4,6,2,None,None,7]),
        (dict(root = [5,3,6,2,4,None,7], key = 0), [5,3,6,2,4,None,7]),
        (dict(root = [], key = 0), []),
        # my checks
        (dict(root = [1], key = 1), []),
        (dict(root = [2,1], key = 1), [2]),
        (dict(root = [2,1], key = 2), [1]),
        (dict(root = [1, None, 2], key = 1), [2]),
        (dict(root = [1, None, 2], key = 2), [1]),
        (dict(root = [2, 1, 3], key = 1), [2, None, 3]),
        (dict(root = [2, 1, 3], key = 2), [3, 1]),
        (dict(root = [2, 1, 3], key = 3), [2, 1]),
        (dict(root = [10, 1, None, None, 2, None, 3, None, 4, None, 5], key = 10), [1, None, 2, None, 3, None, 4, None, 5]),
        # after wrong
        (dict(root = [50,30,70,None,40,60,80], key = 50), [60,30,70,None,40,None,80]),
    ],
)
def test_solution(input_data, output_data):
    input_data['root'] = list_to_tree(input_data['root'])
    assert output_data == tree_to_list(instance.deleteNode(**input_data))

test_solution(dict(root = [50,30,70,None,40,60,80], key = 50), [60,30,70,None,40,None,80])