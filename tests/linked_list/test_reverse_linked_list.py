import pytest

from leetcode.linked_list.reverse_linked_list import ListNode, Solution


@pytest.mark.parametrize(
    ("head", "expected"),
    [  # pyright: ignore[reportUnknownArgumentType]
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_linked_list(head: list[int], expected: list[int]) -> None:
    node_in, node_out = _build_linked_list(head), _build_linked_list(expected)
    res = Solution().reverseList(node_in)
    if res is None or node_out is None:
        assert res is None
        assert node_out is None
    else:
        assert res.val == node_out.val


def _build_linked_list(head: list[int]) -> ListNode | None:
    if not head:
        return None
    nodes: list[ListNode] = []
    for val in reversed(head):
        nodes.append(ListNode(val=val, next=nodes[-1] if nodes else None))
    return nodes[-1]
