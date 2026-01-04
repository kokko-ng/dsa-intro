"""
Linked List helper classes and utilities.
"""
from typing import Optional, List


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        # Compare entire list
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Create a linked list from a list of values.

    Args:
        values: List of integers

    Returns:
        Head of the linked list, or None if empty

    Example:
        >>> head = create_linked_list([1, 2, 3])
        >>> head.val
        1
        >>> head.next.val
        2
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert linked list to Python list.

    Args:
        head: Head of the linked list

    Returns:
        List of values

    Example:
        >>> head = create_linked_list([1, 2, 3])
        >>> linked_list_to_list(head)
        [1, 2, 3]
    """
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def create_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    """
    Create a cycle in the linked list at the given position.

    Args:
        head: Head of the linked list
        pos: Position where the cycle starts (0-indexed), -1 for no cycle

    Returns:
        Head of the linked list (possibly with cycle)
    """
    if not head or pos < 0:
        return head

    # Find the tail and the node at position pos
    cycle_node = None
    current = head
    index = 0
    tail = None

    while current:
        if index == pos:
            cycle_node = current
        if current.next is None:
            tail = current
        current = current.next
        index += 1

    # Create the cycle
    if tail and cycle_node:
        tail.next = cycle_node

    return head
