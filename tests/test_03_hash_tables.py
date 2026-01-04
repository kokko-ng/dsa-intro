"""
Tests for Topic 03: Hash Tables
"""
import pytest
from conftest import get_solution


class TestFirstUniqueChar:
    def test_first_unique_basic(self):
        f = get_solution("first_unique_char")
        assert f("leetcode") == 0

    def test_first_unique_middle(self):
        f = get_solution("first_unique_char")
        assert f("loveleetcode") == 2

    def test_first_unique_none(self):
        f = get_solution("first_unique_char")
        assert f("aabb") == -1

    def test_first_unique_edge_empty(self):
        f = get_solution("first_unique_char")
        assert f("") == -1

    def test_first_unique_edge_single(self):
        f = get_solution("first_unique_char")
        assert f("a") == 0

    def test_first_unique_edge_all_same(self):
        f = get_solution("first_unique_char")
        assert f("aaaa") == -1


class TestGroupAnagrams:
    def test_group_basic(self):
        f = get_solution("group_anagrams")
        result = f(["eat", "tea", "tan", "ate", "nat", "bat"])
        result_sorted = [sorted(g) for g in result]
        result_sorted.sort()
        expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
        assert result_sorted == expected

    def test_group_edge_empty_string(self):
        f = get_solution("group_anagrams")
        assert f([""]) == [[""]]

    def test_group_edge_single(self):
        f = get_solution("group_anagrams")
        assert f(["a"]) == [["a"]]

    def test_group_no_anagrams(self):
        f = get_solution("group_anagrams")
        result = f(["abc", "def", "ghi"])
        assert len(result) == 3


class TestIsomorphicStrings:
    def test_isomorphic_true(self):
        f = get_solution("isomorphic_strings")
        assert f("egg", "add") == True

    def test_isomorphic_false(self):
        f = get_solution("isomorphic_strings")
        assert f("foo", "bar") == False

    def test_isomorphic_paper(self):
        f = get_solution("isomorphic_strings")
        assert f("paper", "title") == True

    def test_isomorphic_edge_single(self):
        f = get_solution("isomorphic_strings")
        assert f("a", "b") == True

    def test_isomorphic_badc(self):
        f = get_solution("isomorphic_strings")
        assert f("badc", "baba") == False


class TestWordPattern:
    def test_pattern_match(self):
        f = get_solution("word_pattern")
        assert f("abba", "dog cat cat dog") == True

    def test_pattern_no_match(self):
        f = get_solution("word_pattern")
        assert f("abba", "dog cat cat fish") == False

    def test_pattern_wrong_pattern(self):
        f = get_solution("word_pattern")
        assert f("aaaa", "dog cat cat dog") == False

    def test_pattern_edge_single(self):
        f = get_solution("word_pattern")
        assert f("a", "dog") == True

    def test_pattern_length_mismatch(self):
        f = get_solution("word_pattern")
        assert f("ab", "dog") == False


class TestIntersectionOfArrays:
    def test_intersection_basic(self):
        f = get_solution("intersection_of_arrays")
        result = set(f([1, 2, 2, 1], [2, 2]))
        assert result == {2}

    def test_intersection_multiple(self):
        f = get_solution("intersection_of_arrays")
        result = set(f([4, 9, 5], [9, 4, 9, 8, 4]))
        assert result == {4, 9}

    def test_intersection_edge_empty(self):
        f = get_solution("intersection_of_arrays")
        assert f([], [1, 2]) == []

    def test_intersection_none(self):
        f = get_solution("intersection_of_arrays")
        assert f([1, 2], [3, 4]) == []


class TestLongestConsecutive:
    def test_consecutive_basic(self):
        f = get_solution("longest_consecutive")
        assert f([100, 4, 200, 1, 3, 2]) == 4

    def test_consecutive_long(self):
        f = get_solution("longest_consecutive")
        assert f([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    def test_consecutive_edge_empty(self):
        f = get_solution("longest_consecutive")
        assert f([]) == 0

    def test_consecutive_edge_single(self):
        f = get_solution("longest_consecutive")
        assert f([1]) == 1

    def test_consecutive_duplicates(self):
        f = get_solution("longest_consecutive")
        assert f([1, 2, 0, 1]) == 3

    def test_consecutive_perf_large(self):
        f = get_solution("longest_consecutive")
        nums = list(range(10000))
        assert f(nums) == 10000


class TestSubarraySumEqualsK:
    def test_subarray_basic(self):
        f = get_solution("subarray_sum_equals_k")
        assert f([1, 1, 1], 2) == 2

    def test_subarray_multiple(self):
        f = get_solution("subarray_sum_equals_k")
        assert f([1, 2, 3], 3) == 2

    def test_subarray_edge_single_match(self):
        f = get_solution("subarray_sum_equals_k")
        assert f([1], 1) == 1

    def test_subarray_edge_single_no_match(self):
        f = get_solution("subarray_sum_equals_k")
        assert f([1], 2) == 0

    def test_subarray_negative(self):
        f = get_solution("subarray_sum_equals_k")
        assert f([1, -1, 0], 0) == 3

    def test_subarray_perf_large(self):
        f = get_solution("subarray_sum_equals_k")
        nums = [1] * 10000
        # Every subarray of length 2 sums to 2
        assert f(nums, 2) == 9999


class TestTopKFrequent:
    def test_topk_basic(self):
        f = get_solution("top_k_frequent")
        result = set(f([1, 1, 1, 2, 2, 3], 2))
        assert result == {1, 2}

    def test_topk_single(self):
        f = get_solution("top_k_frequent")
        assert f([1], 1) == [1]

    def test_topk_all(self):
        f = get_solution("top_k_frequent")
        result = set(f([1, 2, 3], 3))
        assert result == {1, 2, 3}

    def test_topk_ties(self):
        f = get_solution("top_k_frequent")
        result = set(f([1, 1, 2, 2, 3], 2))
        # 1 and 2 both appear twice, either is valid
        assert 1 in result and 2 in result
