import pytest

from solutions.problem_1448_count_good_nodes_in_binary_tree import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([3,1,4,3,None,1,5], 4),
        ([3,3,None,4,2], 3),
        ([1], 1),
        # my checks
        ([1, 1, 1, 1, 1, 1, 1], 7),
    ],
)
def test_solution(input_data, output):
    assert output == instance.goodNodes(list_to_tree(input_data))
