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
        {
            "args": [[1, 2, 3]],
            "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
            "name": "three elements",
            "compare": "set_of_tuples",
        },
        {
            "args": [[0]],
            "expected": [[], [0]],
            "name": "single element",
            "compare": "set_of_tuples",
        },
        {
            "args": [[]],
            "expected": [[]],
            "name": "empty array",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1, 2]],
            "expected": [[], [1], [2], [1, 2]],
            "name": "two elements",
            "compare": "set_of_tuples",
        },
    ],
    "permutations": [
        {
            "args": [[1, 2, 3]],
            "expected": [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
            "name": "three elements",
            "compare": "set_of_tuples",
        },
        {
            "args": [[0, 1]],
            "expected": [[0, 1], [1, 0]],
            "name": "two elements",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1]],
            "expected": [[1]],
            "name": "single element",
            "compare": "set_of_tuples",
        },
    ],
    "generate_parentheses": [
        {"args": [1], "expected": ["()"], "name": "n=1", "compare": "set"},
        {"args": [2], "expected": ["(())", "()()"], "name": "n=2", "compare": "set"},
        {
            "args": [3],
            "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"],
            "name": "n=3",
            "compare": "set",
        },
    ],
    "combination_sum": [
        {
            "args": [[2, 3, 6, 7], 7],
            "expected": [[2, 2, 3], [7]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": [[2, 3, 5], 8],
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            "name": "multiple combos",
            "compare": "set_of_tuples",
        },
        {"args": [[2], 1], "expected": [], "name": "impossible"},
    ],
    "letter_combinations": [
        {
            "args": ["23"],
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            "name": "basic case",
            "compare": "set",
        },
        {"args": [""], "expected": [], "name": "empty input"},
        {
            "args": ["2"],
            "expected": ["a", "b", "c"],
            "name": "single digit",
            "compare": "set",
        },
    ],
    "word_search": [
        {
            "args": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
            ],
            "expected": True,
            "name": "basic found",
        },
        {
            "args": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "SEE",
            ],
            "expected": True,
            "name": "another path",
        },
        {
            "args": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
            ],
            "expected": False,
            "name": "cannot reuse",
        },
    ],
    "n_queens": [
        {"args": [1], "expected": [["Q"]], "name": "n=1", "compare": "set_of_tuples"},
        {
            "args": [4],
            "expected": [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."],
            ],
            "name": "n=4",
            "compare": "set_of_tuples",
        },
    ],
    "sudoku_solver": [
        {
            "args": [
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ],
            "expected": [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
            "name": "standard sudoku",
            "compare": "in_place_grid",
        },
    ],
    "subsets_with_dup": [
        {
            "args": [[1, 2, 2]],
            "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
            "name": "with duplicates",
            "compare": "set_of_tuples",
        },
        {
            "args": [[0]],
            "expected": [[], [0]],
            "name": "single element",
            "compare": "set_of_tuples",
        },
        {
            "args": [[4, 4, 4, 1, 4]],
            "expected": [
                [],
                [1],
                [1, 4],
                [1, 4, 4],
                [1, 4, 4, 4],
                [1, 4, 4, 4, 4],
                [4],
                [4, 4],
                [4, 4, 4],
                [4, 4, 4, 4],
            ],
            "name": "many duplicates",
            "compare": "set_of_tuples",
        },
    ],
    "permutations_ii": [
        {
            "args": [[1, 1, 2]],
            "expected": [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
            "name": "with duplicates",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1, 2, 3]],
            "expected": [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
            "name": "no duplicates",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1]],
            "expected": [[1]],
            "name": "single element",
            "compare": "set_of_tuples",
        },
    ],
    "combinations": [
        {
            "args": [4, 2],
            "expected": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
            "name": "n=4 k=2",
            "compare": "set_of_tuples",
        },
        {
            "args": [3, 3],
            "expected": [[1, 2, 3]],
            "name": "n=k",
            "compare": "set_of_tuples",
        },
        {
            "args": [1, 1],
            "expected": [[1]],
            "name": "n=1 k=1",
            "compare": "set_of_tuples",
        },
    ],
    "combination_sum_ii": [
        {
            "args": [[10, 1, 2, 7, 6, 1, 5], 8],
            "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": [[2, 5, 2, 1, 2], 5],
            "expected": [[1, 2, 2], [5]],
            "name": "duplicates in input",
            "compare": "set_of_tuples",
        },
    ],
    "combination_sum_iii": [
        {
            "args": [3, 7],
            "expected": [[1, 2, 4]],
            "name": "k=3 n=7",
            "compare": "set_of_tuples",
        },
        {
            "args": [3, 9],
            "expected": [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
            "name": "k=3 n=9",
            "compare": "set_of_tuples",
        },
        {
            "args": [2, 18],
            "expected": [],
            "name": "impossible",
            "compare": "set_of_tuples",
        },
    ],
    "restore_ip_addresses": [
        {
            "args": ["25525511135"],
            "expected": ["255.255.11.135", "255.255.111.35"],
            "name": "basic case",
            "compare": "set",
        },
        {
            "args": ["0000"],
            "expected": ["0.0.0.0"],
            "name": "all zeros",
            "compare": "set",
        },
        {
            "args": ["101023"],
            "expected": [
                "1.0.10.23",
                "1.0.102.3",
                "10.1.0.23",
                "10.10.2.3",
                "101.0.2.3",
            ],
            "name": "multiple ways",
            "compare": "set",
        },
    ],
    "palindrome_partitioning": [
        {
            "args": ["aab"],
            "expected": [["a", "a", "b"], ["aa", "b"]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": ["a"],
            "expected": [["a"]],
            "name": "single char",
            "compare": "set_of_tuples",
        },
        {
            "args": ["ab"],
            "expected": [["a", "b"]],
            "name": "no palindrome pairs",
            "compare": "set_of_tuples",
        },
    ],
    "power_of_n": [
        {"args": [2.0, 10], "expected": 1024.0, "name": "positive power"},
        {"args": [2.1, 3], "expected": 9.261, "name": "float base"},
        {"args": [2.0, -2], "expected": 0.25, "name": "negative power"},
        {"args": [1.0, 1000], "expected": 1.0, "name": "one to any power"},
    ],
    "count_and_say": [
        {"args": [1], "expected": "1", "name": "n=1"},
        {"args": [4], "expected": "1211", "name": "n=4"},
        {"args": [5], "expected": "111221", "name": "n=5"},
    ],
    "gray_code": [
        {"args": [2], "expected": [0, 1, 3, 2], "name": "n=2"},
        {"args": [1], "expected": [0, 1], "name": "n=1"},
        {"args": [3], "expected": [0, 1, 3, 2, 6, 7, 5, 4], "name": "n=3"},
    ],
    "different_ways_to_add_parentheses": [
        {
            "args": ["2-1-1"],
            "expected": [0, 2],
            "name": "subtraction",
            "compare": "sorted",
        },
        {
            "args": ["2*3-4*5"],
            "expected": [-34, -14, -10, -10, 10],
            "name": "mixed ops",
            "compare": "sorted",
        },
    ],
}
