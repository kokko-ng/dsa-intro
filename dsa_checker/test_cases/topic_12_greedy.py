"""
Topic 12: Greedy Algorithms
"""

from ..types import TestCasesDict

TOPIC_12_TESTS: TestCasesDict = {
    "jump_game": [
        {"args": [[2, 3, 1, 1, 4]], "expected": True, "name": "can reach end"},
        {"args": [[3, 2, 1, 0, 4]], "expected": False, "name": "stuck at zero"},
        {"args": [[0]], "expected": True, "name": "single element"},
        {"args": [[2, 0, 0]], "expected": True, "name": "jump over zeros"},
        {"args": [[1, 1, 1, 1]], "expected": True, "name": "all ones"},
        {"args": [[1, 0, 1, 0]], "expected": False, "name": "stuck in middle"},
    ],
    "jump_game_ii": [
        {"args": [[2, 3, 1, 1, 4]], "expected": 2, "name": "basic case"},
        {"args": [[2, 3, 0, 1, 4]], "expected": 2, "name": "with zero"},
        {"args": [[1]], "expected": 0, "name": "single element"},
        {"args": [[1, 2]], "expected": 1, "name": "two elements"},
        {"args": [[1, 1, 1, 1]], "expected": 3, "name": "all ones"},
    ],
    "gas_station": [
        {
            "args": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
            "expected": 3,
            "name": "basic case",
        },
        {"args": [[2, 3, 4], [3, 4, 3]], "expected": -1, "name": "impossible"},
        {
            "args": [[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]],
            "expected": 4,
            "name": "start at end",
        },
        {"args": [[5], [4]], "expected": 0, "name": "single station"},
    ],
    "candy": [
        {"args": [[1, 0, 2]], "expected": 5, "name": "basic case"},
        {"args": [[1, 2, 2]], "expected": 4, "name": "plateau"},
        {"args": [[1, 3, 2, 2, 1]], "expected": 7, "name": "complex"},
        {"args": [[1]], "expected": 1, "name": "single child"},
    ],
    "partition_labels": [
        {
            "args": ["ababcbacadefegdehijhklij"],
            "expected": [9, 7, 8],
            "name": "basic case",
        },
        {"args": ["eccbbbbdec"], "expected": [10], "name": "single partition"},
        {"args": ["abc"], "expected": [1, 1, 1], "name": "all unique"},
    ],
    "valid_parenthesis_string": [
        {"args": ["()"], "expected": True, "name": "simple valid"},
        {"args": ["(*)"], "expected": True, "name": "with star"},
        {"args": ["(*))"], "expected": True, "name": "star as open"},
        {"args": ["((*)"], "expected": True, "name": "star as close"},
        {"args": [")("], "expected": False, "name": "invalid order"},
    ],
    "maximum_subarray_greedy": [
        {
            "args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]],
            "expected": 6,
            "name": "standard case",
        },
        {"args": [[1]], "expected": 1, "name": "single element"},
        {"args": [[5, 4, -1, 7, 8]], "expected": 23, "name": "mostly positive"},
        {"args": [[-1]], "expected": -1, "name": "single negative"},
        {"args": [[-2, -1]], "expected": -1, "name": "all negative"},
    ],
    "assign_cookies": [
        {"args": [[1, 2, 3], [1, 1]], "expected": 1, "name": "not enough cookies"},
        {"args": [[1, 2], [1, 2, 3]], "expected": 2, "name": "all satisfied"},
        {"args": [[10, 9, 8, 7], [5, 6, 7, 8]], "expected": 2, "name": "partial match"},
    ],
    "lemonade_change": [
        {"args": [[5, 5, 5, 10, 20]], "expected": True, "name": "basic case"},
        {"args": [[5, 5, 10, 10, 20]], "expected": False, "name": "not enough change"},
        {"args": [[5, 5, 10]], "expected": True, "name": "simple case"},
        {"args": [[10, 10]], "expected": False, "name": "no fives"},
    ],
    "queue_reconstruction": [
        {
            "args": [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]],
            "expected": [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
            "name": "basic case",
        },
        {
            "args": [[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]],
            "expected": [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
            "name": "another case",
        },
    ],
    "minimum_platforms": [
        {
            "args": [
                [900, 940, 950, 1100, 1500, 1800],
                [910, 1200, 1120, 1130, 1900, 2000],
            ],
            "expected": 3,
            "name": "basic case",
        },
        {
            "args": [[100, 200, 300], [110, 210, 310]],
            "expected": 1,
            "name": "no overlap",
        },
        {"args": [[100, 100, 100], [200, 200, 200]], "expected": 3, "name": "all same"},
    ],
    "min_arrows_burst_balloons": [
        {
            "args": [[[10, 16], [2, 8], [1, 6], [7, 12]]],
            "expected": 2,
            "name": "basic case",
        },
        {
            "args": [[[1, 2], [3, 4], [5, 6], [7, 8]]],
            "expected": 4,
            "name": "no overlap",
        },
        {"args": [[[1, 2], [2, 3], [3, 4], [4, 5]]], "expected": 2, "name": "touching"},
    ],
    "remove_covered_intervals": [
        {"args": [[[1, 4], [3, 6], [2, 8]]], "expected": 2, "name": "one covered"},
        {"args": [[[1, 4], [2, 3]]], "expected": 1, "name": "second covered"},
        {"args": [[[1, 2], [1, 4], [3, 4]]], "expected": 1, "name": "multiple covered"},
    ],
    "broken_calculator": [
        {"args": [2, 3], "expected": 2, "name": "basic case"},
        {"args": [5, 8], "expected": 2, "name": "double and decrement"},
        {"args": [3, 10], "expected": 3, "name": "another case"},
        {"args": [1, 1], "expected": 0, "name": "already equal"},
    ],
    "two_city_scheduling": [
        {
            "args": [[[10, 20], [30, 200], [400, 50], [30, 20]]],
            "expected": 110,
            "name": "basic case",
        },
        {
            "args": [
                [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
            ],
            "expected": 1859,
            "name": "larger case",
        },
    ],
    "max_units_on_truck": [
        {"args": [[[1, 3], [2, 2], [3, 1]], 4], "expected": 8, "name": "basic case"},
        {
            "args": [[[5, 10], [2, 5], [4, 7], [3, 9]], 10],
            "expected": 91,
            "name": "larger case",
        },
    ],
    "wiggle_subsequence": [
        {"args": [[1, 7, 4, 9, 2, 5]], "expected": 6, "name": "basic case"},
        {
            "args": [[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]],
            "expected": 7,
            "name": "longer",
        },
        {"args": [[1, 2, 3, 4, 5, 6, 7, 8, 9]], "expected": 2, "name": "monotonic"},
    ],
}
