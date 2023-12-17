import pytest

from solutions.problem_1372_longest_zigzag_path_in_a_binary_tree import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1], 3),
        ([1,1,1,None,1,None,None,1,1,None,1], 4),
        ([1], 0),
        # my checks
        ([1, 1, None, 1, None, 1, None], 1),
        ([1, 1, 1, 1, None, None, None, 1, 1], 2),
    ],
)
def test_solution(input_data, output):
    assert output == instance.longestZigZag(list_to_tree(input_data))

