import pytest

from solutions.problem_2095_delete_the_middle_node_of_a_linked_list import ListNode, Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([1,3,4,7,1,2,6], [1,3,4,1,2,6]),
        ([1,2,3,4], [1,2,4]),
        ([2,1], [2]),
        # my checks
        ([1], []),
    ],
)
def test_solution(input_data, output):
    head = ListNode(input_data[0])
    node = head
    for i in input_data[1:]:
        node.next = ListNode(i)
        node = node.next

    updated_head = instance.deleteMiddle(head)
    for i in output:
        assert i == updated_head.val
        updated_head = updated_head.next
    
    if not output:
        assert updated_head == None