"""
Shared pytest fixtures and configuration for DSA tests.
"""
import pytest
import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import data structures
from data_structures.linked_list import ListNode, create_linked_list, linked_list_to_list, create_cycle
from data_structures.tree import TreeNode, build_tree, tree_to_list
from data_structures.graph import GraphNode, build_graph_from_edges, build_graph_nodes


def get_solution(func_name: str):
    """
    Get the student's solution function by name.
    This is used by test files to access the function being tested.
    """
    from dsa_checker.checker import get_solution as _get_solution
    func = _get_solution(func_name)
    if func is None:
        pytest.skip(f"Function '{func_name}' not implemented yet")
    return func


# ============================================================================
# Linked List Fixtures
# ============================================================================

@pytest.fixture
def sample_linked_list():
    """Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5"""
    return create_linked_list([1, 2, 3, 4, 5])


@pytest.fixture
def single_node_list():
    """Create a single node list: 1"""
    return create_linked_list([1])


@pytest.fixture
def empty_list():
    """Create an empty list"""
    return None


# ============================================================================
# Tree Fixtures
# ============================================================================

@pytest.fixture
def sample_binary_tree():
    """
    Create a sample binary tree:
           1
          / \
         2   3
        / \
       4   5
    """
    return build_tree([1, 2, 3, 4, 5])


@pytest.fixture
def sample_bst():
    """
    Create a sample BST:
           4
          / \
         2   6
        / \ / \
       1  3 5  7
    """
    return build_tree([4, 2, 6, 1, 3, 5, 7])


@pytest.fixture
def single_node_tree():
    """Create a single node tree"""
    return build_tree([1])


@pytest.fixture
def empty_tree():
    """Create an empty tree"""
    return None


# ============================================================================
# Graph Fixtures
# ============================================================================

@pytest.fixture
def sample_undirected_graph():
    """
    Create a sample undirected graph:
    0 -- 1
    |    |
    2 -- 3
    """
    return build_graph_from_edges(4, [[0, 1], [0, 2], [1, 3], [2, 3]], directed=False)


@pytest.fixture
def sample_directed_graph():
    """
    Create a sample directed graph:
    0 -> 1 -> 2
    |         ^
    v         |
    3 --------+
    """
    return build_graph_from_edges(4, [[0, 1], [1, 2], [0, 3], [3, 2]], directed=True)


# ============================================================================
# Custom Markers
# ============================================================================

def pytest_configure(config):
    config.addinivalue_line("markers", "basic: marks tests as basic cases")
    config.addinivalue_line("markers", "edge: marks tests as edge cases")
    config.addinivalue_line("markers", "perf: marks tests as performance tests")
    config.addinivalue_line("markers", "large: marks tests with large inputs")


# ============================================================================
# Timeout Configuration
# ============================================================================

@pytest.fixture(autouse=True)
def set_timeout(request):
    """Default timeout for all tests is handled by pytest-timeout."""
    pass
