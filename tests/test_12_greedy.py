"""
Tests for Topic 12: Greedy Algorithms
"""
import pytest
from conftest import get_solution


class TestJumpGame:
    def test_jump_true(self):
        f = get_solution("jump_game")
        assert f([2, 3, 1, 1, 4]) == True

    def test_jump_false(self):
        f = get_solution("jump_game")
        assert f([3, 2, 1, 0, 4]) == False

    def test_jump_single(self):
        f = get_solution("jump_game")
        assert f([0]) == True


class TestJumpGameII:
    def test_jump2_basic(self):
        f = get_solution("jump_game_ii")
        assert f([2, 3, 1, 1, 4]) == 2

    def test_jump2_larger(self):
        f = get_solution("jump_game_ii")
        assert f([2, 3, 0, 1, 4]) == 2


class TestGasStation:
    def test_gas_possible(self):
        f = get_solution("gas_station")
        assert f([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

    def test_gas_impossible(self):
        f = get_solution("gas_station")
        assert f([2, 3, 4], [3, 4, 3]) == -1


class TestCandy:
    def test_candy_basic(self):
        f = get_solution("candy")
        assert f([1, 0, 2]) == 5

    def test_candy_same(self):
        f = get_solution("candy")
        assert f([1, 2, 2]) == 4


class TestPartitionLabels:
    def test_partition_basic(self):
        f = get_solution("partition_labels")
        assert f("ababcbacadefegdehijhklij") == [9, 7, 8]

    def test_partition_single(self):
        f = get_solution("partition_labels")
        assert f("eccbbbbdec") == [10]


class TestValidParenthesisString:
    def test_valid_true(self):
        f = get_solution("valid_parenthesis_string")
        assert f("()") == True

    def test_valid_star(self):
        f = get_solution("valid_parenthesis_string")
        assert f("(*)") == True

    def test_valid_complex(self):
        f = get_solution("valid_parenthesis_string")
        assert f("(*))") == True


class TestMaximumSubarrayGreedy:
    def test_max_basic(self):
        f = get_solution("maximum_subarray_greedy")
        assert f([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_max_all_negative(self):
        f = get_solution("maximum_subarray_greedy")
        assert f([-1, -2, -3]) == -1
