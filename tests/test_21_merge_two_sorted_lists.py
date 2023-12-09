import pytest

from solutions.problem_21_merge_two_sorted_lists import ListNode, Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([1,2,4], [1,3,4]), [1,1,2,3,4,4]),
        (([], []), []),
        (([], [0]), [0]),
        # my checks
        (([0], []), [0]),
        (([-100], [-50]), [-100, -50]),
        (([1, 2, 3, 4], [5]), [1, 2, 3, 4, 5]),
        (([1, 2, 3, 4], [-5]), [-5, 1, 2, 3, 4]),

    ],
)
def test_solution(input_data, output):
    first_head = ListNode(input_data[0][0]) if input_data[0] else None
    second_head = ListNode(input_data[1][0]) if input_data[1] else None
    first_next, second_next = first_head, second_head
    for i in input_data[0][1:]:
        first_next.next = ListNode(i)
        first_next = first_next.next
    for i in input_data[1][1:]:
        second_next.next = ListNode(i)
        second_next = second_next.next

    node = instance.mergeTwoLists(first_head, second_head)
    answer_list = []
    while node:
        answer_list.append(node.val)
        node = node.next

    assert answer_list == output
