"""
Topic 08: Trees
"""

from ..types import TestCasesDict

TOPIC_08_TESTS: TestCasesDict = {
    "max_depth": [
        {
            "args": [[3, 9, 20, None, None, 15, 7]],
            "expected": 3,
            "name": "balanced tree",
            "input_type": "tree",
        },
        {
            "args": [[1, None, 2]],
            "expected": 2,
            "name": "right skewed",
            "input_type": "tree",
        },
        {"args": [[]], "expected": 0, "name": "empty tree", "input_type": "tree"},
        {"args": [[1]], "expected": 1, "name": "single node", "input_type": "tree"},
        {
            "args": [[1, 2, 3, 4, 5]],
            "expected": 3,
            "name": "left heavy",
            "input_type": "tree",
        },
    ],
    "invert_tree": [
        {
            "args": [[4, 2, 7, 1, 3, 6, 9]],
            "expected": [4, 7, 2, 9, 6, 3, 1],
            "name": "full tree",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[2, 1, 3]],
            "expected": [2, 3, 1],
            "name": "simple tree",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[]],
            "expected": [],
            "name": "empty tree",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1]],
            "expected": [1],
            "name": "single node",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
    ],
    "is_same_tree": [
        {
            "args": [[1, 2, 3], [1, 2, 3]],
            "expected": True,
            "name": "identical trees",
            "input_type": "trees",
        },
        {
            "args": [[1, 2], [1, None, 2]],
            "expected": False,
            "name": "different structure",
            "input_type": "trees",
        },
        {
            "args": [[1, 2, 1], [1, 1, 2]],
            "expected": False,
            "name": "different values",
            "input_type": "trees",
        },
        {
            "args": [[], []],
            "expected": True,
            "name": "both empty",
            "input_type": "trees",
        },
        {
            "args": [[1], [1]],
            "expected": True,
            "name": "single node same",
            "input_type": "trees",
        },
        {
            "args": [[], [1]],
            "expected": False,
            "name": "one empty one not",
            "input_type": "trees",
        },
    ],
    "is_symmetric": [
        {
            "args": [[1, 2, 2, 3, 4, 4, 3]],
            "expected": True,
            "name": "symmetric tree",
            "input_type": "tree",
        },
        {
            "args": [[1, 2, 2, None, 3, None, 3]],
            "expected": False,
            "name": "not symmetric",
            "input_type": "tree",
        },
        {"args": [[1]], "expected": True, "name": "single node", "input_type": "tree"},
        {"args": [[]], "expected": True, "name": "empty tree", "input_type": "tree"},
        {
            "args": [[1, 2, 2]],
            "expected": True,
            "name": "two levels symmetric",
            "input_type": "tree",
        },
    ],
    "level_order": [
        {
            "args": [[3, 9, 20, None, None, 15, 7]],
            "expected": [[3], [9, 20], [15, 7]],
            "name": "standard tree",
            "input_type": "tree",
        },
        {"args": [[1]], "expected": [[1]], "name": "single node", "input_type": "tree"},
        {"args": [[]], "expected": [], "name": "empty tree", "input_type": "tree"},
        {
            "args": [[1, 2, 3, 4, 5]],
            "expected": [[1], [2, 3], [4, 5]],
            "name": "complete tree",
            "input_type": "tree",
        },
    ],
    "validate_bst": [
        {
            "args": [[2, 1, 3]],
            "expected": True,
            "name": "valid simple BST",
            "input_type": "tree",
        },
        {
            "args": [[5, 1, 4, None, None, 3, 6]],
            "expected": False,
            "name": "invalid BST",
            "input_type": "tree",
        },
        {"args": [[]], "expected": True, "name": "empty tree", "input_type": "tree"},
        {"args": [[1]], "expected": True, "name": "single node", "input_type": "tree"},
        {
            "args": [[5, 4, 6, None, None, 3, 7]],
            "expected": False,
            "name": "subtree violation",
            "input_type": "tree",
        },
        {
            "args": [[2, 2, 2]],
            "expected": False,
            "name": "equal values invalid",
            "input_type": "tree",
        },
        {
            "args": [[0, -3, 9, -10, None, 5]],
            "expected": True,
            "name": "valid BST with negatives",
            "input_type": "tree",
        },
    ],
    "lowest_common_ancestor": [
        {
            "args": [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8],
            "expected": 6,
            "name": "root is LCA",
            "input_type": "tree_with_targets",
            "output_type": "tree_val",
        },
        {
            "args": [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4],
            "expected": 2,
            "name": "one is ancestor",
            "input_type": "tree_with_targets",
            "output_type": "tree_val",
        },
        {
            "args": [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5],
            "expected": 4,
            "name": "common ancestor",
            "input_type": "tree_with_targets",
            "output_type": "tree_val",
        },
        {
            "args": [[2, 1], 2, 1],
            "expected": 2,
            "name": "two nodes",
            "input_type": "tree_with_targets",
            "output_type": "tree_val",
        },
    ],
    "kth_smallest_bst": [
        {
            "args": [[3, 1, 4, None, 2], 1],
            "expected": 1,
            "name": "first smallest",
            "input_type": "tree",
        },
        {
            "args": [[5, 3, 6, 2, 4, None, None, 1], 3],
            "expected": 3,
            "name": "third smallest",
            "input_type": "tree",
        },
        {
            "args": [[3, 1, 4, None, 2], 2],
            "expected": 2,
            "name": "second smallest",
            "input_type": "tree",
        },
        {"args": [[1], 1], "expected": 1, "name": "single node", "input_type": "tree"},
        {
            "args": [[3, 1, 4, None, 2], 4],
            "expected": 4,
            "name": "k equals tree size (largest)",
            "input_type": "tree",
        },
    ],
    "build_tree_from_traversals": [
        {
            "args": [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
            "expected": [3, 9, 20, None, None, 15, 7],
            "name": "standard tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[-1], [-1]],
            "expected": [-1],
            "name": "single node",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1, 2], [2, 1]],
            "expected": [1, 2],
            "name": "two nodes",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1, 2, 3], [2, 1, 3]],
            "expected": [1, 2, 3],
            "name": "simple tree",
            "output_type": "tree_to_list",
        },
    ],
    "serialize_deserialize": [
        {
            "args": [],
            "expected": [1, 2, 3, None, None, 4, 5],
            "name": "standard tree",
            "compare": "codec",
        },
        {"args": [], "expected": [], "name": "empty tree", "compare": "codec"},
        {"args": [], "expected": [1], "name": "single node", "compare": "codec"},
        {"args": [], "expected": [1, 2], "name": "two nodes", "compare": "codec"},
        {
            "args": [],
            "expected": [1, None, 2],
            "name": "right child only",
            "compare": "codec",
        },
    ],
    "path_sum": [
        {
            "args": [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22],
            "expected": True,
            "name": "has path",
            "input_type": "tree",
        },
        {
            "args": [[1, 2, 3], 5],
            "expected": False,
            "name": "no path",
            "input_type": "tree",
        },
        {
            "args": [[1, 2], 1],
            "expected": False,
            "name": "root only not leaf",
            "input_type": "tree",
        },
        {
            "args": [[], 0],
            "expected": False,
            "name": "empty tree",
            "input_type": "tree",
        },
    ],
    "path_sum_ii": [
        {
            "args": [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22],
            "expected": [[5, 4, 11, 2], [5, 8, 4, 5]],
            "name": "multiple paths",
            "input_type": "tree",
            "compare": "set_of_tuples",
        },
        {
            "args": [[1, 2, 3], 5],
            "expected": [],
            "name": "no path",
            "input_type": "tree",
        },
        {
            "args": [[1], 1],
            "expected": [[1]],
            "name": "single node",
            "input_type": "tree",
        },
    ],
    "binary_tree_paths": [
        {
            "args": [[1, 2, 3, None, 5]],
            "expected": ["1->2->5", "1->3"],
            "name": "basic tree",
            "input_type": "tree",
            "compare": "set",
        },
        {"args": [[1]], "expected": ["1"], "name": "single node", "input_type": "tree"},
        {
            "args": [[1, 2]],
            "expected": ["1->2"],
            "name": "two nodes",
            "input_type": "tree",
        },
    ],
    "sum_root_to_leaf": [
        {
            "args": [[1, 2, 3]],
            "expected": 25,
            "name": "basic case",
            "input_type": "tree",
        },
        {
            "args": [[4, 9, 0, 5, 1]],
            "expected": 1026,
            "name": "more paths",
            "input_type": "tree",
        },
        {"args": [[1]], "expected": 1, "name": "single node", "input_type": "tree"},
    ],
    "diameter_of_tree": [
        {
            "args": [[1, 2, 3, 4, 5]],
            "expected": 3,
            "name": "basic case",
            "input_type": "tree",
        },
        {"args": [[1, 2]], "expected": 1, "name": "two nodes", "input_type": "tree"},
        {"args": [[1]], "expected": 0, "name": "single node", "input_type": "tree"},
    ],
    "right_side_view": [
        {
            "args": [[1, 2, 3, None, 5, None, 4]],
            "expected": [1, 3, 4],
            "name": "basic case",
            "input_type": "tree",
        },
        {
            "args": [[1, None, 3]],
            "expected": [1, 3],
            "name": "right only",
            "input_type": "tree",
        },
        {
            "args": [[1, 2]],
            "expected": [1, 2],
            "name": "left child visible",
            "input_type": "tree",
        },
        {"args": [[]], "expected": [], "name": "empty tree", "input_type": "tree"},
    ],
    "zigzag_level_order": [
        {
            "args": [[3, 9, 20, None, None, 15, 7]],
            "expected": [[3], [20, 9], [15, 7]],
            "name": "basic case",
            "input_type": "tree",
        },
        {"args": [[1]], "expected": [[1]], "name": "single node", "input_type": "tree"},
        {"args": [[]], "expected": [], "name": "empty tree", "input_type": "tree"},
    ],
    "count_complete_tree_nodes": [
        {
            "args": [[1, 2, 3, 4, 5, 6]],
            "expected": 6,
            "name": "complete tree",
            "input_type": "tree",
        },
        {"args": [[]], "expected": 0, "name": "empty tree", "input_type": "tree"},
        {"args": [[1]], "expected": 1, "name": "single node", "input_type": "tree"},
    ],
    "sorted_array_to_bst": [
        {
            "args": [[-10, -3, 0, 5, 9]],
            "expected": [0, -3, 9, -10, None, 5],
            "name": "basic case",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1, 3]],
            "expected": [3, 1],
            "name": "two elements",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1]],
            "expected": [1],
            "name": "single element",
            "output_type": "tree_to_list",
        },
    ],
    "flatten_tree": [
        {
            "args": [[1, 2, 5, 3, 4, None, 6]],
            "expected": [1, None, 2, None, 3, None, 4, None, 5, None, 6],
            "name": "basic case",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[]],
            "expected": [],
            "name": "empty tree",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
        {
            "args": [[1]],
            "expected": [1],
            "name": "single node",
            "input_type": "tree",
            "output_type": "tree_to_list",
        },
    ],
    "is_balanced": [
        {
            "args": [[3, 9, 20, None, None, 15, 7]],
            "expected": True,
            "name": "balanced",
            "input_type": "tree",
        },
        {
            "args": [[1, 2, 2, 3, 3, None, None, 4, 4]],
            "expected": False,
            "name": "not balanced",
            "input_type": "tree",
        },
        {"args": [[]], "expected": True, "name": "empty tree", "input_type": "tree"},
    ],
    "min_depth": [
        {
            "args": [[3, 9, 20, None, None, 15, 7]],
            "expected": 2,
            "name": "basic case",
            "input_type": "tree",
        },
        {
            "args": [[2, None, 3, None, 4, None, 5, None, 6]],
            "expected": 5,
            "name": "skewed",
            "input_type": "tree",
        },
        {"args": [[1]], "expected": 1, "name": "single node", "input_type": "tree"},
    ],
    "is_subtree": [
        {
            "args": [[3, 4, 5, 1, 2], [4, 1, 2]],
            "expected": True,
            "name": "is subtree",
            "input_type": "trees",
        },
        {
            "args": [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]],
            "expected": False,
            "name": "not subtree",
            "input_type": "trees",
        },
        {
            "args": [[1, 1], [1]],
            "expected": True,
            "name": "single node match",
            "input_type": "trees",
        },
    ],
    "inorder_successor": [
        {
            "args": [[2, 1, 3], 1],
            "expected": 2,
            "name": "basic case",
            "input_type": "tree",
        },
        {
            "args": [[5, 3, 6, 2, 4, None, None, 1], 6],
            "expected": None,
            "name": "no successor",
            "input_type": "tree",
        },
        {
            "args": [[2, 1, 3], 2],
            "expected": 3,
            "name": "root node",
            "input_type": "tree",
        },
    ],
}
