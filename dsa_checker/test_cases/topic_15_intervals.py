"""
Topic 15: Intervals & Sorting Patterns
"""
from ..types import TestCasesDict

TOPIC_15_TESTS: TestCasesDict = {
    "merge_intervals": [
        {"args": [[[1, 3], [2, 6], [8, 10], [15, 18]]], "expected": [[1, 6], [8, 10], [15, 18]], "name": "basic merge"},
        {"args": [[[1, 4], [4, 5]]], "expected": [[1, 5]], "name": "touching intervals"},
        {"args": [[[1, 4], [0, 4]]], "expected": [[0, 4]], "name": "complete overlap"},
        {"args": [[[1, 4]]], "expected": [[1, 4]], "name": "single interval"},
        {"args": [[[1, 4], [0, 0]]], "expected": [[0, 0], [1, 4]], "name": "non overlapping"},
        {"args": [[[1, 4], [2, 3]]], "expected": [[1, 4]], "name": "contained interval"},
    ],
    "insert_interval": [
        {"args": [[[1, 3], [6, 9]], [2, 5]], "expected": [[1, 5], [6, 9]], "name": "basic insert"},
        {"args": [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]], "expected": [[1, 2], [3, 10], [12, 16]], "name": "merge multiple"},
        {"args": [[], [5, 7]], "expected": [[5, 7]], "name": "empty list"},
        {"args": [[[1, 5]], [2, 3]], "expected": [[1, 5]], "name": "contained interval"},
        {"args": [[[1, 5]], [6, 8]], "expected": [[1, 5], [6, 8]], "name": "no overlap after"},
        {"args": [[[3, 5]], [1, 2]], "expected": [[1, 2], [3, 5]], "name": "no overlap before"},
    ],
    "meeting_rooms": [
        {"args": [[[0, 30], [5, 10], [15, 20]]], "expected": False, "name": "overlapping"},
        {"args": [[[7, 10], [2, 4]]], "expected": True, "name": "no overlap"},
        {"args": [[[1, 5], [5, 10]]], "expected": True, "name": "adjacent"},
        {"args": [[]], "expected": True, "name": "no meetings"},
        {"args": [[[1, 2]]], "expected": True, "name": "single meeting"},
    ],
    "meeting_rooms_ii": [
        {"args": [[[0, 30], [5, 10], [15, 20]]], "expected": 2, "name": "two rooms"},
        {"args": [[[7, 10], [2, 4]]], "expected": 1, "name": "one room"},
        {"args": [[[1, 5], [5, 10]]], "expected": 1, "name": "adjacent meetings"},
        {"args": [[[1, 5], [2, 6], [3, 7]]], "expected": 3, "name": "all overlap"},
        {"args": [[]], "expected": 0, "name": "no meetings"},
    ],
    "non_overlapping_intervals": [
        {"args": [[[1, 2], [2, 3], [3, 4], [1, 3]]], "expected": 1, "name": "one removal"},
        {"args": [[[1, 2], [1, 2], [1, 2]]], "expected": 2, "name": "all same"},
        {"args": [[[1, 2], [2, 3]]], "expected": 0, "name": "no removal needed"},
        {"args": [[]], "expected": 0, "name": "empty"},
    ],
    "minimum_number_of_arrows": [
        {"args": [[[10, 16], [2, 8], [1, 6], [7, 12]]], "expected": 2, "name": "basic case"},
        {"args": [[[1, 2], [3, 4], [5, 6], [7, 8]]], "expected": 4, "name": "no overlap"},
        {"args": [[[1, 2], [2, 3], [3, 4], [4, 5]]], "expected": 2, "name": "touching"},
        {"args": [[[1, 2]]], "expected": 1, "name": "single balloon"},
    ],
}
