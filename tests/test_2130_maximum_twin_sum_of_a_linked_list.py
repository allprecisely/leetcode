import pytest

from solutions.problem_2130_maximum_twin_sum_of_a_linked_list import ListNode, Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([5,4,2,1], 6),
        ([4,2,2,3], 7),
        ([1,100000], 100001),
        # my checks
    ],
)
def test_solution(input_data, output):
    head = ListNode(input_data[0]) if input_data else None
    node = head
    for i in input_data[1:]:
        node.next = ListNode(i)
        node = node.next

    assert output == instance.pairSum(head)
