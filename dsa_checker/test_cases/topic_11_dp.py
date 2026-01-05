"""
Topic 11: Dynamic Programming
"""

from ..types import TestCasesDict

TOPIC_11_TESTS: TestCasesDict = {
    "climbing_stairs": [
        {"args": [1], "expected": 1, "name": "one step"},
        {"args": [2], "expected": 2, "name": "two steps"},
        {"args": [3], "expected": 3, "name": "three steps"},
        {"args": [4], "expected": 5, "name": "four steps"},
        {"args": [5], "expected": 8, "name": "five steps"},
        {"args": [10], "expected": 89, "name": "ten steps"},
    ],
    "house_robber": [
        {"args": [[1, 2, 3, 1]], "expected": 4, "name": "basic case"},
        {"args": [[2, 7, 9, 3, 1]], "expected": 12, "name": "longer array"},
        {"args": [[1]], "expected": 1, "name": "single house"},
        {"args": [[1, 2]], "expected": 2, "name": "two houses"},
        {"args": [[2, 1, 1, 2]], "expected": 4, "name": "skip middle"},
        {"args": [[0, 0, 0]], "expected": 0, "name": "all zeros"},
    ],
    "coin_change": [
        {"args": [[1, 2, 5], 11], "expected": 3, "name": "basic case"},
        {"args": [[2], 3], "expected": -1, "name": "impossible"},
        {"args": [[1], 0], "expected": 0, "name": "zero amount"},
        {"args": [[1], 1], "expected": 1, "name": "exact coin"},
        {"args": [[1, 2, 5], 100], "expected": 20, "name": "larger amount"},
        {"args": [[2, 5, 10], 3], "expected": -1, "name": "no solution"},
    ],
    "longest_increasing_subsequence": [
        {"args": [[10, 9, 2, 5, 3, 7, 101, 18]], "expected": 4, "name": "basic case"},
        {"args": [[0, 1, 0, 3, 2, 3]], "expected": 4, "name": "with duplicates"},
        {"args": [[7, 7, 7, 7, 7]], "expected": 1, "name": "all same"},
        {"args": [[1, 2, 3, 4, 5]], "expected": 5, "name": "already sorted"},
        {"args": [[5, 4, 3, 2, 1]], "expected": 1, "name": "decreasing"},
    ],
    "unique_paths": [
        {"args": [3, 7], "expected": 28, "name": "3x7 grid"},
        {"args": [3, 2], "expected": 3, "name": "3x2 grid"},
        {"args": [1, 1], "expected": 1, "name": "1x1 grid"},
        {"args": [1, 5], "expected": 1, "name": "single row"},
        {"args": [5, 1], "expected": 1, "name": "single column"},
        {"args": [3, 3], "expected": 6, "name": "3x3 grid"},
    ],
    "word_break": [
        {
            "args": ["leetcode", ["leet", "code"]],
            "expected": True,
            "name": "basic true",
        },
        {
            "args": ["applepenapple", ["apple", "pen"]],
            "expected": True,
            "name": "word reuse",
        },
        {
            "args": ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
            "expected": False,
            "name": "cannot break",
        },
        {"args": ["a", ["a"]], "expected": True, "name": "single char"},
        {"args": ["", []], "expected": True, "name": "empty string"},
        {
            "args": ["aaaaaaa", ["aaaa", "aaa"]],
            "expected": True,
            "name": "multiple ways",
        },
    ],
    "longest_common_subsequence": [
        {"args": ["abcde", "ace"], "expected": 3, "name": "basic case"},
        {"args": ["abc", "abc"], "expected": 3, "name": "identical"},
        {"args": ["abc", "def"], "expected": 0, "name": "no common"},
        {"args": ["", "abc"], "expected": 0, "name": "empty string"},
        {"args": ["abcba", "abcbcba"], "expected": 5, "name": "longer strings"},
    ],
    "edit_distance": [
        {"args": ["horse", "ros"], "expected": 3, "name": "basic case"},
        {"args": ["intention", "execution"], "expected": 5, "name": "longer strings"},
        {"args": ["", "abc"], "expected": 3, "name": "empty to string"},
        {"args": ["abc", ""], "expected": 3, "name": "string to empty"},
        {"args": ["abc", "abc"], "expected": 0, "name": "identical"},
    ],
    "decode_ways": [
        {"args": ["12"], "expected": 2, "name": "basic case"},
        {"args": ["226"], "expected": 3, "name": "three ways"},
        {"args": ["06"], "expected": 0, "name": "leading zero"},
        {"args": ["11106"], "expected": 2, "name": "complex"},
        {"args": ["0"], "expected": 0, "name": "just zero"},
    ],
    "max_product_subarray": [
        {"args": [[2, 3, -2, 4]], "expected": 6, "name": "basic case"},
        {"args": [[-2, 0, -1]], "expected": 0, "name": "with zero"},
        {"args": [[-2, 3, -4]], "expected": 24, "name": "negative times negative"},
        {"args": [[2]], "expected": 2, "name": "single element"},
        {"args": [[-2]], "expected": -2, "name": "single negative"},
    ],
    "min_path_sum": [
        {
            "args": [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]],
            "expected": 7,
            "name": "basic case",
        },
        {"args": [[[1, 2, 3], [4, 5, 6]]], "expected": 12, "name": "rectangular"},
        {"args": [[[1]]], "expected": 1, "name": "single cell"},
    ],
    "triangle": [
        {
            "args": [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]],
            "expected": 11,
            "name": "basic case",
        },
        {"args": [[[-10]]], "expected": -10, "name": "single element"},
        {
            "args": [[[-1], [2, 3], [1, -1, -3]]],
            "expected": -1,
            "name": "with negatives",
        },
    ],
    "perfect_squares": [
        {"args": [12], "expected": 3, "name": "12 = 4+4+4"},
        {"args": [13], "expected": 2, "name": "13 = 4+9"},
        {"args": [1], "expected": 1, "name": "already perfect"},
        {"args": [7], "expected": 4, "name": "7 = 1+1+1+4"},
    ],
    "partition_equal_subset_sum": [
        {"args": [[1, 5, 11, 5]], "expected": True, "name": "can partition"},
        {"args": [[1, 2, 3, 5]], "expected": False, "name": "cannot partition"},
        {"args": [[1, 1]], "expected": True, "name": "two equal"},
        {"args": [[2, 2, 2]], "expected": True, "name": "odd count even sum"},
    ],
    "target_sum": [
        {"args": [[1, 1, 1, 1, 1], 3], "expected": 5, "name": "basic case"},
        {"args": [[1], 1], "expected": 1, "name": "single element"},
        {"args": [[1, 0], 1], "expected": 2, "name": "with zero"},
    ],
    "longest_palindromic_subsequence": [
        {"args": ["bbbab"], "expected": 4, "name": "basic case"},
        {"args": ["cbbd"], "expected": 2, "name": "bb"},
        {"args": ["a"], "expected": 1, "name": "single char"},
        {"args": ["abcdef"], "expected": 1, "name": "no palindrome"},
    ],
    "coin_change_ii": [
        {"args": [5, [1, 2, 5]], "expected": 4, "name": "basic case"},
        {"args": [3, [2]], "expected": 0, "name": "impossible"},
        {"args": [10, [10]], "expected": 1, "name": "exact match"},
    ],
    "house_robber_ii": [
        {"args": [[2, 3, 2]], "expected": 3, "name": "basic case"},
        {"args": [[1, 2, 3, 1]], "expected": 4, "name": "skip first or last"},
        {"args": [[1, 2, 3]], "expected": 3, "name": "pick middle"},
        {"args": [[1]], "expected": 1, "name": "single house"},
    ],
    "minimum_falling_path": [
        {
            "args": [[[2, 1, 3], [6, 5, 4], [7, 8, 9]]],
            "expected": 13,
            "name": "basic case",
        },
        {"args": [[[-19, 57], [-40, -5]]], "expected": -59, "name": "with negatives"},
        {"args": [[[1]]], "expected": 1, "name": "single cell"},
    ],
    "count_palindromic_substrings": [
        {"args": ["abc"], "expected": 3, "name": "no palindromes"},
        {"args": ["aaa"], "expected": 6, "name": "all palindromes"},
        {"args": ["aba"], "expected": 4, "name": "with center palindrome"},
    ],
    "maximal_square": [
        {
            "args": [
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ],
            "expected": 4,
            "name": "basic case",
        },
        {"args": [[["0", "1"], ["1", "0"]]], "expected": 1, "name": "no larger square"},
        {"args": [[["0"]]], "expected": 0, "name": "single zero"},
    ],
    "integer_break": [
        {"args": [2], "expected": 1, "name": "n=2"},
        {"args": [10], "expected": 36, "name": "n=10"},
        {"args": [8], "expected": 18, "name": "n=8"},
    ],
    "min_cost_climbing_stairs": [
        {"args": [[10, 15, 20]], "expected": 15, "name": "basic case"},
        {
            "args": [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]],
            "expected": 6,
            "name": "longer",
        },
        {"args": [[0, 0, 0, 1]], "expected": 0, "name": "with zeros"},
    ],
    "delete_and_earn": [
        {"args": [[3, 4, 2]], "expected": 6, "name": "basic case"},
        {"args": [[2, 2, 3, 3, 3, 4]], "expected": 9, "name": "duplicates"},
        {"args": [[1]], "expected": 1, "name": "single element"},
    ],
    "longest_palindrome_substring": [
        {"args": ["babad"], "expected": "bab", "name": "basic case"},
        {"args": ["cbbd"], "expected": "bb", "name": "even length"},
        {"args": ["a"], "expected": "a", "name": "single char"},
        {"args": ["ac"], "expected": "a", "name": "no palindrome"},
    ],
}
