import pytest

from leetcode.trees.lowest_common_ancestor import Solution, TreeNode


@pytest.mark.parametrize(
    ("vals", "p", "q", "expected"),
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ],
)
def test_lowest_common_ancestor(vals: list[int | None], p: int, q: int, expected: int) -> None:
    root, pp, qq = _build_node(vals), _build_node([p]), _build_node([q])
    assert root
    assert pp
    assert qq

    res = Solution().lowestCommonAncestor(root, pp, qq)
    assert res.val == expected


def _build_node(vals: list[int | None], i: int = 0) -> TreeNode | None:
    if not vals:
        raise ValueError("Empty vals")
    if not i < len(vals):
        raise IndexError("Index out of range")

    v = vals[i]
    if v is None:
        return None

    node = TreeNode(x=v)
    left = ((i + 1) * 2) - 1
    right = left + 1
    if left < len(vals) and vals[left] is not None:
        node.left = _build_node(vals, left)
    if right < len(vals) and vals[right] is not None:
        node.right = _build_node(vals, right)

    return node
