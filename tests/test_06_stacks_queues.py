"""
Tests for Topic 06: Stacks & Queues
"""
import pytest
from conftest import get_solution


class TestValidParentheses:
    def test_valid_basic(self):
        f = get_solution("valid_parentheses")
        assert f("()") == True

    def test_valid_multiple(self):
        f = get_solution("valid_parentheses")
        assert f("()[]{}") == True

    def test_valid_nested(self):
        f = get_solution("valid_parentheses")
        assert f("{[]}") == True

    def test_invalid_mismatch(self):
        f = get_solution("valid_parentheses")
        assert f("(]") == False

    def test_invalid_order(self):
        f = get_solution("valid_parentheses")
        assert f("([)]") == False

    def test_valid_edge_empty(self):
        f = get_solution("valid_parentheses")
        assert f("") == True


class TestMinStack:
    def test_min_stack_basic(self):
        f = get_solution("min_stack")
        MinStack = f()
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.getMin() == -3
        stack.pop()
        assert stack.top() == 0
        assert stack.getMin() == -2

    def test_min_stack_single(self):
        f = get_solution("min_stack")
        MinStack = f()
        stack = MinStack()
        stack.push(1)
        assert stack.getMin() == 1
        assert stack.top() == 1


class TestEvaluateRPN:
    def test_rpn_basic(self):
        f = get_solution("evaluate_rpn")
        assert f(["2", "1", "+", "3", "*"]) == 9

    def test_rpn_division(self):
        f = get_solution("evaluate_rpn")
        assert f(["4", "13", "5", "/", "+"]) == 6

    def test_rpn_complex(self):
        f = get_solution("evaluate_rpn")
        assert f(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22

    def test_rpn_single(self):
        f = get_solution("evaluate_rpn")
        assert f(["5"]) == 5


class TestDailyTemperatures:
    def test_temps_basic(self):
        f = get_solution("daily_temperatures")
        assert f([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_temps_decreasing(self):
        f = get_solution("daily_temperatures")
        assert f([30, 60, 90]) == [1, 1, 0]

    def test_temps_same(self):
        f = get_solution("daily_temperatures")
        assert f([30, 30, 30]) == [0, 0, 0]


class TestNextGreaterElement:
    def test_nge_basic(self):
        f = get_solution("next_greater_element")
        assert f([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

    def test_nge_all_greater(self):
        f = get_solution("next_greater_element")
        assert f([2, 4], [1, 2, 3, 4]) == [3, -1]


class TestQueueWithStacks:
    def test_queue_basic(self):
        f = get_solution("implement_queue_with_stacks")
        MyQueue = f()
        q = MyQueue()
        q.push(1)
        q.push(2)
        assert q.peek() == 1
        assert q.pop() == 1
        assert q.empty() == False


class TestSimplifyPath:
    def test_path_basic(self):
        f = get_solution("simplify_path")
        assert f("/home/") == "/home"

    def test_path_dotdot(self):
        f = get_solution("simplify_path")
        assert f("/../") == "/"

    def test_path_multiple_slashes(self):
        f = get_solution("simplify_path")
        assert f("/home//foo/") == "/home/foo"

    def test_path_complex(self):
        f = get_solution("simplify_path")
        assert f("/a/./b/../../c/") == "/c"


class TestLargestRectangleHistogram:
    def test_histogram_basic(self):
        f = get_solution("largest_rectangle_histogram")
        assert f([2, 1, 5, 6, 2, 3]) == 10

    def test_histogram_single(self):
        f = get_solution("largest_rectangle_histogram")
        assert f([2, 4]) == 4

    def test_histogram_all_same(self):
        f = get_solution("largest_rectangle_histogram")
        assert f([3, 3, 3, 3]) == 12

    def test_histogram_increasing(self):
        f = get_solution("largest_rectangle_histogram")
        assert f([1, 2, 3, 4, 5]) == 9
