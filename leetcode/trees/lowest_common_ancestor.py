# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return _solution_iterative(root, p, q)


def _solution_recursive(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if _is_between(root, p, q):
        return root
    if root.val > p.val:  # pq are in the left branch
        return _solution_recursive(root.left, p, q)  # pyright: ignore[reportArgumentType] (problem's constraints make this impossible)
    return _solution_recursive(root.right, p, q)  # pyright: ignore[reportArgumentType] (problem's constraints make this impossible)


def _is_between(root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
    return p.val <= root.val <= q.val or p.val >= root.val >= q.val


def _solution_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left  # pyright: ignore[reportAssignmentType] (problem's constraints make this impossible)
        elif root.val < p.val and root.val < q.val:
            root = root.right  # pyright: ignore[reportAssignmentType] (problem's constraints make this impossible)
        else:
            return root
