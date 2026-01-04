"""
Tests for Topic 04: Two Pointers & Sliding Window
"""
import pytest
from conftest import get_solution


class TestValidPalindrome:
    def test_valid_basic_true(self):
        f = get_solution("valid_palindrome")
        assert f("A man, a plan, a canal: Panama") == True

    def test_valid_basic_false(self):
        f = get_solution("valid_palindrome")
        assert f("race a car") == False

    def test_valid_edge_empty(self):
        f = get_solution("valid_palindrome")
        assert f("") == True

    def test_valid_edge_single(self):
        f = get_solution("valid_palindrome")
        assert f("a") == True

    def test_valid_spaces_only(self):
        f = get_solution("valid_palindrome")
        assert f(" ") == True


class TestTwoSumSorted:
    def test_two_sum_basic(self):
        f = get_solution("two_sum_sorted")
        assert f([2, 7, 11, 15], 9) == [1, 2]

    def test_two_sum_end(self):
        f = get_solution("two_sum_sorted")
        assert f([2, 3, 4], 6) == [1, 3]

    def test_two_sum_negative(self):
        f = get_solution("two_sum_sorted")
        assert f([-1, 0], -1) == [1, 2]

    def test_two_sum_perf_large(self):
        f = get_solution("two_sum_sorted")
        nums = list(range(1, 10001))
        assert f(nums, 19999) == [9999, 10000]


class TestThreeSum:
    def test_three_sum_basic(self):
        f = get_solution("three_sum")
        result = f([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

    def test_three_sum_no_solution(self):
        f = get_solution("three_sum")
        assert f([0, 1, 1]) == []

    def test_three_sum_all_zeros(self):
        f = get_solution("three_sum")
        assert f([0, 0, 0]) == [[0, 0, 0]]

    def test_three_sum_edge_empty(self):
        f = get_solution("three_sum")
        assert f([]) == []


class TestContainerWithMostWater:
    def test_container_basic(self):
        f = get_solution("container_with_most_water")
        assert f([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_container_two_elements(self):
        f = get_solution("container_with_most_water")
        assert f([1, 1]) == 1

    def test_container_increasing(self):
        f = get_solution("container_with_most_water")
        assert f([1, 2, 3, 4, 5]) == 6

    def test_container_perf_large(self):
        f = get_solution("container_with_most_water")
        height = [i for i in range(10000)]
        result = f(height)
        assert result > 0


class TestRemoveDuplicatesSorted:
    def test_remove_basic(self):
        f = get_solution("remove_duplicates_sorted")
        nums = [1, 1, 2]
        k = f(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_remove_many(self):
        f = get_solution("remove_duplicates_sorted")
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = f(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]

    def test_remove_edge_single(self):
        f = get_solution("remove_duplicates_sorted")
        nums = [1]
        assert f(nums) == 1

    def test_remove_no_duplicates(self):
        f = get_solution("remove_duplicates_sorted")
        nums = [1, 2, 3]
        assert f(nums) == 3


class TestMaxSumSubarrayK:
    def test_max_sum_basic(self):
        f = get_solution("max_sum_subarray_k")
        assert f([2, 1, 5, 1, 3, 2], 3) == 9

    def test_max_sum_all_same(self):
        f = get_solution("max_sum_subarray_k")
        assert f([1, 1, 1, 1], 2) == 2

    def test_max_sum_k_equals_len(self):
        f = get_solution("max_sum_subarray_k")
        assert f([1, 2, 3], 3) == 6

    def test_max_sum_negative(self):
        f = get_solution("max_sum_subarray_k")
        assert f([-1, -2, -3, -4], 2) == -3


class TestLongestSubstringWithoutRepeating:
    def test_longest_basic(self):
        f = get_solution("longest_substring_without_repeating")
        assert f("abcabcbb") == 3

    def test_longest_all_same(self):
        f = get_solution("longest_substring_without_repeating")
        assert f("bbbbb") == 1

    def test_longest_all_unique(self):
        f = get_solution("longest_substring_without_repeating")
        assert f("abcdef") == 6

    def test_longest_edge_empty(self):
        f = get_solution("longest_substring_without_repeating")
        assert f("") == 0

    def test_longest_pwwkew(self):
        f = get_solution("longest_substring_without_repeating")
        assert f("pwwkew") == 3


class TestMinimumWindowSubstring:
    def test_min_window_basic(self):
        f = get_solution("minimum_window_substring")
        assert f("ADOBECODEBANC", "ABC") == "BANC"

    def test_min_window_exact(self):
        f = get_solution("minimum_window_substring")
        assert f("a", "a") == "a"

    def test_min_window_no_solution(self):
        f = get_solution("minimum_window_substring")
        assert f("a", "aa") == ""

    def test_min_window_all_same(self):
        f = get_solution("minimum_window_substring")
        assert f("aa", "aa") == "aa"
