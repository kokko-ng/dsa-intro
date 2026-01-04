"""
Tests for Topic 05: Linked Lists
"""
import pytest
from conftest import get_solution, create_linked_list, linked_list_to_list, create_cycle


class TestReverseList:
    def test_reverse_basic(self):
        f = get_solution("reverse_list")
        head = create_linked_list([1, 2, 3, 4, 5])
        result = f(head)
        assert linked_list_to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_edge_single(self):
        f = get_solution("reverse_list")
        head = create_linked_list([1])
        result = f(head)
        assert linked_list_to_list(result) == [1]

    def test_reverse_edge_empty(self):
        f = get_solution("reverse_list")
        assert f(None) is None

    def test_reverse_two(self):
        f = get_solution("reverse_list")
        head = create_linked_list([1, 2])
        result = f(head)
        assert linked_list_to_list(result) == [2, 1]


class TestMergeTwoLists:
    def test_merge_basic(self):
        f = get_solution("merge_two_lists")
        l1 = create_linked_list([1, 2, 4])
        l2 = create_linked_list([1, 3, 4])
        result = f(l1, l2)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

    def test_merge_edge_one_empty(self):
        f = get_solution("merge_two_lists")
        l1 = create_linked_list([])
        l2 = create_linked_list([0])
        result = f(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_merge_edge_both_empty(self):
        f = get_solution("merge_two_lists")
        result = f(None, None)
        assert result is None

    def test_merge_different_lengths(self):
        f = get_solution("merge_two_lists")
        l1 = create_linked_list([1])
        l2 = create_linked_list([2, 3, 4])
        result = f(l1, l2)
        assert linked_list_to_list(result) == [1, 2, 3, 4]


class TestHasCycle:
    def test_cycle_true(self):
        f = get_solution("has_cycle")
        head = create_linked_list([3, 2, 0, -4])
        create_cycle(head, 1)  # Cycle at position 1
        assert f(head) == True

    def test_cycle_false(self):
        f = get_solution("has_cycle")
        head = create_linked_list([1, 2, 3])
        assert f(head) == False

    def test_cycle_edge_single_no_cycle(self):
        f = get_solution("has_cycle")
        head = create_linked_list([1])
        assert f(head) == False

    def test_cycle_edge_empty(self):
        f = get_solution("has_cycle")
        assert f(None) == False

    def test_cycle_self_loop(self):
        f = get_solution("has_cycle")
        head = create_linked_list([1])
        head.next = head
        assert f(head) == True


class TestRemoveNthFromEnd:
    def test_remove_basic(self):
        f = get_solution("remove_nth_from_end")
        head = create_linked_list([1, 2, 3, 4, 5])
        result = f(head, 2)
        assert linked_list_to_list(result) == [1, 2, 3, 5]

    def test_remove_head(self):
        f = get_solution("remove_nth_from_end")
        head = create_linked_list([1])
        result = f(head, 1)
        assert result is None

    def test_remove_first(self):
        f = get_solution("remove_nth_from_end")
        head = create_linked_list([1, 2])
        result = f(head, 2)
        assert linked_list_to_list(result) == [2]


class TestFindMiddle:
    def test_middle_odd(self):
        f = get_solution("find_middle")
        head = create_linked_list([1, 2, 3, 4, 5])
        result = f(head)
        assert result.val == 3

    def test_middle_even(self):
        f = get_solution("find_middle")
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        result = f(head)
        assert result.val == 4  # Second middle

    def test_middle_single(self):
        f = get_solution("find_middle")
        head = create_linked_list([1])
        result = f(head)
        assert result.val == 1


class TestIsPalindromeList:
    def test_palindrome_true(self):
        f = get_solution("is_palindrome_list")
        head = create_linked_list([1, 2, 2, 1])
        assert f(head) == True

    def test_palindrome_false(self):
        f = get_solution("is_palindrome_list")
        head = create_linked_list([1, 2])
        assert f(head) == False

    def test_palindrome_single(self):
        f = get_solution("is_palindrome_list")
        head = create_linked_list([1])
        assert f(head) == True

    def test_palindrome_odd(self):
        f = get_solution("is_palindrome_list")
        head = create_linked_list([1, 2, 1])
        assert f(head) == True


class TestAddTwoNumbers:
    def test_add_basic(self):
        f = get_solution("add_two_numbers")
        l1 = create_linked_list([2, 4, 3])  # 342
        l2 = create_linked_list([5, 6, 4])  # 465
        result = f(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]  # 807

    def test_add_zeros(self):
        f = get_solution("add_two_numbers")
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        result = f(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_add_carry(self):
        f = get_solution("add_two_numbers")
        l1 = create_linked_list([9, 9, 9])
        l2 = create_linked_list([1])
        result = f(l1, l2)
        assert linked_list_to_list(result) == [0, 0, 0, 1]


class TestReorderList:
    def test_reorder_basic(self):
        f = get_solution("reorder_list")
        head = create_linked_list([1, 2, 3, 4])
        f(head)
        assert linked_list_to_list(head) == [1, 4, 2, 3]

    def test_reorder_five(self):
        f = get_solution("reorder_list")
        head = create_linked_list([1, 2, 3, 4, 5])
        f(head)
        assert linked_list_to_list(head) == [1, 5, 2, 4, 3]

    def test_reorder_single(self):
        f = get_solution("reorder_list")
        head = create_linked_list([1])
        f(head)
        assert linked_list_to_list(head) == [1]

    def test_reorder_two(self):
        f = get_solution("reorder_list")
        head = create_linked_list([1, 2])
        f(head)
        assert linked_list_to_list(head) == [1, 2]
