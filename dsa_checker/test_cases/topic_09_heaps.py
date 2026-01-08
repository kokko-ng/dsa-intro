"""
Topic 09: Heaps & Priority Queues
"""

from ..types import TestCasesDict

TOPIC_09_TESTS: TestCasesDict = {
    "kth_largest_element": [
        {"args": [[3, 2, 1, 5, 6, 4], 2], "expected": 5, "name": "k=2"},
        {
            "args": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
            "expected": 4,
            "name": "k=4 with duplicates",
        },
        {"args": [[1], 1], "expected": 1, "name": "single element"},
        {"args": [[2, 1], 2], "expected": 1, "name": "k equals length"},
        {
            "args": [[7, 6, 5, 4, 3, 2, 1], 5],
            "expected": 3,
            "name": "sorted descending",
        },
        {"args": [[-1, -2, -3, -4], 2], "expected": -2, "name": "negative numbers"},
    ],
    "merge_k_lists": [
        {
            "args": [[[1, 4, 5], [1, 3, 4], [2, 6]]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6],
            "name": "three lists",
            "input_type": "k_linked_lists",
            "output_type": "linked_list_to_list",
        },
        {
            "args": [[[]]],
            "expected": [],
            "name": "empty lists",
            "input_type": "k_linked_lists",
            "output_type": "linked_list_to_list",
        },
        {
            "args": [[]],
            "expected": [],
            "name": "no lists",
            "input_type": "k_linked_lists",
            "output_type": "linked_list_to_list",
        },
        {
            "args": [[[1]]],
            "expected": [1],
            "name": "single list single element",
            "input_type": "k_linked_lists",
            "output_type": "linked_list_to_list",
        },
    ],
    "top_k_frequent_elements": [
        {
            "args": [[1, 1, 1, 2, 2, 3], 2],
            "expected": [1, 2],
            "name": "basic case",
            "compare": "set",
        },
        {"args": [[1], 1], "expected": [1], "name": "single element"},
        {
            "args": [[1, 2], 2],
            "expected": [1, 2],
            "name": "k equals unique count",
            "compare": "set",
        },
        {
            "args": [[4, 1, -1, 2, -1, 2, 3], 2],
            "expected": [-1, 2],
            "name": "with negatives",
            "compare": "set",
        },
    ],
    "find_median": [
        {
            "args": [[1, 2]],
            "expected": 1.5,
            "name": "two elements",
            "compare": "median_finder",
        },
        {
            "args": [[1, 2, 3]],
            "expected": 2.0,
            "name": "three elements",
            "compare": "median_finder",
        },
        {
            "args": [[1]],
            "expected": 1.0,
            "name": "single element",
            "compare": "median_finder",
        },
        {
            "args": [[2, 1, 3, 4]],
            "expected": 2.5,
            "name": "four elements",
            "compare": "median_finder",
        },
        {
            "args": [[-1, -2, -3]],
            "expected": -2.0,
            "name": "negative numbers",
            "compare": "median_finder",
        },
        {
            "args": [[5, 5, 5, 5]],
            "expected": 5.0,
            "name": "all duplicates",
            "compare": "median_finder",
        },
    ],
    "k_closest_points": [
        {
            "args": [[[1, 3], [-2, 2]], 1],
            "expected": [[-2, 2]],
            "name": "k=1",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[3, 3], [5, -1], [-2, 4]], 2],
            "expected": [[3, 3], [-2, 4]],
            "name": "k=2",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[0, 1], [1, 0]], 2],
            "expected": [[0, 1], [1, 0]],
            "name": "same distance",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[5, 5]], 1],
            "expected": [[5, 5]],
            "name": "single point",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[-1, -2], [1, 2], [0, 0]], 2],
            "expected": [[0, 0], [-1, -2]],
            "name": "with negatives and origin",
            "compare": "set_of_tuples",
        },
    ],
    "reorganize_string": [
        {
            "args": ["aab"],
            "expected": "aba",
            "name": "basic case",
            "compare": "reorganized",
        },
        {"args": ["aaab"], "expected": "", "name": "impossible"},
        {"args": ["a"], "expected": "a", "name": "single char"},
        {
            "args": ["aabb"],
            "expected": "abab",
            "name": "equal counts",
            "compare": "reorganized",
        },
        {"args": ["aa"], "expected": "", "name": "two same chars impossible"},
        {
            "args": ["vvvlo"],
            "expected": "vlvov",
            "name": "three same chars possible",
            "compare": "reorganized",
        },
    ],
    "task_scheduler": [
        {"args": [["A", "A", "A", "B", "B", "B"], 2], "expected": 8, "name": "n=2"},
        {
            "args": [["A", "A", "A", "B", "B", "B"], 0],
            "expected": 6,
            "name": "n=0 no cooldown",
        },
        {
            "args": [["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2],
            "expected": 16,
            "name": "many A's",
        },
        {"args": [["A"], 2], "expected": 1, "name": "single task"},
        {
            "args": [["A", "B", "C", "D", "E", "F"], 2],
            "expected": 6,
            "name": "many types no idle needed",
        },
    ],
    "last_stone_weight": [
        {"args": [[2, 7, 4, 1, 8, 1]], "expected": 1, "name": "basic case"},
        {"args": [[1]], "expected": 1, "name": "single stone"},
        {"args": [[2, 2]], "expected": 0, "name": "equal stones"},
        {"args": [[10, 4, 2, 10]], "expected": 2, "name": "two equal largest"},
    ],
    "kth_smallest_matrix": [
        {
            "args": [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8],
            "expected": 13,
            "name": "basic case",
        },
        {"args": [[[-5]], 1], "expected": -5, "name": "single element"},
        {"args": [[[1, 2], [1, 3]], 2], "expected": 1, "name": "duplicate values"},
    ],
    "sort_nearly_sorted": [
        {
            "args": [[3, 2, 1, 5, 4, 6], 2],
            "expected": [1, 2, 3, 4, 5, 6],
            "name": "k=2",
        },
        {
            "args": [[6, 5, 3, 2, 8, 10, 9], 3],
            "expected": [2, 3, 5, 6, 8, 9, 10],
            "name": "k=3",
        },
        {"args": [[1, 2, 3], 1], "expected": [1, 2, 3], "name": "already sorted"},
    ],
    "find_k_pairs_smallest_sums": [
        {
            "args": [[1, 7, 11], [2, 4, 6], 3],
            "expected": [[1, 2], [1, 4], [1, 6]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1, 1, 2], [1, 2, 3], 2],
            "expected": [[1, 1], [1, 1]],
            "name": "duplicates",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1, 2], [3], 3],
            "expected": [[1, 3], [2, 3]],
            "name": "less pairs",
            "compare": "set_of_tuples",
        },
    ],
    "smallest_range_covering_k_lists": [
        {
            "args": [[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]],
            "expected": [20, 24],
            "name": "basic case",
        },
        {
            "args": [[[1, 2, 3], [1, 2, 3], [1, 2, 3]]],
            "expected": [1, 1],
            "name": "same elements",
        },
    ],
    "sliding_window_maximum": [
        {
            "args": [[1, 3, -1, -3, 5, 3, 6, 7], 3],
            "expected": [3, 3, 5, 5, 6, 7],
            "name": "basic case",
        },
        {"args": [[1], 1], "expected": [1], "name": "single element"},
        {"args": [[1, -1], 1], "expected": [1, -1], "name": "window size 1"},
        {"args": [[7, 2, 4], 2], "expected": [7, 4], "name": "window size 2"},
    ],
    "kth_largest_stream": [
        {
            "args": [3, [4, 5, 8, 2], [[3], [5], [10], [9], [4]]],
            "expected": [4, 5, 5, 8, 8],
            "name": "basic case",
            "compare": "kth_largest_ops",
        },
    ],
    "ugly_number_ii": [
        {"args": [10], "expected": 12, "name": "n=10"},
        {"args": [1], "expected": 1, "name": "n=1"},
        {"args": [15], "expected": 24, "name": "n=15"},
    ],
    "find_max_min_pair": [
        {"args": [[3, 5, 1, 2, 4, 8]], "expected": [1, 8], "name": "basic case"},
        {"args": [[1]], "expected": [1, 1], "name": "single element"},
        {"args": [[2, 2, 2]], "expected": [2, 2], "name": "all same"},
    ],
    "top_k_words": [
        {
            "args": [["i", "love", "leetcode", "i", "love", "coding"], 2],
            "expected": ["i", "love"],
            "name": "basic case",
        },
        {
            "args": [
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4,
            ],
            "expected": ["the", "is", "sunny", "day"],
            "name": "more words",
        },
    ],
}
