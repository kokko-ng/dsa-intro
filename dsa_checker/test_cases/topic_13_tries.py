"""
Topic 13: Tries
"""

from ..types import TestCasesDict

TOPIC_13_TESTS: TestCasesDict = {
    "implement_trie": [
        {
            "args": [
                ["insert", "search", "search", "startsWith", "insert", "search"],
                [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            ],
            "expected": [None, True, False, True, None, True],
            "name": "basic operations",
            "compare": "trie_ops",
        },
        {
            "args": [
                ["insert", "search", "startsWith"],
                [["hello"], ["hello"], ["hell"]],
            ],
            "expected": [None, True, True],
            "name": "prefix check",
            "compare": "trie_ops",
        },
        {
            "args": [
                ["insert", "search", "startsWith"],
                [[""], [""], [""]],
            ],
            "expected": [None, True, True],
            "name": "empty string",
            "compare": "trie_ops",
        },
    ],
    "word_search_ii": [
        {
            "args": [
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain"],
            ],
            "expected": ["eat", "oath"],
            "name": "basic case",
            "compare": "set",
        },
        {
            "args": [[["a", "b"], ["c", "d"]], ["abcb"]],
            "expected": [],
            "name": "no matches",
        },
        {"args": [[["a"]], ["a"]], "expected": ["a"], "name": "single cell match"},
        {
            "args": [[["a", "b"], ["c", "d"]], []],
            "expected": [],
            "name": "empty words list",
        },
        {
            "args": [[["a", "a"]], ["aaa"]],
            "expected": [],
            "name": "cannot reuse same cell",
        },
    ],
    "add_and_search_word": [
        {
            "args": [
                [
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                [["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            ],
            "expected": [None, None, None, False, True, True, True],
            "name": "with wildcards",
            "compare": "word_dict_ops",
        },
        {
            "args": [["addWord", "search", "search"], [["a"], ["a"], ["."]]],
            "expected": [None, True, True],
            "name": "single char",
            "compare": "word_dict_ops",
        },
    ],
    "replace_words": [
        {
            "args": [["cat", "bat", "rat"], "the cattle was rattled by the battery"],
            "expected": "the cat was rat by the bat",
            "name": "basic replacement",
        },
        {
            "args": [["a", "b", "c"], "aadsfasf absbs bbab cadsfabd"],
            "expected": "a a b c",
            "name": "short roots",
        },
        {
            "args": [
                ["catt", "cat", "bat", "rat"],
                "the cattle was rattled by the battery",
            ],
            "expected": "the cat was rat by the bat",
            "name": "overlapping roots",
        },
        {
            "args": [[], "hello world"],
            "expected": "hello world",
            "name": "empty dictionary",
        },
        {
            "args": [["xyz"], "hello world"],
            "expected": "hello world",
            "name": "no matching roots",
        },
    ],
    "longest_word": [
        {
            "args": [["w", "wo", "wor", "worl", "world"]],
            "expected": "world",
            "name": "buildable word",
        },
        {
            "args": [["a", "banana", "app", "appl", "ap", "apply", "apple"]],
            "expected": "apple",
            "name": "lexicographically smallest",
        },
        {
            "args": [
                [
                    "yo",
                    "ew",
                    "fc",
                    "zrc",
                    "yodn",
                    "fcm",
                    "qm",
                    "qmo",
                    "fcmz",
                    "z",
                    "ewq",
                    "yod",
                    "ewqz",
                    "y",
                ]
            ],
            "expected": "yodn",
            "name": "complex case",
        },
        {"args": [["a"]], "expected": "a", "name": "single word"},
        {
            "args": [["b", "a"]],
            "expected": "a",
            "name": "two single letters lexicographic",
        },
    ],
    "map_sum": [
        {
            "args": [
                ["insert", "sum", "insert", "sum"],
                [["apple", 3], ["ap"], ["app", 2], ["ap"]],
            ],
            "expected": [None, 3, None, 5],
            "name": "basic sum",
            "compare": "map_sum_ops",
        },
        {
            "args": [["insert", "insert", "sum"], [["a", 1], ["a", 2], ["a"]]],
            "expected": [None, None, 2],
            "name": "overwrite value",
            "compare": "map_sum_ops",
        },
        {
            "args": [["sum"], [["nonexistent"]]],
            "expected": [0],
            "name": "sum with no matching prefix",
            "compare": "map_sum_ops",
        },
    ],
    "count_prefix": [
        {
            "args": [["apple", "app", "application"], "app"],
            "expected": 3,
            "name": "basic case",
        },
        {"args": [["hello", "world"], "he"], "expected": 1, "name": "single match"},
        {"args": [["abc", "def"], "x"], "expected": 0, "name": "no match"},
    ],
    "search_suggestions": [
        {
            "args": [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],
            "expected": [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
            "name": "basic case",
        },
        {
            "args": [["havana"], "havana"],
            "expected": [
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
            ],
            "name": "exact match",
        },
    ],
    "palindrome_pairs": [
        {
            "args": [["abcd", "dcba", "lls", "s", "sssll"]],
            "expected": [[0, 1], [1, 0], [3, 2], [2, 4]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": [["bat", "tab", "cat"]],
            "expected": [[0, 1], [1, 0]],
            "name": "simple pairs",
            "compare": "set_of_tuples",
        },
        {
            "args": [["a", ""]],
            "expected": [[0, 1], [1, 0]],
            "name": "with empty",
            "compare": "set_of_tuples",
        },
    ],
    "index_pairs": [
        {
            "args": ["thestoryofleetcodeandme", ["story", "fleet", "leetcode"]],
            "expected": [[3, 7], [9, 13], [10, 17]],
            "name": "basic case",
        },
        {
            "args": ["ababa", ["aba", "ab"]],
            "expected": [[0, 1], [0, 2], [2, 3], [2, 4]],
            "name": "overlapping",
        },
    ],
    "magic_dictionary": [
        {
            "args": [
                ["buildDict", "search", "search", "search", "search"],
                [
                    [["hello", "leetcode"]],
                    ["hello"],
                    ["hhllo"],
                    ["hell"],
                    ["leetcoded"],
                ],
            ],
            "expected": [None, False, True, False, False],
            "name": "basic case",
            "compare": "magic_dict_ops",
        },
    ],
    "concat_words": [
        {
            "args": [
                [
                    "cat",
                    "cats",
                    "catsdogcats",
                    "dog",
                    "dogcatsdog",
                    "hippopotamuses",
                    "rat",
                    "ratcatdogcat",
                ]
            ],
            "expected": ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
            "name": "basic case",
            "compare": "set",
        },
        {
            "args": [["cat", "dog", "catdog"]],
            "expected": ["catdog"],
            "name": "simple case",
            "compare": "set",
        },
    ],
}
