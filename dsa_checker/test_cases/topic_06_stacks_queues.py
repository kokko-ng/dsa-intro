"""
Topic 06: Stacks & Queues
"""

TOPIC_06_TESTS = {
    "valid_parentheses": [
        {"args": ["()"], "expected": True, "name": "simple pair"},
        {"args": ["()[]{}"], "expected": True, "name": "multiple types"},
        {"args": ["(]"], "expected": False, "name": "mismatched"},
        {"args": ["([)]"], "expected": False, "name": "interleaved wrong"},
        {"args": ["{[]}"], "expected": True, "name": "nested"},
        {"args": [""], "expected": True, "name": "empty string"},
        {"args": ["("], "expected": False, "name": "single open"},
        {"args": [")"], "expected": False, "name": "single close"},
        {"args": ["((()))"], "expected": True, "name": "deeply nested"},
    ],
    "evaluate_rpn": [
        {"args": [["2", "1", "+", "3", "*"]], "expected": 9, "name": "basic expression"},
        {"args": [["4", "13", "5", "/", "+"]], "expected": 6, "name": "with division"},
        {"args": [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], "expected": 22, "name": "complex"},
        {"args": [["3"]], "expected": 3, "name": "single number"},
        {"args": [["3", "4", "+"]], "expected": 7, "name": "simple addition"},
        {"args": [["3", "4", "-"]], "expected": -1, "name": "simple subtraction"},
    ],
    "daily_temperatures": [
        {"args": [[73, 74, 75, 71, 69, 72, 76, 73]], "expected": [1, 1, 4, 2, 1, 1, 0, 0], "name": "basic case"},
        {"args": [[30, 40, 50, 60]], "expected": [1, 1, 1, 0], "name": "increasing"},
        {"args": [[60, 50, 40, 30]], "expected": [0, 0, 0, 0], "name": "decreasing"},
        {"args": [[30]], "expected": [0], "name": "single element"},
        {"args": [[30, 30, 30]], "expected": [0, 0, 0], "name": "all same"},
    ],
    "next_greater_element": [
        {"args": [[4, 1, 2], [1, 3, 4, 2]], "expected": [-1, 3, -1], "name": "basic case"},
        {"args": [[2, 4], [1, 2, 3, 4]], "expected": [3, -1], "name": "simple case"},
        {"args": [[1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]], "expected": [7, 7, 7, 7, 7], "name": "all have greater"},
    ],
    "simplify_path": [
        {"args": ["/home/"], "expected": "/home", "name": "trailing slash"},
        {"args": ["/../"], "expected": "/", "name": "go above root"},
        {"args": ["/home//foo/"], "expected": "/home/foo", "name": "double slash"},
        {"args": ["/a/./b/../../c/"], "expected": "/c", "name": "complex path"},
        {"args": ["/"], "expected": "/", "name": "root only"},
    ],
    "largest_rectangle_histogram": [
        {"args": [[2, 1, 5, 6, 2, 3]], "expected": 10, "name": "basic case"},
        {"args": [[2, 4]], "expected": 4, "name": "two bars"},
        {"args": [[1]], "expected": 1, "name": "single bar"},
        {"args": [[1, 1, 1, 1]], "expected": 4, "name": "all same"},
        {"args": [[6, 2, 5, 4, 5, 1, 6]], "expected": 12, "name": "complex"},
    ],
}
