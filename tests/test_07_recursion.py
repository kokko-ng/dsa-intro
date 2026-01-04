"""
Tests for Topic 07: Recursion & Backtracking
"""
import pytest
from conftest import get_solution


class TestFibonacci:
    def test_fib_base(self):
        f = get_solution("fibonacci")
        assert f(0) == 0
        assert f(1) == 1

    def test_fib_small(self):
        f = get_solution("fibonacci")
        assert f(5) == 5
        assert f(10) == 55

    def test_fib_larger(self):
        f = get_solution("fibonacci")
        assert f(20) == 6765


class TestFactorial:
    def test_fact_base(self):
        f = get_solution("factorial")
        assert f(0) == 1
        assert f(1) == 1

    def test_fact_small(self):
        f = get_solution("factorial")
        assert f(5) == 120
        assert f(10) == 3628800


class TestSubsets:
    def test_subsets_basic(self):
        f = get_solution("subsets")
        result = f([1, 2, 3])
        assert len(result) == 8
        assert [] in result
        assert [1, 2, 3] in result

    def test_subsets_single(self):
        f = get_solution("subsets")
        result = f([0])
        assert sorted(result) == [[], [0]]

    def test_subsets_empty(self):
        f = get_solution("subsets")
        assert f([]) == [[]]


class TestPermutations:
    def test_perms_basic(self):
        f = get_solution("permutations")
        result = f([1, 2, 3])
        assert len(result) == 6
        assert [1, 2, 3] in result
        assert [3, 2, 1] in result

    def test_perms_single(self):
        f = get_solution("permutations")
        assert f([1]) == [[1]]


class TestCombinationSum:
    def test_combo_basic(self):
        f = get_solution("combination_sum")
        result = f([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

    def test_combo_multiple(self):
        f = get_solution("combination_sum")
        result = f([2, 3, 5], 8)
        assert len(result) == 3

    def test_combo_no_solution(self):
        f = get_solution("combination_sum")
        assert f([2], 1) == []


class TestLetterCombinations:
    def test_letters_basic(self):
        f = get_solution("letter_combinations")
        result = f("23")
        assert len(result) == 9
        assert "ad" in result

    def test_letters_empty(self):
        f = get_solution("letter_combinations")
        assert f("") == []

    def test_letters_single(self):
        f = get_solution("letter_combinations")
        result = f("2")
        assert sorted(result) == ["a", "b", "c"]


class TestGenerateParentheses:
    def test_parens_one(self):
        f = get_solution("generate_parentheses")
        assert f(1) == ["()"]

    def test_parens_three(self):
        f = get_solution("generate_parentheses")
        result = f(3)
        assert len(result) == 5
        assert "((()))" in result


class TestWordSearch:
    def test_word_found(self):
        f = get_solution("word_search")
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert f(board, "ABCCED") == True

    def test_word_not_found(self):
        f = get_solution("word_search")
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert f(board, "ABCB") == False

    def test_word_single(self):
        f = get_solution("word_search")
        assert f([["A"]], "A") == True


class TestNQueens:
    def test_queens_four(self):
        f = get_solution("n_queens")
        result = f(4)
        assert len(result) == 2

    def test_queens_one(self):
        f = get_solution("n_queens")
        assert f(1) == [["Q"]]


class TestSudokuSolver:
    def test_sudoku_basic(self):
        f = get_solution("sudoku_solver")
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        f(board)
        # Check it's solved (no dots)
        for row in board:
            assert "." not in row
