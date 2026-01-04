"""
Tests for Topic 14: Union-Find
"""
import pytest
from conftest import get_solution


class TestImplementUnionFind:
    def test_uf_basic(self):
        f = get_solution("implement_union_find")
        UF = f()
        uf = UF(5)
        assert uf.connected(0, 1) == False
        uf.union(0, 1)
        assert uf.connected(0, 1) == True
        uf.union(1, 2)
        assert uf.connected(0, 2) == True

    def test_uf_all_connected(self):
        f = get_solution("implement_union_find")
        UF = f()
        uf = UF(4)
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(1, 2)
        assert uf.connected(0, 3) == True


class TestNumConnectedComponents:
    def test_components_basic(self):
        f = get_solution("num_connected_components")
        assert f(5, [[0, 1], [1, 2], [3, 4]]) == 2

    def test_components_all_connected(self):
        f = get_solution("num_connected_components")
        assert f(4, [[0, 1], [1, 2], [2, 3]]) == 1


class TestRedundantConnection:
    def test_redundant_basic(self):
        f = get_solution("redundant_connection")
        assert f([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_redundant_larger(self):
        f = get_solution("redundant_connection")
        assert f([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


class TestAccountsMerge:
    def test_accounts_basic(self):
        f = get_solution("accounts_merge")
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ]
        result = f(accounts)
        # Should merge first two Johns
        assert len(result) == 3


class TestLongestConsecutiveUF:
    def test_consecutive_basic(self):
        f = get_solution("longest_consecutive_uf")
        assert f([100, 4, 200, 1, 3, 2]) == 4

    def test_consecutive_empty(self):
        f = get_solution("longest_consecutive_uf")
        assert f([]) == 0


class TestSatisfiabilityOfEquations:
    def test_satisfiable_true(self):
        f = get_solution("satisfiability_of_equations")
        assert f(["a==b", "b!=a"]) == False

    def test_satisfiable_false(self):
        f = get_solution("satisfiability_of_equations")
        assert f(["b==a", "a==b"]) == True
