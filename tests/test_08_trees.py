"""
Tests for Topic 08: Trees
"""
import pytest
from conftest import get_solution, build_tree, tree_to_list, TreeNode


class TestMaxDepth:
    def test_depth_basic(self):
        f = get_solution("max_depth")
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert f(root) == 3

    def test_depth_single(self):
        f = get_solution("max_depth")
        root = build_tree([1])
        assert f(root) == 1

    def test_depth_empty(self):
        f = get_solution("max_depth")
        assert f(None) == 0


class TestInvertTree:
    def test_invert_basic(self):
        f = get_solution("invert_tree")
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        result = f(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_invert_empty(self):
        f = get_solution("invert_tree")
        assert f(None) is None


class TestIsSameTree:
    def test_same_true(self):
        f = get_solution("is_same_tree")
        p = build_tree([1, 2, 3])
        q = build_tree([1, 2, 3])
        assert f(p, q) == True

    def test_same_false(self):
        f = get_solution("is_same_tree")
        p = build_tree([1, 2])
        q = build_tree([1, None, 2])
        assert f(p, q) == False

    def test_same_both_empty(self):
        f = get_solution("is_same_tree")
        assert f(None, None) == True


class TestIsSymmetric:
    def test_symmetric_true(self):
        f = get_solution("is_symmetric")
        root = build_tree([1, 2, 2, 3, 4, 4, 3])
        assert f(root) == True

    def test_symmetric_false(self):
        f = get_solution("is_symmetric")
        root = build_tree([1, 2, 2, None, 3, None, 3])
        assert f(root) == False


class TestLevelOrder:
    def test_level_basic(self):
        f = get_solution("level_order")
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert f(root) == [[3], [9, 20], [15, 7]]

    def test_level_empty(self):
        f = get_solution("level_order")
        assert f(None) == []

    def test_level_single(self):
        f = get_solution("level_order")
        root = build_tree([1])
        assert f(root) == [[1]]


class TestValidateBST:
    def test_bst_valid(self):
        f = get_solution("validate_bst")
        root = build_tree([2, 1, 3])
        assert f(root) == True

    def test_bst_invalid(self):
        f = get_solution("validate_bst")
        root = build_tree([5, 1, 4, None, None, 3, 6])
        assert f(root) == False

    def test_bst_empty(self):
        f = get_solution("validate_bst")
        assert f(None) == True


class TestLowestCommonAncestor:
    def test_lca_basic(self):
        f = get_solution("lowest_common_ancestor")
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = TreeNode(2)
        q = TreeNode(8)
        result = f(root, p, q)
        assert result.val == 6

    def test_lca_same_subtree(self):
        f = get_solution("lowest_common_ancestor")
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = TreeNode(2)
        q = TreeNode(4)
        result = f(root, p, q)
        assert result.val == 2


class TestKthSmallestBST:
    def test_kth_basic(self):
        f = get_solution("kth_smallest_bst")
        root = build_tree([3, 1, 4, None, 2])
        assert f(root, 1) == 1

    def test_kth_larger(self):
        f = get_solution("kth_smallest_bst")
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        assert f(root, 3) == 3


class TestBuildTreeFromTraversals:
    def test_build_basic(self):
        f = get_solution("build_tree_from_traversals")
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = f(preorder, inorder)
        assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]

    def test_build_single(self):
        f = get_solution("build_tree_from_traversals")
        result = f([1], [1])
        assert tree_to_list(result) == [1]


class TestSerializeDeserialize:
    def test_serde_basic(self):
        f = get_solution("serialize_deserialize")
        Codec = f()
        codec = Codec()
        root = build_tree([1, 2, 3, None, None, 4, 5])
        data = codec.serialize(root)
        result = codec.deserialize(data)
        assert tree_to_list(result) == tree_to_list(root)

    def test_serde_empty(self):
        f = get_solution("serialize_deserialize")
        Codec = f()
        codec = Codec()
        data = codec.serialize(None)
        result = codec.deserialize(data)
        assert result is None
