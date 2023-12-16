import pytest

from solutions.problem_328_odd_even_linked_list import ListNode, Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,2,3,4,5], [1,3,5,2,4]),
        ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]),
        # my checks
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
    ],
)
def test_solution(input_data, output):
    head = ListNode(input_data[0]) if input_data else None
    node = head
    for i in input_data[1:]:
        node.next = ListNode(i)
        node = node.next

    result = []
    updated_head = instance.oddEvenList(head)
    while updated_head:
        result.append(updated_head.val)
        updated_head = updated_head.next
    assert output == result