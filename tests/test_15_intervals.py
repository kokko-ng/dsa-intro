"""
Tests for Topic 15: Intervals & Sorting Patterns
"""
import pytest
from conftest import get_solution


class TestMergeIntervals:
    def test_merge_basic(self):
        f = get_solution("merge_intervals")
        assert f([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    def test_merge_all(self):
        f = get_solution("merge_intervals")
        assert f([[1, 4], [4, 5]]) == [[1, 5]]

    def test_merge_single(self):
        f = get_solution("merge_intervals")
        assert f([[1, 4]]) == [[1, 4]]


class TestInsertInterval:
    def test_insert_middle(self):
        f = get_solution("insert_interval")
        assert f([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

    def test_insert_merge_multiple(self):
        f = get_solution("insert_interval")
        assert f([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]


class TestMeetingRooms:
    def test_rooms_possible(self):
        f = get_solution("meeting_rooms")
        assert f([[0, 30], [5, 10], [15, 20]]) == False

    def test_rooms_not_possible(self):
        f = get_solution("meeting_rooms")
        assert f([[7, 10], [2, 4]]) == True

    def test_rooms_empty(self):
        f = get_solution("meeting_rooms")
        assert f([]) == True


class TestMeetingRoomsII:
    def test_rooms2_basic(self):
        f = get_solution("meeting_rooms_ii")
        assert f([[0, 30], [5, 10], [15, 20]]) == 2

    def test_rooms2_sequential(self):
        f = get_solution("meeting_rooms_ii")
        assert f([[7, 10], [2, 4]]) == 1


class TestNonOverlappingIntervals:
    def test_non_overlapping_basic(self):
        f = get_solution("non_overlapping_intervals")
        assert f([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    def test_non_overlapping_all_same(self):
        f = get_solution("non_overlapping_intervals")
        assert f([[1, 2], [1, 2], [1, 2]]) == 2


class TestMinimumNumberOfArrows:
    def test_arrows_basic(self):
        f = get_solution("minimum_number_of_arrows")
        assert f([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2

    def test_arrows_no_overlap(self):
        f = get_solution("minimum_number_of_arrows")
        assert f([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4


class TestIntervalListIntersections:
    def test_intersect_basic(self):
        f = get_solution("interval_list_intersections")
        result = f([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])
        assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    def test_intersect_empty(self):
        f = get_solution("interval_list_intersections")
        assert f([], [[1, 2]]) == []
