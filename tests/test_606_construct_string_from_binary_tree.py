import pytest

from solutions.problem_606_construct_string_from_binary_tree import Solution, TreeNode

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), '1(2(4))(3)'),
        (TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), '1(2()(4))(3)'),
        # my checks
        (TreeNode(1, None, None), '1'),
        (TreeNode(1, TreeNode(2), None), '1(2)'),
        (TreeNode(1, None, TreeNode(2)), '1()(2)'),
        (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), '1()(2()(3))'),
    ],
)
def test_solution(input, output):
    assert output == instance.tree2str(input)
