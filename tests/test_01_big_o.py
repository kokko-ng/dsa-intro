"""
Tests for Topic 01: Big O Notation & Complexity Analysis

Test naming convention: test_{function_name}_{category}_{description}
Categories: basic, edge, perf (performance)
"""
import pytest
from conftest import get_solution


# ============================================================================
# Exercise 1: Sum Array
# ============================================================================

class TestSumArray:
    """Tests for sum_array function."""

    def test_sum_array_basic_positive(self):
        """Basic case with positive numbers."""
        sum_array = get_solution("sum_array")
        assert sum_array([1, 2, 3, 4, 5]) == 15

    def test_sum_array_basic_mixed(self):
        """Mix of positive and negative numbers."""
        sum_array = get_solution("sum_array")
        assert sum_array([-1, 1, -2, 2]) == 0

    def test_sum_array_edge_empty(self):
        """Empty array should return 0."""
        sum_array = get_solution("sum_array")
        assert sum_array([]) == 0

    def test_sum_array_edge_single(self):
        """Single element."""
        sum_array = get_solution("sum_array")
        assert sum_array([42]) == 42

    def test_sum_array_edge_negative(self):
        """All negative numbers."""
        sum_array = get_solution("sum_array")
        assert sum_array([-1, -2, -3]) == -6

    def test_sum_array_perf_large(self):
        """Large input should complete quickly."""
        sum_array = get_solution("sum_array")
        nums = list(range(10000))
        assert sum_array(nums) == sum(nums)


# ============================================================================
# Exercise 2: Has Duplicates
# ============================================================================

class TestHasDuplicates:
    """Tests for has_duplicates function."""

    def test_has_duplicates_basic_true(self):
        """Array with duplicates."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([1, 2, 3, 1]) == True

    def test_has_duplicates_basic_false(self):
        """Array without duplicates."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([1, 2, 3, 4]) == False

    def test_has_duplicates_edge_empty(self):
        """Empty array has no duplicates."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([]) == False

    def test_has_duplicates_edge_single(self):
        """Single element has no duplicates."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([1]) == False

    def test_has_duplicates_edge_all_same(self):
        """All same elements."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([5, 5, 5, 5]) == True

    def test_has_duplicates_edge_negative(self):
        """Negative numbers."""
        has_duplicates = get_solution("has_duplicates")
        assert has_duplicates([-1, -2, -1]) == True

    def test_has_duplicates_perf_large_no_dup(self):
        """Large input without duplicates - must be O(n)."""
        has_duplicates = get_solution("has_duplicates")
        nums = list(range(100000))
        assert has_duplicates(nums) == False

    def test_has_duplicates_perf_large_with_dup(self):
        """Large input with duplicate at end."""
        has_duplicates = get_solution("has_duplicates")
        nums = list(range(100000)) + [0]
        assert has_duplicates(nums) == True


# ============================================================================
# Exercise 3: Find Pair With Sum
# ============================================================================

class TestFindPairWithSum:
    """Tests for find_pair_with_sum function."""

    def test_find_pair_with_sum_basic_true(self):
        """Pair exists."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([2, 7, 11, 15], 9) == True

    def test_find_pair_with_sum_basic_false(self):
        """No pair exists."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([1, 2, 3, 4], 10) == False

    def test_find_pair_with_sum_edge_duplicates(self):
        """Same number used twice."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([3, 3], 6) == True

    def test_find_pair_with_sum_edge_two_elements_no(self):
        """Two elements, no match."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([1, 2], 10) == False

    def test_find_pair_with_sum_edge_negative(self):
        """Negative numbers."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([-1, -2, -3, 4], 1) == True  # -2 + 3 won't work, but -3 + 4 = 1

    def test_find_pair_with_sum_edge_zero_target(self):
        """Target is zero."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        assert find_pair_with_sum([-5, 5, 1, 2], 0) == True

    def test_find_pair_with_sum_perf_large(self):
        """Large input - must be O(n)."""
        find_pair_with_sum = get_solution("find_pair_with_sum")
        nums = list(range(100000))
        # 99998 + 99999 = 199997
        assert find_pair_with_sum(nums, 199997) == True


# ============================================================================
# Exercise 4: Print Pairs
# ============================================================================

class TestPrintPairs:
    """Tests for print_pairs function."""

    def test_print_pairs_basic(self):
        """Standard case."""
        print_pairs = get_solution("print_pairs")
        result = print_pairs([1, 2, 3])
        assert result == [[1, 2], [1, 3], [2, 3]]

    def test_print_pairs_basic_four(self):
        """Four elements."""
        print_pairs = get_solution("print_pairs")
        result = print_pairs([1, 2, 3, 4])
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        assert result == expected

    def test_print_pairs_edge_empty(self):
        """Empty array."""
        print_pairs = get_solution("print_pairs")
        assert print_pairs([]) == []

    def test_print_pairs_edge_single(self):
        """Single element - no pairs."""
        print_pairs = get_solution("print_pairs")
        assert print_pairs([1]) == []

    def test_print_pairs_edge_two(self):
        """Two elements - one pair."""
        print_pairs = get_solution("print_pairs")
        assert print_pairs([5, 10]) == [[5, 10]]


# ============================================================================
# Exercise 5: Binary Search
# ============================================================================

class TestBinarySearch:
    """Tests for binary_search function."""

    def test_binary_search_basic_found(self):
        """Target exists in array."""
        binary_search = get_solution("binary_search")
        assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_binary_search_basic_not_found(self):
        """Target doesn't exist."""
        binary_search = get_solution("binary_search")
        assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_binary_search_basic_first(self):
        """Target is first element."""
        binary_search = get_solution("binary_search")
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_binary_search_basic_last(self):
        """Target is last element."""
        binary_search = get_solution("binary_search")
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_binary_search_edge_empty(self):
        """Empty array."""
        binary_search = get_solution("binary_search")
        assert binary_search([], 5) == -1

    def test_binary_search_edge_single_found(self):
        """Single element, found."""
        binary_search = get_solution("binary_search")
        assert binary_search([5], 5) == 0

    def test_binary_search_edge_single_not_found(self):
        """Single element, not found."""
        binary_search = get_solution("binary_search")
        assert binary_search([5], 3) == -1

    def test_binary_search_edge_two_elements(self):
        """Two elements."""
        binary_search = get_solution("binary_search")
        assert binary_search([1, 3], 3) == 1
        assert binary_search([1, 3], 1) == 0
        assert binary_search([1, 3], 2) == -1

    def test_binary_search_perf_large(self):
        """Large input - must be O(log n)."""
        binary_search = get_solution("binary_search")
        nums = list(range(0, 1000000, 2))  # Even numbers 0 to 999998
        assert binary_search(nums, 500000) == 250000
        assert binary_search(nums, 500001) == -1  # Odd number not in list
