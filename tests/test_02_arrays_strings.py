"""
Tests for Topic 02: Arrays & Strings
"""
import pytest
from conftest import get_solution


# ============================================================================
# Exercise 1: Two Sum
# ============================================================================

class TestTwoSum:
    """Tests for two_sum function."""

    def test_two_sum_basic(self):
        two_sum = get_solution("two_sum")
        result = two_sum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]

    def test_two_sum_basic_middle(self):
        two_sum = get_solution("two_sum")
        result = two_sum([3, 2, 4], 6)
        assert sorted(result) == [1, 2]

    def test_two_sum_edge_duplicates(self):
        two_sum = get_solution("two_sum")
        result = two_sum([3, 3], 6)
        assert sorted(result) == [0, 1]

    def test_two_sum_edge_negative(self):
        two_sum = get_solution("two_sum")
        result = two_sum([-1, -2, -3, -4, -5], -8)
        assert sorted(result) == [2, 4]

    def test_two_sum_perf_large(self):
        two_sum = get_solution("two_sum")
        nums = list(range(10000))
        result = two_sum(nums, 19997)  # 9998 + 9999
        assert sorted(result) == [9998, 9999]


# ============================================================================
# Exercise 2: Best Time to Buy and Sell
# ============================================================================

class TestBestTimeToBuySell:
    """Tests for best_time_to_buy_sell function."""

    def test_best_time_basic(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([7, 1, 5, 3, 6, 4]) == 5

    def test_best_time_no_profit(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([7, 6, 4, 3, 1]) == 0

    def test_best_time_edge_single(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([5]) == 0

    def test_best_time_edge_two_profit(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([1, 2]) == 1

    def test_best_time_edge_two_no_profit(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([2, 1]) == 0

    def test_best_time_edge_all_same(self):
        best_time = get_solution("best_time_to_buy_sell")
        assert best_time([5, 5, 5, 5]) == 0

    def test_best_time_perf_large(self):
        best_time = get_solution("best_time_to_buy_sell")
        prices = list(range(10000, 0, -1)) + [10001]  # Decreasing then spike
        assert best_time(prices) == 10000


# ============================================================================
# Exercise 3: Contains Duplicate
# ============================================================================

class TestContainsDuplicate:
    """Tests for contains_duplicate function."""

    def test_contains_dup_basic_true(self):
        contains_dup = get_solution("contains_duplicate")
        assert contains_dup([1, 2, 3, 1]) == True

    def test_contains_dup_basic_false(self):
        contains_dup = get_solution("contains_duplicate")
        assert contains_dup([1, 2, 3, 4]) == False

    def test_contains_dup_edge_single(self):
        contains_dup = get_solution("contains_duplicate")
        assert contains_dup([1]) == False

    def test_contains_dup_edge_all_same(self):
        contains_dup = get_solution("contains_duplicate")
        assert contains_dup([1, 1, 1, 1]) == True

    def test_contains_dup_perf_large(self):
        contains_dup = get_solution("contains_duplicate")
        assert contains_dup(list(range(100000))) == False
        assert contains_dup(list(range(100000)) + [0]) == True


# ============================================================================
# Exercise 4: Maximum Subarray
# ============================================================================

class TestMaxSubarray:
    """Tests for max_subarray function."""

    def test_max_subarray_basic(self):
        max_sub = get_solution("max_subarray")
        assert max_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_max_subarray_edge_single_positive(self):
        max_sub = get_solution("max_subarray")
        assert max_sub([1]) == 1

    def test_max_subarray_edge_single_negative(self):
        max_sub = get_solution("max_subarray")
        assert max_sub([-1]) == -1

    def test_max_subarray_all_negative(self):
        max_sub = get_solution("max_subarray")
        assert max_sub([-2, -1, -3]) == -1

    def test_max_subarray_all_positive(self):
        max_sub = get_solution("max_subarray")
        assert max_sub([1, 2, 3, 4]) == 10

    def test_max_subarray_perf_large(self):
        max_sub = get_solution("max_subarray")
        nums = [1] * 100000
        assert max_sub(nums) == 100000


# ============================================================================
# Exercise 5: Rotate Array
# ============================================================================

class TestRotateArray:
    """Tests for rotate_array function."""

    def test_rotate_basic(self):
        rotate = get_solution("rotate_array")
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

    def test_rotate_basic_small(self):
        rotate = get_solution("rotate_array")
        nums = [-1, -100, 3, 99]
        rotate(nums, 2)
        assert nums == [3, 99, -1, -100]

    def test_rotate_edge_k_zero(self):
        rotate = get_solution("rotate_array")
        nums = [1, 2, 3]
        rotate(nums, 0)
        assert nums == [1, 2, 3]

    def test_rotate_edge_k_equals_length(self):
        rotate = get_solution("rotate_array")
        nums = [1, 2, 3]
        rotate(nums, 3)
        assert nums == [1, 2, 3]

    def test_rotate_edge_k_greater_than_length(self):
        rotate = get_solution("rotate_array")
        nums = [1, 2, 3]
        rotate(nums, 5)  # Same as k=2
        assert nums == [2, 3, 1]

    def test_rotate_edge_single(self):
        rotate = get_solution("rotate_array")
        nums = [1]
        rotate(nums, 5)
        assert nums == [1]


# ============================================================================
# Exercise 6: Reverse String
# ============================================================================

class TestReverseString:
    """Tests for reverse_string function."""

    def test_reverse_basic(self):
        reverse = get_solution("reverse_string")
        assert reverse("hello") == "olleh"

    def test_reverse_edge_empty(self):
        reverse = get_solution("reverse_string")
        assert reverse("") == ""

    def test_reverse_edge_single(self):
        reverse = get_solution("reverse_string")
        assert reverse("a") == "a"

    def test_reverse_palindrome(self):
        reverse = get_solution("reverse_string")
        assert reverse("radar") == "radar"

    def test_reverse_with_spaces(self):
        reverse = get_solution("reverse_string")
        assert reverse("hello world") == "dlrow olleh"


# ============================================================================
# Exercise 7: Valid Anagram
# ============================================================================

class TestValidAnagram:
    """Tests for valid_anagram function."""

    def test_anagram_basic_true(self):
        valid = get_solution("valid_anagram")
        assert valid("anagram", "nagaram") == True

    def test_anagram_basic_false(self):
        valid = get_solution("valid_anagram")
        assert valid("rat", "car") == False

    def test_anagram_edge_different_lengths(self):
        valid = get_solution("valid_anagram")
        assert valid("a", "ab") == False

    def test_anagram_edge_empty(self):
        valid = get_solution("valid_anagram")
        assert valid("", "") == True

    def test_anagram_edge_single_same(self):
        valid = get_solution("valid_anagram")
        assert valid("a", "a") == True

    def test_anagram_edge_single_different(self):
        valid = get_solution("valid_anagram")
        assert valid("a", "b") == False


# ============================================================================
# Exercise 8: Longest Common Prefix
# ============================================================================

class TestLongestCommonPrefix:
    """Tests for longest_common_prefix function."""

    def test_lcp_basic(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["flower", "flow", "flight"]) == "fl"

    def test_lcp_no_common(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["dog", "racecar", "car"]) == ""

    def test_lcp_edge_single_string(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["alone"]) == "alone"

    def test_lcp_edge_empty_string(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["", "abc", "ab"]) == ""

    def test_lcp_all_same(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["test", "test", "test"]) == "test"

    def test_lcp_edge_one_char(self):
        lcp = get_solution("longest_common_prefix")
        assert lcp(["a", "a", "a"]) == "a"


# ============================================================================
# Exercise 9: String to Integer
# ============================================================================

class TestStringToInteger:
    """Tests for string_to_integer function."""

    def test_atoi_basic(self):
        atoi = get_solution("string_to_integer")
        assert atoi("42") == 42

    def test_atoi_negative(self):
        atoi = get_solution("string_to_integer")
        assert atoi("-42") == -42

    def test_atoi_with_whitespace(self):
        atoi = get_solution("string_to_integer")
        assert atoi("   -42") == -42

    def test_atoi_with_trailing_text(self):
        atoi = get_solution("string_to_integer")
        assert atoi("4193 with words") == 4193

    def test_atoi_edge_overflow_positive(self):
        atoi = get_solution("string_to_integer")
        assert atoi("91283472332") == 2147483647  # INT_MAX

    def test_atoi_edge_overflow_negative(self):
        atoi = get_solution("string_to_integer")
        assert atoi("-91283472332") == -2147483648  # INT_MIN

    def test_atoi_edge_empty(self):
        atoi = get_solution("string_to_integer")
        assert atoi("") == 0

    def test_atoi_edge_only_sign(self):
        atoi = get_solution("string_to_integer")
        assert atoi("+") == 0

    def test_atoi_edge_text_first(self):
        atoi = get_solution("string_to_integer")
        assert atoi("words and 987") == 0


# ============================================================================
# Exercise 10: Product Except Self
# ============================================================================

class TestProductExceptSelf:
    """Tests for product_except_self function."""

    def test_product_basic(self):
        product = get_solution("product_except_self")
        assert product([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_product_with_zero(self):
        product = get_solution("product_except_self")
        assert product([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_product_edge_two_elements(self):
        product = get_solution("product_except_self")
        assert product([2, 3]) == [3, 2]

    def test_product_edge_with_negatives(self):
        product = get_solution("product_except_self")
        assert product([-1, -2, -3]) == [6, 3, 2]

    def test_product_edge_multiple_zeros(self):
        product = get_solution("product_except_self")
        assert product([0, 0, 1]) == [0, 0, 0]

    def test_product_perf_large(self):
        product = get_solution("product_except_self")
        nums = [1] * 1000
        result = product(nums)
        assert all(r == 1 for r in result)
