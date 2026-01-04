"""
Tree helper classes and utilities.
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        # Compare trees recursively
        if self.val != other.val:
            return False
        left_eq = (self.left == other.left) if (self.left or other.left) else True
        right_eq = (self.right == other.right) if (self.right or other.right) else True
        return left_eq and right_eq


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

        # Right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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

    result = []
    queue = deque([root])

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


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Return inorder traversal of tree."""
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Return preorder traversal of tree."""
    result = []

    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Return postorder traversal of tree."""
    result = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

    postorder(root)
    return result
