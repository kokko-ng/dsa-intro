"""
Topic 06: Stacks & Queues
"""

from ..types import TestCasesDict

TOPIC_06_TESTS: TestCasesDict = {
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
        {
            "args": [["2", "1", "+", "3", "*"]],
            "expected": 9,
            "name": "basic expression",
        },
        {"args": [["4", "13", "5", "/", "+"]], "expected": 6, "name": "with division"},
        {
            "args": [
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ],
            "expected": 22,
            "name": "complex",
        },
        {"args": [["3"]], "expected": 3, "name": "single number"},
        {"args": [["3", "4", "+"]], "expected": 7, "name": "simple addition"},
        {"args": [["3", "4", "-"]], "expected": -1, "name": "simple subtraction"},
        {"args": [["-3", "4", "+"]], "expected": 1, "name": "negative number"},
        {
            "args": [["6", "-3", "/"]],
            "expected": -2,
            "name": "division with negative truncates toward zero",
        },
        {
            "args": [["-7", "3", "/"]],
            "expected": -2,
            "name": "truncation toward zero not floor",
        },
    ],
    "daily_temperatures": [
        {
            "args": [[73, 74, 75, 71, 69, 72, 76, 73]],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0],
            "name": "basic case",
        },
        {"args": [[30, 40, 50, 60]], "expected": [1, 1, 1, 0], "name": "increasing"},
        {"args": [[60, 50, 40, 30]], "expected": [0, 0, 0, 0], "name": "decreasing"},
        {"args": [[30]], "expected": [0], "name": "single element"},
        {"args": [[30, 30, 30]], "expected": [0, 0, 0], "name": "all same"},
        {"args": [[]], "expected": [], "name": "empty array"},
    ],
    "next_greater_element": [
        {
            "args": [[4, 1, 2], [1, 3, 4, 2]],
            "expected": [-1, 3, -1],
            "name": "basic case",
        },
        {"args": [[2, 4], [1, 2, 3, 4]], "expected": [3, -1], "name": "simple case"},
        {
            "args": [[1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]],
            "expected": [7, 7, 7, 7, 7],
            "name": "all have greater",
        },
        {"args": [[], [1, 2, 3]], "expected": [], "name": "empty nums1"},
        {
            "args": [[1, 2, 3], [1, 2, 3]],
            "expected": [2, 3, -1],
            "name": "nums1 equals nums2",
        },
    ],
    "simplify_path": [
        {"args": ["/home/"], "expected": "/home", "name": "trailing slash"},
        {"args": ["/../"], "expected": "/", "name": "go above root"},
        {"args": ["/home//foo/"], "expected": "/home/foo", "name": "double slash"},
        {"args": ["/a/./b/../../c/"], "expected": "/c", "name": "complex path"},
        {"args": ["/"], "expected": "/", "name": "root only"},
        {"args": ["/a/b/c"], "expected": "/a/b/c", "name": "no special chars"},
        {"args": ["/./././."], "expected": "/", "name": "all current dir"},
        {"args": ["/a/b/../.."], "expected": "/", "name": "back to root"},
        {
            "args": ["/a/.../b"],
            "expected": "/a/.../b",
            "name": "triple dots as dir name",
        },
    ],
    "largest_rectangle_histogram": [
        {"args": [[2, 1, 5, 6, 2, 3]], "expected": 10, "name": "basic case"},
        {"args": [[2, 4]], "expected": 4, "name": "two bars"},
        {"args": [[1]], "expected": 1, "name": "single bar"},
        {"args": [[1, 1, 1, 1]], "expected": 4, "name": "all same"},
        {"args": [[6, 2, 5, 4, 5, 1, 6]], "expected": 12, "name": "complex"},
        {"args": [[]], "expected": 0, "name": "empty array"},
        {"args": [[1, 2, 3, 4, 5]], "expected": 9, "name": "increasing heights"},
        {"args": [[5, 4, 3, 2, 1]], "expected": 9, "name": "decreasing heights"},
        {"args": [[0, 0, 0]], "expected": 0, "name": "all zeros"},
    ],
    "min_stack": [
        {
            "args": [
                ["push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[-2], [0], [-3], [], [], [], []],
            ],
            "expected": [None, None, None, -3, None, 0, -2],
            "name": "basic operations",
            "compare": "stack_ops",
        },
        {
            "args": [["push", "getMin", "push", "getMin"], [[1], [], [-1], []]],
            "expected": [None, 1, None, -1],
            "name": "update min",
            "compare": "stack_ops",
        },
        {
            "args": [
                ["push", "push", "push", "pop", "getMin"],
                [[0], [0], [0], [], []],
            ],
            "expected": [None, None, None, None, 0],
            "name": "duplicate min values",
            "compare": "stack_ops",
        },
    ],
    "implement_queue_with_stacks": [
        {
            "args": [["push", "push", "peek", "pop", "empty"], [[1], [2], [], [], []]],
            "expected": [None, None, 1, 1, False],
            "name": "basic operations",
            "compare": "queue_ops",
        },
        {
            "args": [["push", "pop", "empty"], [[1], [], []]],
            "expected": [None, 1, True],
            "name": "push pop empty",
            "compare": "queue_ops",
        },
        {
            "args": [
                ["push", "push", "pop", "push", "pop", "pop"],
                [[1], [2], [], [3], [], []],
            ],
            "expected": [None, None, 1, None, 2, 3],
            "name": "interleaved push pop",
            "compare": "queue_ops",
        },
        {
            "args": [
                ["push", "push", "push", "pop", "pop", "peek"],
                [[1], [2], [3], [], [], []],
            ],
            "expected": [None, None, None, 1, 2, 3],
            "name": "multiple pops then peek",
            "compare": "queue_ops",
        },
    ],
    "decode_string": [
        {"args": ["3[a]2[bc]"], "expected": "aaabcbc", "name": "basic case"},
        {"args": ["3[a2[c]]"], "expected": "accaccacc", "name": "nested"},
        {"args": ["2[abc]3[cd]ef"], "expected": "abcabccdcdcdef", "name": "mixed"},
        {"args": ["abc"], "expected": "abc", "name": "no encoding"},
        {"args": [""], "expected": "", "name": "empty string"},
        {"args": ["10[a]"], "expected": "aaaaaaaaaa", "name": "double digit number"},
    ],
    "asteroid_collision": [
        {"args": [[5, 10, -5]], "expected": [5, 10], "name": "basic case"},
        {"args": [[8, -8]], "expected": [], "name": "mutual destruction"},
        {"args": [[10, 2, -5]], "expected": [10], "name": "bigger survives"},
        {"args": [[-2, -1, 1, 2]], "expected": [-2, -1, 1, 2], "name": "no collision"},
        {"args": [[]], "expected": [], "name": "empty array"},
        {"args": [[5]], "expected": [5], "name": "single asteroid"},
    ],
    "remove_k_digits": [
        {"args": ["1432219", 3], "expected": "1219", "name": "basic case"},
        {"args": ["10200", 1], "expected": "200", "name": "leading zeros"},
        {"args": ["10", 2], "expected": "0", "name": "remove all"},
        {"args": ["112", 1], "expected": "11", "name": "remove from middle"},
        {"args": ["1111", 2], "expected": "11", "name": "all same digits"},
        {"args": ["9", 1], "expected": "0", "name": "single digit remove all"},
    ],
    "car_fleet": [
        {
            "args": [12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]],
            "expected": 3,
            "name": "basic case",
        },
        {"args": [10, [3], [3]], "expected": 1, "name": "single car"},
        {"args": [100, [0, 2, 4], [4, 2, 1]], "expected": 1, "name": "all merge"},
        {"args": [10, [], []], "expected": 0, "name": "no cars"},
    ],
    "validate_stack_sequences": [
        {
            "args": [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]],
            "expected": True,
            "name": "valid sequence",
        },
        {
            "args": [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]],
            "expected": False,
            "name": "invalid sequence",
        },
        {"args": [[1], [1]], "expected": True, "name": "single element"},
        {"args": [[], []], "expected": True, "name": "empty"},
    ],
    "basic_calculator_ii": [
        {"args": ["3+2*2"], "expected": 7, "name": "basic case"},
        {"args": [" 3/2 "], "expected": 1, "name": "with spaces"},
        {"args": [" 3+5 / 2 "], "expected": 5, "name": "mixed operations"},
        {"args": ["42"], "expected": 42, "name": "just number"},
    ],
    "remove_adjacent_duplicates": [
        {"args": ["abbaca"], "expected": "ca", "name": "basic case"},
        {"args": ["azxxzy"], "expected": "ay", "name": "chain removal"},
        {"args": ["aab"], "expected": "b", "name": "remove at start"},
        {"args": ["abc"], "expected": "abc", "name": "no duplicates"},
        {"args": [""], "expected": "", "name": "empty string"},
        {"args": ["a"], "expected": "a", "name": "single char"},
    ],
    "remove_adjacent_duplicates_k": [
        {"args": ["abcd", 2], "expected": "abcd", "name": "no duplicates"},
        {"args": ["deeedbbcccbdaa", 3], "expected": "aa", "name": "complex case"},
        {"args": ["pbbcggttciiippooaais", 2], "expected": "ps", "name": "another case"},
        {"args": ["", 2], "expected": "", "name": "empty string"},
        {"args": ["a", 2], "expected": "a", "name": "single char"},
    ],
    "max_nesting_depth": [
        {"args": ["(1+(2*3)+((8)/4))+1"], "expected": 3, "name": "basic case"},
        {"args": ["(1)+((2))+(((3)))"], "expected": 3, "name": "increasing depth"},
        {"args": ["1+(2*3)/(2-1)"], "expected": 1, "name": "flat"},
        {"args": ["1"], "expected": 0, "name": "no parens"},
        {"args": [""], "expected": 0, "name": "empty string"},
    ],
    "make_valid_parentheses": [
        {"args": ["lee(t(c)o)de)"], "expected": "lee(t(c)o)de", "name": "basic case"},
        {"args": ["a)b(c)d"], "expected": "ab(c)d", "name": "remove leading"},
        {"args": ["))(("], "expected": "", "name": "all invalid"},
        {"args": ["()"], "expected": "()", "name": "already valid"},
        {"args": [""], "expected": "", "name": "empty string"},
    ],
    "backspace_string_compare": [
        {"args": ["ab#c", "ad#c"], "expected": True, "name": "basic case"},
        {"args": ["ab##", "c#d#"], "expected": True, "name": "multiple backspace"},
        {"args": ["a#c", "b"], "expected": False, "name": "different"},
        {"args": ["a##c", "#a#c"], "expected": True, "name": "extra backspaces"},
        {"args": ["", ""], "expected": True, "name": "both empty strings"},
        {"args": ["a", ""], "expected": False, "name": "one empty string"},
    ],
}
