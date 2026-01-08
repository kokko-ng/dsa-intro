"""
Topic 14: Union-Find (Disjoint Set Union)
"""

from ..types import TestCasesDict

TOPIC_14_TESTS: TestCasesDict = {
    "implement_union_find": [
        {
            "args": [
                5,
                [
                    ["union", 0, 1],
                    ["union", 2, 3],
                    ["connected", 0, 1],
                    ["connected", 0, 2],
                    ["union", 1, 2],
                    ["connected", 0, 3],
                ],
            ],
            "expected": [True, True, True, False, True, True],
            "name": "basic operations",
            "compare": "union_find_ops",
        },
        {
            "args": [3, [["connected", 0, 1], ["union", 0, 1], ["connected", 0, 1]]],
            "expected": [False, True, True],
            "name": "simple connect",
            "compare": "union_find_ops",
        },
        {
            "args": [3, [["union", 0, 0], ["connected", 0, 0]]],
            "expected": [False, True],
            "name": "self union",
            "compare": "union_find_ops",
        },
        {
            "args": [3, [["union", 0, 1], ["union", 0, 1], ["connected", 0, 1]]],
            "expected": [True, False, True],
            "name": "already connected union",
            "compare": "union_find_ops",
        },
        {
            "args": [1, [["connected", 0, 0]]],
            "expected": [True],
            "name": "single element connected to itself",
            "compare": "union_find_ops",
        },
    ],
    "num_connected_components": [
        {
            "args": [5, [[0, 1], [1, 2], [3, 4]]],
            "expected": 2,
            "name": "two components",
        },
        {
            "args": [5, [[0, 1], [1, 2], [2, 3], [3, 4]]],
            "expected": 1,
            "name": "single chain",
        },
        {"args": [4, []], "expected": 4, "name": "all disconnected"},
        {"args": [1, []], "expected": 1, "name": "single node"},
        {
            "args": [5, [[0, 1], [0, 2], [0, 3], [0, 4]]],
            "expected": 1,
            "name": "star graph",
        },
        {
            "args": [3, [[0, 1], [0, 1]]],
            "expected": 2,
            "name": "duplicate edges",
        },
    ],
    "redundant_connection": [
        {
            "args": [[[1, 2], [1, 3], [2, 3]]],
            "expected": [2, 3],
            "name": "triangle cycle",
        },
        {
            "args": [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]],
            "expected": [1, 4],
            "name": "larger cycle",
        },
        {
            "args": [[[1, 2], [1, 3], [3, 1]]],
            "expected": [3, 1],
            "name": "duplicate edge",
        },
        {
            "args": [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]],
            "expected": [5, 1],
            "name": "5-node cycle",
        },
    ],
    "accounts_merge": [
        {
            "args": [
                [
                    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                    ["John", "johnsmith@mail.com", "john00@mail.com"],
                    ["Mary", "mary@mail.com"],
                    ["John", "johnnybravo@mail.com"],
                ]
            ],
            "expected": [
                [
                    "John",
                    "john00@mail.com",
                    "john_newyork@mail.com",
                    "johnsmith@mail.com",
                ],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ],
            "name": "merge accounts",
            "compare": "accounts_merge",
        },
        {
            "args": [
                [
                    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                    ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                    ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                    ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                    ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
                ]
            ],
            "expected": [
                ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
                ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
                ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
                ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ],
            "name": "no merges",
            "compare": "accounts_merge",
        },
        {
            "args": [[["Alice", "alice@mail.com"]]],
            "expected": [["Alice", "alice@mail.com"]],
            "name": "single account",
            "compare": "accounts_merge",
        },
        {
            "args": [[]],
            "expected": [],
            "name": "empty accounts",
            "compare": "accounts_merge",
        },
        {
            "args": [
                [
                    ["Alex", "a@mail.com", "b@mail.com"],
                    ["Alex", "b@mail.com", "c@mail.com"],
                    ["Alex", "c@mail.com", "d@mail.com"],
                ]
            ],
            "expected": [
                ["Alex", "a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com"],
            ],
            "name": "chain merge multiple accounts",
            "compare": "accounts_merge",
        },
    ],
    "longest_consecutive_uf": [
        {"args": [[100, 4, 200, 1, 3, 2]], "expected": 4, "name": "basic case"},
        {"args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9, "name": "0 to 8"},
        {"args": [[]], "expected": 0, "name": "empty array"},
        {"args": [[1]], "expected": 1, "name": "single element"},
        {"args": [[-5, -4, -3, -2, -1]], "expected": 5, "name": "negative numbers"},
        {"args": [[5, 5, 5, 5]], "expected": 1, "name": "all duplicates"},
    ],
    "satisfiability_of_equations": [
        {"args": [["a==b", "b!=a"]], "expected": False, "name": "contradiction"},
        {"args": [["b==a", "a==b"]], "expected": True, "name": "consistent"},
        {"args": [["a==b", "b==c", "a==c"]], "expected": True, "name": "transitive"},
        {
            "args": [["a==b", "b!=c", "c==a"]],
            "expected": False,
            "name": "indirect contradiction",
        },
        {"args": [["a!=a"]], "expected": False, "name": "self inequality"},
        {"args": [["a==a"]], "expected": True, "name": "self equality"},
        {"args": [[]], "expected": True, "name": "empty equations"},
        {
            "args": [["a!=b", "b!=c", "a!=c"]],
            "expected": True,
            "name": "all inequalities",
        },
    ],
    "friend_circles": [
        {
            "args": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
            "expected": 2,
            "name": "two groups",
        },
        {
            "args": [[[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
            "expected": 1,
            "name": "all connected",
        },
        {
            "args": [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]],
            "expected": 3,
            "name": "all separate",
        },
    ],
    "smallest_string_with_swaps": [
        {"args": ["dcab", [[0, 3], [1, 2]]], "expected": "bacd", "name": "basic case"},
        {
            "args": ["dcab", [[0, 3], [1, 2], [0, 2]]],
            "expected": "abcd",
            "name": "connected swaps",
        },
        {"args": ["cba", [[0, 1], [1, 2]]], "expected": "abc", "name": "chain swaps"},
    ],
    "min_cost_connect_all_points": [
        {
            "args": [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]],
            "expected": 20,
            "name": "basic case",
        },
        {
            "args": [[[3, 12], [-2, 5], [-4, 1]]],
            "expected": 18,
            "name": "with negatives",
        },
        {"args": [[[0, 0], [1, 1]]], "expected": 2, "name": "two points"},
    ],
    "regions_cut_by_slashes": [
        {"args": [[" /", "/ "]], "expected": 2, "name": "basic case"},
        {"args": [[" /", "  "]], "expected": 1, "name": "single region"},
        {"args": [["/\\", "\\/"]], "expected": 5, "name": "four squares"},
    ],
    "similar_string_groups": [
        {
            "args": [["tars", "rats", "arts", "star"]],
            "expected": 2,
            "name": "two groups",
        },
        {"args": [["omv", "ovm"]], "expected": 1, "name": "single group"},
        {"args": [["abc", "def", "ghi"]], "expected": 3, "name": "all different"},
    ],
    "most_stones_removed": [
        {
            "args": [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]],
            "expected": 5,
            "name": "basic case",
        },
        {
            "args": [[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]],
            "expected": 3,
            "name": "another case",
        },
        {"args": [[[0, 0]]], "expected": 0, "name": "single stone"},
    ],
    "making_a_large_island": [
        {"args": [[[1, 0], [0, 1]]], "expected": 3, "name": "basic case"},
        {"args": [[[1, 1], [1, 0]]], "expected": 4, "name": "one zero"},
        {"args": [[[1, 1], [1, 1]]], "expected": 4, "name": "all ones"},
        {"args": [[[0, 0], [0, 0]]], "expected": 1, "name": "all zeros"},
    ],
}
