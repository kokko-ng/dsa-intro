"""
Topic 10: Graphs
"""

from ..types import TestCasesDict

TOPIC_10_TESTS: TestCasesDict = {
    "num_islands": [
        {
            "args": [
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ],
            "expected": 1,
            "name": "single island",
        },
        {
            "args": [
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ],
            "expected": 3,
            "name": "three islands",
        },
        {
            "args": [[["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]],
            "expected": 5,
            "name": "diagonal islands",
        },
        {"args": [[["0"]]], "expected": 0, "name": "no islands"},
        {"args": [[["1"]]], "expected": 1, "name": "single cell island"},
        {"args": [[]], "expected": 0, "name": "empty grid"},
        {
            "args": [
                [
                    ["0", "0", "0"],
                    ["0", "0", "0"],
                    ["0", "0", "0"],
                ]
            ],
            "expected": 0,
            "name": "all water",
        },
        {
            "args": [
                [
                    ["1", "1", "1"],
                    ["1", "1", "1"],
                    ["1", "1", "1"],
                ]
            ],
            "expected": 1,
            "name": "all land",
        },
    ],
    "clone_graph": [
        {
            "args": [[[2, 4], [1, 3], [2, 4], [1, 3]]],
            "expected": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "name": "4 node cycle",
            "compare": "graph_clone",
        },
        {
            "args": [[[]]],
            "expected": [[]],
            "name": "single node",
            "compare": "graph_clone",
        },
        {"args": [[]], "expected": [], "name": "empty graph", "compare": "graph_clone"},
        {
            "args": [[[2], [1]]],
            "expected": [[2], [1]],
            "name": "two connected nodes",
            "compare": "graph_clone",
        },
    ],
    "course_schedule": [
        {"args": [2, [[1, 0]]], "expected": True, "name": "simple dependency"},
        {"args": [2, [[1, 0], [0, 1]]], "expected": False, "name": "cycle"},
        {"args": [3, [[1, 0], [2, 1]]], "expected": True, "name": "chain"},
        {"args": [1, []], "expected": True, "name": "no prerequisites"},
        {
            "args": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
            "expected": True,
            "name": "diamond",
        },
        {"args": [3, []], "expected": True, "name": "multiple independent courses"},
        {
            "args": [3, [[0, 1], [1, 2], [2, 0]]],
            "expected": False,
            "name": "3-node cycle",
        },
    ],
    "course_schedule_order": [
        {"args": [2, [[1, 0]]], "expected": [0, 1], "name": "simple order"},
        {
            "args": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
            "expected": [0, 1, 2, 3],
            "name": "multiple valid",
            "compare": "valid_course_order",
        },
        {"args": [2, [[1, 0], [0, 1]]], "expected": [], "name": "cycle impossible"},
        {"args": [1, []], "expected": [0], "name": "single course"},
    ],
    "pacific_atlantic": [
        {
            "args": [
                [
                    [1, 2, 2, 3, 5],
                    [3, 2, 3, 4, 4],
                    [2, 4, 5, 3, 1],
                    [6, 7, 1, 4, 5],
                    [5, 1, 1, 2, 4],
                ]
            ],
            "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            "name": "standard case",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[1]]],
            "expected": [[0, 0]],
            "name": "single cell",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[1, 1], [1, 1]]],
            "expected": [[0, 0], [0, 1], [1, 0], [1, 1]],
            "name": "all same height",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[1, 2, 3]]],
            "expected": [[0, 0], [0, 1], [0, 2]],
            "name": "single row",
            "compare": "set_of_tuples",
        },
    ],
    "word_ladder": [
        {
            "args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
            "expected": 5,
            "name": "basic case",
        },
        {
            "args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
            "expected": 0,
            "name": "no path",
        },
        {"args": ["a", "c", ["a", "b", "c"]], "expected": 2, "name": "short words"},
        {"args": ["hit", "hit", ["hit"]], "expected": 1, "name": "same start and end"},
    ],
    "surrounded_regions": [
        {
            "args": [
                [
                    ["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"],
                ]
            ],
            "expected": [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
            "name": "basic case",
            "compare": "in_place_grid",
        },
        {
            "args": [[["X"]]],
            "expected": [["X"]],
            "name": "single X",
            "compare": "in_place_grid",
        },
        {
            "args": [[["O"]]],
            "expected": [["O"]],
            "name": "single O",
            "compare": "in_place_grid",
        },
        {
            "args": [
                [
                    ["O", "O", "O"],
                    ["O", "X", "O"],
                    ["O", "O", "O"],
                ]
            ],
            "expected": [
                ["O", "O", "O"],
                ["O", "X", "O"],
                ["O", "O", "O"],
            ],
            "name": "all border O's - nothing captured",
            "compare": "in_place_grid",
        },
    ],
    "graph_valid_tree": [
        {
            "args": [5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
            "expected": True,
            "name": "valid tree",
        },
        {
            "args": [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]],
            "expected": False,
            "name": "has cycle",
        },
        {"args": [5, [[0, 1], [2, 3]]], "expected": False, "name": "disconnected"},
        {"args": [1, []], "expected": True, "name": "single node"},
        {"args": [2, [[0, 1]]], "expected": True, "name": "two nodes one edge"},
        {"args": [2, []], "expected": False, "name": "two nodes no edges"},
        {
            "args": [3, [[0, 1], [1, 2], [0, 2]]],
            "expected": False,
            "name": "triangle cycle",
        },
    ],
    "count_connected_components": [
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
    ],
    "alien_dictionary": [
        {
            "args": [["wrt", "wrf", "er", "ett", "rftt"]],
            "expected": "wertf",
            "name": "basic case",
        },
        {"args": [["z", "x"]], "expected": "zx", "name": "two words"},
        {"args": [["z", "x", "z"]], "expected": "", "name": "invalid order"},
        {
            "args": [["abc"]],
            "expected": "abc",
            "name": "single word",
            "compare": "alien_order",
        },
        {"args": [["abc", "ab"]], "expected": "", "name": "prefix comes after"},
        {"args": [["a", "b", "c"]], "expected": "abc", "name": "single char words"},
    ],
    "rotting_oranges": [
        {
            "args": [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]],
            "expected": 4,
            "name": "basic case",
        },
        {
            "args": [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]],
            "expected": -1,
            "name": "impossible",
        },
        {"args": [[[0, 2]]], "expected": 0, "name": "no fresh"},
        {
            "args": [[[2, 1, 1], [1, 1, 1], [0, 1, 2]]],
            "expected": 2,
            "name": "two sources",
        },
    ],
    "shortest_path_binary_matrix": [
        {"args": [[[0, 1], [1, 0]]], "expected": 2, "name": "basic 2x2"},
        {
            "args": [[[0, 0, 0], [1, 1, 0], [1, 1, 0]]],
            "expected": 4,
            "name": "3x3 path",
        },
        {
            "args": [[[1, 0, 0], [1, 1, 0], [1, 1, 0]]],
            "expected": -1,
            "name": "blocked start",
        },
        {"args": [[[0]]], "expected": 1, "name": "single cell"},
    ],
    "network_delay_time": [
        {
            "args": [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2],
            "expected": 2,
            "name": "basic case",
        },
        {"args": [[[1, 2, 1]], 2, 1], "expected": 1, "name": "simple path"},
        {"args": [[[1, 2, 1]], 2, 2], "expected": -1, "name": "unreachable"},
    ],
    "cheapest_flights": [
        {
            "args": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1],
            "expected": 200,
            "name": "with stop",
        },
        {
            "args": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0],
            "expected": 500,
            "name": "direct flight",
        },
        {
            "args": [3, [[0, 1, 100], [1, 2, 100]], 0, 2, 0],
            "expected": -1,
            "name": "not enough stops",
        },
    ],
    "all_paths_source_target": [
        {
            "args": [[[1, 2], [3], [3], []]],
            "expected": [[0, 1, 3], [0, 2, 3]],
            "name": "basic case",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[4, 3, 1], [3, 2, 4], [3], [4], []]],
            "expected": [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
            "name": "multiple paths",
            "compare": "set_of_tuples",
        },
        {
            "args": [[[1], []]],
            "expected": [[0, 1]],
            "name": "simple path",
            "compare": "set_of_tuples",
        },
    ],
    "evaluate_division": [
        {
            "args": [
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ],
            "expected": [6.0, 0.5, -1.0, 1.0, -1.0],
            "name": "basic case",
        },
        {
            "args": [[["a", "b"]], [2.0], [["a", "b"], ["b", "a"], ["a", "c"]]],
            "expected": [2.0, 0.5, -1.0],
            "name": "simple case",
        },
    ],
    "minimum_height_trees": [
        {"args": [4, [[1, 0], [1, 2], [1, 3]]], "expected": [1], "name": "star graph"},
        {
            "args": [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]],
            "expected": [3, 4],
            "name": "two roots",
        },
        {"args": [1, []], "expected": [0], "name": "single node"},
    ],
    "is_bipartite": [
        {
            "args": [[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]],
            "expected": False,
            "name": "not bipartite",
        },
        {
            "args": [[[1, 3], [0, 2], [1, 3], [0, 2]]],
            "expected": True,
            "name": "bipartite",
        },
        {"args": [[[1], [0]]], "expected": True, "name": "two nodes"},
    ],
    "keys_and_rooms": [
        {"args": [[[1], [2], [3], []]], "expected": True, "name": "can visit all"},
        {
            "args": [[[1, 3], [3, 0, 1], [2], [0]]],
            "expected": False,
            "name": "room 2 locked",
        },
        {"args": [[[1, 2], [], []]], "expected": True, "name": "all keys in room 0"},
    ],
    "find_eventual_safe_nodes": [
        {
            "args": [[[1, 2], [2, 3], [5], [0], [5], [], []]],
            "expected": [2, 4, 5, 6],
            "name": "basic case",
        },
        {
            "args": [[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]],
            "expected": [4],
            "name": "mostly cycles",
        },
    ],
    "shortest_bridge": [
        {"args": [[[0, 1], [1, 0]]], "expected": 1, "name": "basic case"},
        {
            "args": [[[0, 1, 0], [0, 0, 0], [0, 0, 1]]],
            "expected": 2,
            "name": "diagonal islands",
        },
        {
            "args": [
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ]
            ],
            "expected": 1,
            "name": "nested islands",
        },
    ],
}
