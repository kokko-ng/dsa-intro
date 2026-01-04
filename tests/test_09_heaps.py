"""
Tests for Topic 09: Heaps & Priority Queues
"""
import pytest
from conftest import get_solution, create_linked_list, linked_list_to_list


class TestKthLargestElement:
    def test_kth_basic(self):
        f = get_solution("kth_largest_element")
        assert f([3, 2, 1, 5, 6, 4], 2) == 5

    def test_kth_duplicates(self):
        f = get_solution("kth_largest_element")
        assert f([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


class TestMergeKLists:
    def test_merge_basic(self):
        f = get_solution("merge_k_lists")
        lists = [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6])
        ]
        result = f(lists)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_merge_empty(self):
        f = get_solution("merge_k_lists")
        assert f([]) is None

    def test_merge_single_empty(self):
        f = get_solution("merge_k_lists")
        assert f([None]) is None


class TestTopKFrequentElements:
    def test_topk_basic(self):
        f = get_solution("top_k_frequent_elements")
        result = set(f([1, 1, 1, 2, 2, 3], 2))
        assert result == {1, 2}

    def test_topk_single(self):
        f = get_solution("top_k_frequent_elements")
        assert f([1], 1) == [1]


class TestFindMedian:
    def test_median_basic(self):
        f = get_solution("find_median")
        MedianFinder = f()
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0


class TestKClosestPoints:
    def test_closest_basic(self):
        f = get_solution("k_closest_points")
        result = f([[1, 3], [-2, 2]], 1)
        assert result == [[-2, 2]]

    def test_closest_multiple(self):
        f = get_solution("k_closest_points")
        result = f([[3, 3], [5, -1], [-2, 4]], 2)
        assert len(result) == 2


class TestReorganizeString:
    def test_reorg_possible(self):
        f = get_solution("reorganize_string")
        result = f("aab")
        assert result in ["aba", "baa"]  # Valid reorganizations

    def test_reorg_impossible(self):
        f = get_solution("reorganize_string")
        assert f("aaab") == ""


class TestTaskScheduler:
    def test_task_basic(self):
        f = get_solution("task_scheduler")
        assert f(["A", "A", "A", "B", "B", "B"], 2) == 8

    def test_task_no_cooldown(self):
        f = get_solution("task_scheduler")
        assert f(["A", "A", "A", "B", "B", "B"], 0) == 6
