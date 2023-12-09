import pytest

from solutions.problem_94_binary_tree_inorder_traversal import Solution, TreeNode

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 3, 2]),
        (None, []),
        (TreeNode(1), [1]),
        # my checks
        (TreeNode(1, TreeNode(2)), [2, 1]),
        (TreeNode(1, None, TreeNode(2)), [1, 2]),
        (TreeNode(1, TreeNode(2), TreeNode(3)), [2, 1, 3]),
        (TreeNode(1, TreeNode(2, TreeNode(3))), [3, 2, 1]),
        (TreeNode(1, TreeNode(2, None, TreeNode(3))), [2, 3, 1]),
        (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [1, 2, 3]),
        (
            TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7))),
            [3, 2, 4, 1, 6, 5, 7],
        ),
    ],
)
def test_solution(input, output):
    assert output == instance.inorderTraversal(input)
