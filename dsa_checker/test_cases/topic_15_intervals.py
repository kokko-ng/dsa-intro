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
    "interval_list_intersections": [
        {"args": [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]], "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], "name": "basic case"},
        {"args": [[[1, 3], [5, 9]], []], "expected": [], "name": "one empty"},
        {"args": [[], [[4, 8], [10, 12]]], "expected": [], "name": "other empty"},
        {"args": [[[1, 7]], [[3, 10]]], "expected": [[3, 7]], "name": "single overlap"},
    ],
    "video_stitching": [
        {"args": [[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10], "expected": 3, "name": "basic case"},
        {"args": [[[0, 1], [1, 2]], 5], "expected": -1, "name": "impossible"},
        {"args": [[[0, 4], [2, 8]], 5], "expected": 2, "name": "two clips"},
    ],
    "my_calendar_i": [
        {"args": [["book", "book", "book"], [[10, 20], [15, 25], [20, 30]]], "expected": [True, False, True], "name": "basic case", "compare": "calendar_ops"},
        {"args": [["book", "book", "book"], [[10, 20], [20, 30], [30, 40]]], "expected": [True, True, True], "name": "no overlap", "compare": "calendar_ops"},
    ],
    "my_calendar_ii": [
        {"args": [["book", "book", "book", "book", "book", "book"], [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]], "expected": [True, True, True, False, True, True], "name": "basic case", "compare": "calendar_ops"},
    ],
    "remove_interval": [
        {"args": [[[0, 2], [3, 4], [5, 7]], [1, 6]], "expected": [[0, 1], [6, 7]], "name": "basic case"},
        {"args": [[[0, 5]], [2, 3]], "expected": [[0, 2], [3, 5]], "name": "split interval"},
        {"args": [[[0, 4], [3, 5], [7, 10]], [0, 10]], "expected": [], "name": "remove all"},
    ],
    "data_stream_disjoint_intervals": [
        {"args": [["addNum", "addNum", "getIntervals", "addNum", "getIntervals"], [[1], [3], [], [2], []]], "expected": [None, None, [[1, 1], [3, 3]], None, [[1, 3]]], "name": "basic case", "compare": "stream_interval_ops"},
    ],
    "range_module": [
        {"args": [["addRange", "queryRange", "removeRange", "queryRange"], [[10, 20], [14, 16], [14, 16], [14, 16]]], "expected": [None, True, None, False], "name": "basic case", "compare": "range_module_ops"},
    ],
    "count_covered_buildings": [
        {"args": [[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]], "expected": [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]], "name": "basic case"},
    ],
    "summary_ranges": [
        {"args": [[0, 1, 2, 4, 5, 7]], "expected": ["0->2", "4->5", "7"], "name": "basic case"},
        {"args": [[0, 2, 3, 4, 6, 8, 9]], "expected": ["0", "2->4", "6", "8->9"], "name": "mixed"},
        {"args": [[]], "expected": [], "name": "empty"},
        {"args": [[-1]], "expected": ["-1"], "name": "single negative"},
    ],
    "find_right_interval": [
        {"args": [[[1, 2]]], "expected": [-1], "name": "single interval"},
        {"args": [[[3, 4], [2, 3], [1, 2]]], "expected": [-1, 0, 1], "name": "basic case"},
        {"args": [[[1, 4], [2, 3], [3, 4]]], "expected": [-1, 2, -1], "name": "another case"},
    ],
    "add_bold_tag": [
        {"args": ["abcxyz123", ["abc", "123"]], "expected": "<b>abc</b>xyz<b>123</b>", "name": "basic case"},
        {"args": ["aaabbcc", ["aaa", "aab", "bc"]], "expected": "<b>aaabbc</b>c", "name": "overlapping"},
    ],
}
