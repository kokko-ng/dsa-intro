"""
Tree helper classes and utilities.
"""
from __future__ import annotations

from collections import deque


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return False
        # Compare trees recursively
        if self.val != other.val:
            return False
        left_eq = (self.left == other.left) if (self.left or other.left) else True
        right_eq = (self.right == other.right) if (self.right or other.right) else True
        return left_eq and right_eq


def build_tree(values: list[int | None]) -> TreeNode | None:
    """
    Build binary tree from level-order array representation.
    None represents missing nodes.

    Args:
        values: List of integers (None for missing nodes)

    Returns:
        Root of the binary tree, or None if empty

    Example:
        >>> root = build_tree([1, 2, 3, None, 4])
        >>> root.val
        1
        >>> root.left.val
        2
        >>> root.right.val
        3
        >>> root.left.right.val
        4
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values):
            val = values[i]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            i += 1

        # Right child
        if i < len(values):
            val = values[i]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            i += 1

    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """
    Convert tree to level-order array representation.

    Args:
        root: Root of the binary tree

    Returns:
        List of values in level-order (None for missing nodes)

    Example:
        >>> root = build_tree([1, 2, 3, None, 4])
        >>> tree_to_list(root)
        [1, 2, 3, None, 4]
    """
    if not root:
        return []

    result: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result


def inorder_traversal(root: TreeNode | None) -> list[int]:
    """Return inorder traversal of tree."""
    result: list[int] = []

    def inorder(node: TreeNode | None) -> None:
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


def preorder_traversal(root: TreeNode | None) -> list[int]:
    """Return preorder traversal of tree."""
    result: list[int] = []

    def preorder(node: TreeNode | None) -> None:
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result


def postorder_traversal(root: TreeNode | None) -> list[int]:
    """Return postorder traversal of tree."""
    result: list[int] = []

    def postorder(node: TreeNode | None) -> None:
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

    postorder(root)
    return result
