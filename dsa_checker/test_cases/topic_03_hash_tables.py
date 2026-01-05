"""
Topic 03: Hash Tables
"""

from ..types import TestCasesDict

TOPIC_03_TESTS: TestCasesDict = {
    "first_unique_char": [
        {"args": ["leetcode"], "expected": 0, "name": "first char unique"},
        {"args": ["loveleetcode"], "expected": 2, "name": "middle unique"},
        {"args": ["aabb"], "expected": -1, "name": "no unique char"},
        {"args": [""], "expected": -1, "name": "empty string"},
        {"args": ["z"], "expected": 0, "name": "single char"},
        {"args": ["aadadaad"], "expected": -1, "name": "all repeated"},
        {"args": ["abcabc"], "expected": -1, "name": "all repeated pattern"},
    ],
    "group_anagrams": [
        {
            "args": [["eat", "tea", "tan", "ate", "nat", "bat"]],
            "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            "name": "basic groups",
            "compare": "set_of_sets",
        },
        {
            "args": [[""]],
            "expected": [[""]],
            "name": "empty string",
            "compare": "set_of_sets",
        },
        {
            "args": [["a"]],
            "expected": [["a"]],
            "name": "single char",
            "compare": "set_of_sets",
        },
        {
            "args": [["abc", "bca", "cab", "xyz"]],
            "expected": [["abc", "bca", "cab"], ["xyz"]],
            "name": "one group plus single",
            "compare": "set_of_sets",
        },
        {
            "args": [["", ""]],
            "expected": [["", ""]],
            "name": "two empty strings",
            "compare": "set_of_sets",
        },
    ],
    "isomorphic_strings": [
        {"args": ["egg", "add"], "expected": True, "name": "basic isomorphic"},
        {"args": ["foo", "bar"], "expected": False, "name": "not isomorphic"},
        {"args": ["paper", "title"], "expected": True, "name": "longer isomorphic"},
        {"args": ["", ""], "expected": True, "name": "empty strings"},
        {"args": ["a", "b"], "expected": True, "name": "single chars"},
        {"args": ["ab", "aa"], "expected": False, "name": "different patterns"},
        {"args": ["badc", "baba"], "expected": False, "name": "mapping conflict"},
    ],
    "word_pattern": [
        {
            "args": ["abba", "dog cat cat dog"],
            "expected": True,
            "name": "basic pattern match",
        },
        {
            "args": ["abba", "dog cat cat fish"],
            "expected": False,
            "name": "pattern mismatch",
        },
        {
            "args": ["aaaa", "dog cat cat dog"],
            "expected": False,
            "name": "word mismatch",
        },
        {
            "args": ["abba", "dog dog dog dog"],
            "expected": False,
            "name": "all same words",
        },
        {"args": ["a", "dog"], "expected": True, "name": "single word"},
        {"args": ["abc", "dog cat fish"], "expected": True, "name": "all different"},
    ],
    "longest_consecutive": [
        {"args": [[100, 4, 200, 1, 3, 2]], "expected": 4, "name": "basic sequence"},
        {
            "args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]],
            "expected": 9,
            "name": "longer sequence",
        },
        {"args": [[]], "expected": 0, "name": "empty array"},
        {"args": [[1]], "expected": 1, "name": "single element"},
        {"args": [[1, 2, 3, 4, 5]], "expected": 5, "name": "all consecutive"},
        {"args": [[5, 4, 3, 2, 1]], "expected": 5, "name": "reverse order"},
        {"args": [[1, 3, 5, 7]], "expected": 1, "name": "no consecutive"},
    ],
    "subarray_sum_equals_k": [
        {"args": [[1, 1, 1], 2], "expected": 2, "name": "basic case"},
        {"args": [[1, 2, 3], 3], "expected": 2, "name": "multiple ways"},
        {"args": [[1], 1], "expected": 1, "name": "single element match"},
        {"args": [[1], 0], "expected": 0, "name": "single element no match"},
        {"args": [[0, 0, 0], 0], "expected": 6, "name": "all zeros"},
        {"args": [[-1, -1, 1], 0], "expected": 1, "name": "negative numbers"},
    ],
    "top_k_frequent": [
        {
            "args": [[1, 1, 1, 2, 2, 3], 2],
            "expected": [1, 2],
            "name": "basic k=2",
            "compare": "set",
        },
        {"args": [[1], 1], "expected": [1], "name": "single element", "compare": "set"},
        {
            "args": [[1, 2], 2],
            "expected": [1, 2],
            "name": "two elements k=2",
            "compare": "set",
        },
        {
            "args": [[4, 1, -1, 2, -1, 2, 3], 2],
            "expected": [-1, 2],
            "name": "with negatives",
            "compare": "set",
        },
        {
            "args": [[3, 3, 3, 1, 1, 2], 1],
            "expected": [3],
            "name": "k=1",
            "compare": "set",
        },
    ],
    "intersection_of_arrays": [
        {
            "args": [[1, 2, 2, 1], [2, 2]],
            "expected": [2],
            "name": "basic intersection",
            "compare": "set",
        },
        {
            "args": [[4, 9, 5], [9, 4, 9, 8, 4]],
            "expected": [4, 9],
            "name": "multiple common",
            "compare": "set",
        },
        {
            "args": [[1, 2, 3], [4, 5, 6]],
            "expected": [],
            "name": "no intersection",
            "compare": "set",
        },
        {
            "args": [[], [1, 2, 3]],
            "expected": [],
            "name": "one empty",
            "compare": "set",
        },
        {
            "args": [[1, 1, 1], [1, 1, 1]],
            "expected": [1],
            "name": "all same",
            "compare": "set",
        },
    ],
    "valid_sudoku": [
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
            "expected": True,
            "name": "valid board",
        },
        {
            "args": [
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
            "expected": False,
            "name": "duplicate in column",
        },
    ],
    "happy_number": [
        {"args": [19], "expected": True, "name": "happy 19"},
        {"args": [2], "expected": False, "name": "not happy 2"},
        {"args": [1], "expected": True, "name": "already 1"},
        {"args": [7], "expected": True, "name": "happy 7"},
        {"args": [116], "expected": False, "name": "not happy 116"},
    ],
    "contains_nearby_duplicate": [
        {"args": [[1, 2, 3, 1], 3], "expected": True, "name": "within k"},
        {"args": [[1, 0, 1, 1], 1], "expected": True, "name": "adjacent"},
        {"args": [[1, 2, 3, 1, 2, 3], 2], "expected": False, "name": "outside k"},
        {"args": [[1, 2, 3, 4], 2], "expected": False, "name": "no duplicates"},
    ],
    "find_duplicate": [
        {"args": [[1, 3, 4, 2, 2]], "expected": 2, "name": "basic case"},
        {"args": [[3, 1, 3, 4, 2]], "expected": 3, "name": "another case"},
        {"args": [[1, 1]], "expected": 1, "name": "two elements"},
        {"args": [[2, 2, 2, 2, 2]], "expected": 2, "name": "all same"},
    ],
    "count_pairs_sum": [
        {"args": [[1, 5, 7, -1], 6], "expected": 2, "name": "basic case"},
        {"args": [[1, 1, 1, 1], 2], "expected": 6, "name": "all same"},
        {"args": [[1, 2, 3], 10], "expected": 0, "name": "no pairs"},
        {"args": [[0, 0, 0], 0], "expected": 3, "name": "zero sum"},
    ],
    "ransom_note": [
        {"args": ["a", "b"], "expected": False, "name": "single char no match"},
        {"args": ["aa", "ab"], "expected": False, "name": "not enough chars"},
        {"args": ["aa", "aab"], "expected": True, "name": "enough chars"},
        {"args": ["", "abc"], "expected": True, "name": "empty ransom"},
    ],
    "jewels_and_stones": [
        {"args": ["aA", "aAAbbbb"], "expected": 3, "name": "basic case"},
        {"args": ["z", "ZZ"], "expected": 0, "name": "case sensitive"},
        {"args": ["abc", "abcabc"], "expected": 6, "name": "all jewels"},
    ],
    "find_common_characters": [
        {
            "args": [["bella", "label", "roller"]],
            "expected": ["e", "l", "l"],
            "name": "basic case",
            "compare": "sorted",
        },
        {
            "args": [["cool", "lock", "cook"]],
            "expected": ["c", "o"],
            "name": "two common",
            "compare": "sorted",
        },
        {"args": [["abc", "def"]], "expected": [], "name": "no common"},
    ],
    "count_elements": [
        {"args": [[1, 2, 3]], "expected": 2, "name": "basic case"},
        {"args": [[1, 1, 3, 3, 5, 5, 7, 7]], "expected": 0, "name": "no consecutive"},
        {"args": [[1, 3, 2, 3, 5, 0]], "expected": 3, "name": "mixed"},
        {"args": [[1, 1, 2, 2]], "expected": 2, "name": "duplicates"},
    ],
    "unique_occurrences": [
        {"args": [[1, 2, 2, 1, 1, 3]], "expected": True, "name": "unique counts"},
        {"args": [[1, 2]], "expected": False, "name": "same counts"},
        {
            "args": [[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]],
            "expected": True,
            "name": "with negatives",
        },
    ],
    "set_mismatch": [
        {"args": [[1, 2, 2, 4]], "expected": [2, 3], "name": "basic case"},
        {"args": [[1, 1]], "expected": [1, 2], "name": "two elements"},
        {"args": [[3, 2, 3, 4, 6, 5]], "expected": [3, 1], "name": "larger"},
    ],
}
