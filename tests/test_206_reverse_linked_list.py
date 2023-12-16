import pytest

from solutions.problem_206_reverse_linked_list import ListNode, Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], []),
        # my checks
        ([1], [1]),

    ],
)
def test_solution(input_data, output):
    head = ListNode(input_data[0]) if input_data else None
    node = head
    for i in input_data[1:]:
        node.next = ListNode(i)
        node = node.next

    result = []
    updated_head = instance.reverseList(head)
    while updated_head:
        result.append(updated_head.val)
        updated_head = updated_head.next
    assert output == result
