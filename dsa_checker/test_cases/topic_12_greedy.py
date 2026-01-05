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
        {"args": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]], "expected": 3, "name": "basic case"},
        {"args": [[2, 3, 4], [3, 4, 3]], "expected": -1, "name": "impossible"},
        {"args": [[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]], "expected": 4, "name": "start at end"},
        {"args": [[5], [4]], "expected": 0, "name": "single station"},
    ],
    "candy": [
        {"args": [[1, 0, 2]], "expected": 5, "name": "basic case"},
        {"args": [[1, 2, 2]], "expected": 4, "name": "plateau"},
        {"args": [[1, 3, 2, 2, 1]], "expected": 7, "name": "complex"},
        {"args": [[1]], "expected": 1, "name": "single child"},
    ],
    "partition_labels": [
        {"args": ["ababcbacadefegdehijhklij"], "expected": [9, 7, 8], "name": "basic case"},
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
}
