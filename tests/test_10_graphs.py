"""
Tests for Topic 10: Graphs
"""
import pytest
from conftest import get_solution, build_graph_nodes, graph_to_adj_list


class TestNumIslands:
    def test_islands_basic(self):
        f = get_solution("num_islands")
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert f(grid) == 1

    def test_islands_multiple(self):
        f = get_solution("num_islands")
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert f(grid) == 3

    def test_islands_empty(self):
        f = get_solution("num_islands")
        assert f([]) == 0


class TestCloneGraph:
    def test_clone_basic(self):
        f = get_solution("clone_graph")
        node = build_graph_nodes([[2, 4], [1, 3], [2, 4], [1, 3]])
        clone = f(node)
        assert clone is not node
        assert graph_to_adj_list(clone) == [[2, 4], [1, 3], [2, 4], [1, 3]]

    def test_clone_empty(self):
        f = get_solution("clone_graph")
        assert f(None) is None


class TestCourseSchedule:
    def test_schedule_possible(self):
        f = get_solution("course_schedule")
        assert f(2, [[1, 0]]) == True

    def test_schedule_impossible(self):
        f = get_solution("course_schedule")
        assert f(2, [[1, 0], [0, 1]]) == False

    def test_schedule_no_prereqs(self):
        f = get_solution("course_schedule")
        assert f(3, []) == True


class TestCourseScheduleOrder:
    def test_order_basic(self):
        f = get_solution("course_schedule_order")
        result = f(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        assert len(result) == 4
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)

    def test_order_impossible(self):
        f = get_solution("course_schedule_order")
        assert f(2, [[1, 0], [0, 1]]) == []


class TestPacificAtlantic:
    def test_pacific_basic(self):
        f = get_solution("pacific_atlantic")
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        result = f(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        assert sorted(result) == sorted(expected)


class TestWordLadder:
    def test_ladder_basic(self):
        f = get_solution("word_ladder")
        assert f("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5

    def test_ladder_no_path(self):
        f = get_solution("word_ladder")
        assert f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0


class TestSurroundedRegions:
    def test_surrounded_basic(self):
        f = get_solution("surrounded_regions")
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        f(board)
        assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]


class TestGraphValidTree:
    def test_tree_valid(self):
        f = get_solution("graph_valid_tree")
        assert f(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

    def test_tree_invalid_cycle(self):
        f = get_solution("graph_valid_tree")
        assert f(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False


class TestCountConnectedComponents:
    def test_components_basic(self):
        f = get_solution("count_connected_components")
        assert f(5, [[0, 1], [1, 2], [3, 4]]) == 2

    def test_components_single(self):
        f = get_solution("count_connected_components")
        assert f(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


class TestAlienDictionary:
    def test_alien_basic(self):
        f = get_solution("alien_dictionary")
        result = f(["wrt", "wrf", "er", "ett", "rftt"])
        # Check ordering constraints
        assert result.index('w') < result.index('e')
        assert result.index('r') < result.index('t')
        assert result.index('e') < result.index('r')

    def test_alien_invalid(self):
        f = get_solution("alien_dictionary")
        assert f(["z", "x", "z"]) == ""
