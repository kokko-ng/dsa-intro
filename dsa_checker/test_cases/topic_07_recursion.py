"""
Topic 07: Recursion & Backtracking
"""
from ..types import TestCasesDict

TOPIC_07_TESTS: TestCasesDict = {
    "fibonacci": [
        {"args": [0], "expected": 0, "name": "fib(0)"},
        {"args": [1], "expected": 1, "name": "fib(1)"},
        {"args": [2], "expected": 1, "name": "fib(2)"},
        {"args": [5], "expected": 5, "name": "fib(5)"},
        {"args": [10], "expected": 55, "name": "fib(10)"},
        {"args": [15], "expected": 610, "name": "fib(15)"},
    ],
    "factorial": [
        {"args": [0], "expected": 1, "name": "0!"},
        {"args": [1], "expected": 1, "name": "1!"},
        {"args": [5], "expected": 120, "name": "5!"},
        {"args": [7], "expected": 5040, "name": "7!"},
        {"args": [10], "expected": 3628800, "name": "10!"},
    ],
    "subsets": [
        {"args": [[1, 2, 3]], "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], "name": "three elements", "compare": "set_of_tuples"},
        {"args": [[0]], "expected": [[], [0]], "name": "single element", "compare": "set_of_tuples"},
        {"args": [[]], "expected": [[]], "name": "empty array", "compare": "set_of_tuples"},
        {"args": [[1, 2]], "expected": [[], [1], [2], [1, 2]], "name": "two elements", "compare": "set_of_tuples"},
    ],
    "permutations": [
        {"args": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], "name": "three elements", "compare": "set_of_tuples"},
        {"args": [[0, 1]], "expected": [[0, 1], [1, 0]], "name": "two elements", "compare": "set_of_tuples"},
        {"args": [[1]], "expected": [[1]], "name": "single element", "compare": "set_of_tuples"},
    ],
    "generate_parentheses": [
        {"args": [1], "expected": ["()"], "name": "n=1", "compare": "set"},
        {"args": [2], "expected": ["(())", "()()"], "name": "n=2", "compare": "set"},
        {"args": [3], "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"], "name": "n=3", "compare": "set"},
    ],
    "combination_sum": [
        {"args": [[2, 3, 6, 7], 7], "expected": [[2, 2, 3], [7]], "name": "basic case", "compare": "set_of_tuples"},
        {"args": [[2, 3, 5], 8], "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]], "name": "multiple combos", "compare": "set_of_tuples"},
        {"args": [[2], 1], "expected": [], "name": "impossible"},
    ],
    "letter_combinations": [
        {"args": ["23"], "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "name": "basic case", "compare": "set"},
        {"args": [""], "expected": [], "name": "empty input"},
        {"args": ["2"], "expected": ["a", "b", "c"], "name": "single digit", "compare": "set"},
    ],
    "word_search": [
        {"args": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"], "expected": True, "name": "basic found"},
        {"args": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"], "expected": True, "name": "another path"},
        {"args": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"], "expected": False, "name": "cannot reuse"},
    ],
    "n_queens": [
        {"args": [1], "expected": [["Q"]], "name": "n=1", "compare": "set_of_tuples"},
        {"args": [4], "expected": [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]], "name": "n=4", "compare": "set_of_tuples"},
    ],
}
