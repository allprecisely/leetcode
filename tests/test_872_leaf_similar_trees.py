import pytest

from solutions.problem_872_leaf_similar_trees import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]), True),
        (([1,2,3], [1,3,2]), False),
        # my checks
        (([1], [1]), True),
        (([1], [2]), False),
        (([1, 2, 3], [1, 2, 3]), True),
        (([1, 2, None, 3], [3, None, 1, None, None, 3]), True),
        # after wrong
        (
            (
                [3,5,1,6,7,4,2,None,None,None,None,None,None,9,11,None,None,8,10],
                [3,5,1,6,2,9,8,None,None,7,4],
            ),
            False,
        )
    ],
)
def test_solution(input_data, output):
    assert output == instance.leafSimilar(list_to_tree(input_data[0]), list_to_tree(input_data[1]))
