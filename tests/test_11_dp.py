"""
Tests for Topic 11: Dynamic Programming
"""
import pytest
from conftest import get_solution


class TestClimbingStairs:
    def test_stairs_base(self):
        f = get_solution("climbing_stairs")
        assert f(1) == 1
        assert f(2) == 2

    def test_stairs_larger(self):
        f = get_solution("climbing_stairs")
        assert f(3) == 3
        assert f(5) == 8


class TestHouseRobber:
    def test_robber_basic(self):
        f = get_solution("house_robber")
        assert f([1, 2, 3, 1]) == 4

    def test_robber_larger(self):
        f = get_solution("house_robber")
        assert f([2, 7, 9, 3, 1]) == 12

    def test_robber_single(self):
        f = get_solution("house_robber")
        assert f([5]) == 5


class TestCoinChange:
    def test_coin_basic(self):
        f = get_solution("coin_change")
        assert f([1, 2, 5], 11) == 3

    def test_coin_impossible(self):
        f = get_solution("coin_change")
        assert f([2], 3) == -1

    def test_coin_zero(self):
        f = get_solution("coin_change")
        assert f([1], 0) == 0


class TestLongestIncreasingSubsequence:
    def test_lis_basic(self):
        f = get_solution("longest_increasing_subsequence")
        assert f([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_lis_all_same(self):
        f = get_solution("longest_increasing_subsequence")
        assert f([7, 7, 7, 7]) == 1

    def test_lis_increasing(self):
        f = get_solution("longest_increasing_subsequence")
        assert f([1, 2, 3, 4, 5]) == 5


class TestUniquePaths:
    def test_paths_basic(self):
        f = get_solution("unique_paths")
        assert f(3, 7) == 28

    def test_paths_edge(self):
        f = get_solution("unique_paths")
        assert f(1, 1) == 1
        assert f(2, 2) == 2


class TestDecodeWays:
    def test_decode_basic(self):
        f = get_solution("decode_ways")
        assert f("12") == 2  # AB or L

    def test_decode_larger(self):
        f = get_solution("decode_ways")
        assert f("226") == 3

    def test_decode_zero(self):
        f = get_solution("decode_ways")
        assert f("06") == 0


class TestWordBreak:
    def test_break_true(self):
        f = get_solution("word_break")
        assert f("leetcode", ["leet", "code"]) == True

    def test_break_false(self):
        f = get_solution("word_break")
        assert f("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False


class TestLongestCommonSubsequence:
    def test_lcs_basic(self):
        f = get_solution("longest_common_subsequence")
        assert f("abcde", "ace") == 3

    def test_lcs_none(self):
        f = get_solution("longest_common_subsequence")
        assert f("abc", "def") == 0


class TestEditDistance:
    def test_edit_basic(self):
        f = get_solution("edit_distance")
        assert f("horse", "ros") == 3

    def test_edit_larger(self):
        f = get_solution("edit_distance")
        assert f("intention", "execution") == 5


class TestMaxProductSubarray:
    def test_product_basic(self):
        f = get_solution("max_product_subarray")
        assert f([2, 3, -2, 4]) == 6

    def test_product_negative(self):
        f = get_solution("max_product_subarray")
        assert f([-2, 0, -1]) == 0
