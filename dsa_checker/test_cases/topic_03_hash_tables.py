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
        {"args": [["eat", "tea", "tan", "ate", "nat", "bat"]], "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], "name": "basic groups", "compare": "set_of_sets"},
        {"args": [[""]], "expected": [[""]], "name": "empty string", "compare": "set_of_sets"},
        {"args": [["a"]], "expected": [["a"]], "name": "single char", "compare": "set_of_sets"},
        {"args": [["abc", "bca", "cab", "xyz"]], "expected": [["abc", "bca", "cab"], ["xyz"]], "name": "one group plus single", "compare": "set_of_sets"},
        {"args": [["", ""]], "expected": [["", ""]], "name": "two empty strings", "compare": "set_of_sets"},
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
        {"args": ["abba", "dog cat cat dog"], "expected": True, "name": "basic pattern match"},
        {"args": ["abba", "dog cat cat fish"], "expected": False, "name": "pattern mismatch"},
        {"args": ["aaaa", "dog cat cat dog"], "expected": False, "name": "word mismatch"},
        {"args": ["abba", "dog dog dog dog"], "expected": False, "name": "all same words"},
        {"args": ["a", "dog"], "expected": True, "name": "single word"},
        {"args": ["abc", "dog cat fish"], "expected": True, "name": "all different"},
    ],
    "longest_consecutive": [
        {"args": [[100, 4, 200, 1, 3, 2]], "expected": 4, "name": "basic sequence"},
        {"args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9, "name": "longer sequence"},
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
        {"args": [[1, 1, 1, 2, 2, 3], 2], "expected": [1, 2], "name": "basic k=2", "compare": "set"},
        {"args": [[1], 1], "expected": [1], "name": "single element", "compare": "set"},
        {"args": [[1, 2], 2], "expected": [1, 2], "name": "two elements k=2", "compare": "set"},
        {"args": [[4, 1, -1, 2, -1, 2, 3], 2], "expected": [-1, 2], "name": "with negatives", "compare": "set"},
        {"args": [[3, 3, 3, 1, 1, 2], 1], "expected": [3], "name": "k=1", "compare": "set"},
    ],
    "intersection_of_arrays": [
        {"args": [[1, 2, 2, 1], [2, 2]], "expected": [2], "name": "basic intersection", "compare": "set"},
        {"args": [[4, 9, 5], [9, 4, 9, 8, 4]], "expected": [4, 9], "name": "multiple common", "compare": "set"},
        {"args": [[1, 2, 3], [4, 5, 6]], "expected": [], "name": "no intersection", "compare": "set"},
        {"args": [[], [1, 2, 3]], "expected": [], "name": "one empty", "compare": "set"},
        {"args": [[1, 1, 1], [1, 1, 1]], "expected": [1], "name": "all same", "compare": "set"},
    ],
}
