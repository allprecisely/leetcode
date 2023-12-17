import pytest

from solutions.problem_1161_maximum_level_sum_of_a_binary_tree import Solution
from utils import list_to_tree

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(root = [1,7,0,7,-8,None,None]), 2),
        (dict(root = [989,None,10250,98693,-89388,None,None,None,-32127]), 2),
        # my checks
        (dict(root = [1]), 1),
        (dict(root = [1, 2]), 2),
        (dict(root = [2, 1, 1, 3]), 3),
        # wrong answers
        (dict(root = [-100,-200,-300,-20,-5,-10,None]), 3),
        (dict(root = [1,1,0,7,-8,-7,9]), 1),
    ],
)
def test_solution(input_data, output):
    input_data['root'] = list_to_tree(input_data['root'])
    assert output == instance.maxLevelSum(**input_data)
