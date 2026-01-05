"""
Topic 04: Two Pointers & Sliding Window
"""

TOPIC_04_TESTS = {
    "valid_palindrome": [
        {"args": ["A man, a plan, a canal: Panama"], "expected": True, "name": "classic palindrome"},
        {"args": ["race a car"], "expected": False, "name": "not palindrome"},
        {"args": [" "], "expected": True, "name": "space only"},
        {"args": [""], "expected": True, "name": "empty string"},
        {"args": ["a"], "expected": True, "name": "single char"},
        {"args": ["ab"], "expected": False, "name": "two different chars"},
        {"args": ["aa"], "expected": True, "name": "two same chars"},
        {"args": ["0P"], "expected": False, "name": "alphanumeric"},
    ],
    "two_sum_sorted": [
        {"args": [[2, 7, 11, 15], 9], "expected": [1, 2], "name": "basic case"},
        {"args": [[2, 3, 4], 6], "expected": [1, 3], "name": "skip middle"},
        {"args": [[1, 2], 3], "expected": [1, 2], "name": "two elements"},
        {"args": [[-1, 0], -1], "expected": [1, 2], "name": "with negative"},
        {"args": [[1, 2, 3, 4, 5], 9], "expected": [4, 5], "name": "at end"},
        {"args": [[1, 2, 3, 4, 5], 3], "expected": [1, 2], "name": "at start"},
    ],
    "three_sum": [
        {"args": [[-1, 0, 1, 2, -1, -4]], "expected": [[-1, -1, 2], [-1, 0, 1]], "name": "basic triplets", "compare": "set_of_tuples"},
        {"args": [[0, 1, 1]], "expected": [], "name": "no triplet"},
        {"args": [[0, 0, 0]], "expected": [[0, 0, 0]], "name": "all zeros", "compare": "set_of_tuples"},
        {"args": [[]], "expected": [], "name": "empty array"},
        {"args": [[0]], "expected": [], "name": "single element"},
        {"args": [[-2, 0, 1, 1, 2]], "expected": [[-2, 0, 2], [-2, 1, 1]], "name": "multiple triplets", "compare": "set_of_tuples"},
    ],
    "container_with_most_water": [
        {"args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expected": 49, "name": "basic case"},
        {"args": [[1, 1]], "expected": 1, "name": "two elements"},
        {"args": [[4, 3, 2, 1, 4]], "expected": 16, "name": "same height ends"},
        {"args": [[1, 2, 1]], "expected": 2, "name": "three elements"},
        {"args": [[2, 3, 4, 5, 18, 17, 6]], "expected": 17, "name": "tall in middle"},
    ],
    "max_sum_subarray_k": [
        {"args": [[1, 4, 2, 10, 23, 3, 1, 0, 20], 4], "expected": 39, "name": "basic window"},
        {"args": [[1, 2, 3], 3], "expected": 6, "name": "window equals length"},
        {"args": [[5], 1], "expected": 5, "name": "single element"},
        {"args": [[1, 2, 3, 4, 5], 2], "expected": 9, "name": "window at end"},
        {"args": [[-1, -2, -3, -4], 2], "expected": -3, "name": "all negative"},
    ],
    "longest_substring_without_repeating": [
        {"args": ["abcabcbb"], "expected": 3, "name": "basic case"},
        {"args": ["bbbbb"], "expected": 1, "name": "all same"},
        {"args": ["pwwkew"], "expected": 3, "name": "middle substring"},
        {"args": [""], "expected": 0, "name": "empty string"},
        {"args": [" "], "expected": 1, "name": "single space"},
        {"args": ["au"], "expected": 2, "name": "two different"},
        {"args": ["dvdf"], "expected": 3, "name": "overlapping"},
    ],
    "remove_duplicates_sorted": [
        {"args": [[1, 1, 2]], "expected": 2, "name": "basic case"},
        {"args": [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], "expected": 5, "name": "multiple duplicates"},
        {"args": [[]], "expected": 0, "name": "empty array"},
        {"args": [[1]], "expected": 1, "name": "single element"},
        {"args": [[1, 2, 3]], "expected": 3, "name": "no duplicates"},
    ],
    "minimum_window_substring": [
        {"args": ["ADOBECODEBANC", "ABC"], "expected": "BANC", "name": "basic case"},
        {"args": ["a", "a"], "expected": "a", "name": "single char match"},
        {"args": ["a", "aa"], "expected": "", "name": "impossible"},
        {"args": ["aa", "aa"], "expected": "aa", "name": "exact match"},
    ],
}
