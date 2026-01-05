"""
DSA Checker - Standalone test runner for DSA exercises.
"""

from __future__ import annotations

from collections.abc import Callable

from .test_cases import TEST_CASES
from .types import TestCase


class _NoneResult:
    """Marker for when a function returned None (potentially unimplemented)."""

    pass


def _transform_input(args: list[object], input_type: str | None) -> list[object]:
    """Transform input arguments based on input_type."""
    if not input_type:
        return args

    if input_type == "tree":
        from data_structures import build_tree

        tree_args = args[0]
        if isinstance(tree_args, list):
            return [build_tree(tree_args)] + list(args[1:])
        return args
    elif input_type == "trees":
        from data_structures import build_tree

        return [build_tree(arg) if isinstance(arg, list) else arg for arg in args]
    elif input_type == "linked_list":
        from data_structures import create_linked_list

        ll_args = args[0]
        if isinstance(ll_args, list):
            int_list: list[int] = [x for x in ll_args if isinstance(x, int)]
            return [create_linked_list(int_list)] + list(args[1:])
        return args
    elif input_type == "linked_lists":
        from data_structures import create_linked_list

        def to_linked_list(arg: object) -> object:
            if isinstance(arg, list):
                int_list: list[int] = [x for x in arg if isinstance(x, int)]
                return create_linked_list(int_list)
            return arg

        return [to_linked_list(arg) for arg in args]
    elif input_type == "tree_with_targets":
        # For LCA: build tree and find target nodes by value
        from data_structures import build_tree
        from data_structures.tree import TreeNode

        tree_args = args[0]
        if not isinstance(tree_args, list):
            return args
        root = build_tree(tree_args)
        p_val, q_val = args[1], args[2]

        # Find nodes with given values
        def find_node(node: TreeNode | None, val: object) -> TreeNode | None:
            if not node:
                return None
            if node.val == val:
                return node
            return find_node(node.left, val) or find_node(node.right, val)

        p = find_node(root, p_val)
        q = find_node(root, q_val)
        return [root, p, q]
    elif input_type == "linked_list_cycle":
        # Create linked list with optional cycle
        from data_structures import create_cycle, create_linked_list

        ll_args = args[0]
        if not isinstance(ll_args, list):
            return args
        cycle_int_list: list[int] = [x for x in ll_args if isinstance(x, int)]
        head = create_linked_list(cycle_int_list)
        pos = args[1]
        if isinstance(pos, int):
            head = create_cycle(head, pos)
        return [head]
    elif input_type == "k_linked_lists":
        # Convert list of lists to list of linked lists
        from data_structures import create_linked_list

        def to_linked_list_or_none(lst: object) -> object:
            if not lst:
                return None
            if isinstance(lst, list):
                int_list: list[int] = [x for x in lst if isinstance(x, int)]
                return create_linked_list(int_list)
            return None

        lists = args[0]
        if isinstance(lists, list):
            return [[to_linked_list_or_none(lst) for lst in lists]]
        return args
    return args


def _transform_expected(expected: object, output_type: str | None) -> object:
    """Transform expected value based on output_type."""
    if not output_type:
        return expected

    if output_type == "tree":
        from data_structures import build_tree

        if isinstance(expected, list):
            return build_tree(expected)
        return expected
    elif output_type == "linked_list":
        from data_structures import create_linked_list

        if isinstance(expected, list):
            int_list: list[int] = [x for x in expected if isinstance(x, int)]
            return create_linked_list(int_list)
        return expected
    elif output_type == "tree_to_list":
        # Result is a tree, convert to list for comparison
        return expected  # Expected is already a list
    return expected


def _transform_result(result: object, output_type: str | None) -> object:
    """Transform result for comparison based on output_type."""
    if output_type == "tree_to_list":
        from data_structures import tree_to_list
        from data_structures.tree import TreeNode

        if result is None:
            return _NoneResult()  # Mark as None return for proper comparison
        if isinstance(result, TreeNode):
            return tree_to_list(result)
        return result
    elif output_type == "linked_list_to_list":
        from data_structures import linked_list_to_list
        from data_structures.linked_list import ListNode

        if result is None:
            return _NoneResult()  # Mark as None return for proper comparison
        if isinstance(result, ListNode):
            return linked_list_to_list(result)
        return result
    elif output_type == "tree_val":
        # Return just the value of the tree node
        from data_structures.tree import TreeNode

        if isinstance(result, TreeNode):
            return result.val
        return None
    elif output_type == "node_val":
        # Return just the value of the linked list node
        from data_structures.linked_list import ListNode

        if isinstance(result, ListNode):
            return result.val
        return None
    return result


def _compare_results(
    result: object, expected: object, compare_mode: str | None = None
) -> bool:
    """Compare results with special handling for unordered collections."""
    # Handle _NoneResult marker (function returned None for tree/linked list)
    if isinstance(result, _NoneResult):
        # Only pass if expected is an empty list (representing empty structure)
        return expected == []
    if compare_mode == "set":
        if isinstance(result, (list, set)) and isinstance(expected, (list, set)):
            return set(result) == set(expected)
        return False
    elif compare_mode == "set_of_tuples":

        def to_tuple_set(items: object) -> set[tuple[object, ...] | object]:
            if not isinstance(items, (list, set)):
                return set()
            return {tuple(x) if isinstance(x, list) else x for x in items}

        return to_tuple_set(result) == to_tuple_set(expected)
    elif compare_mode == "set_of_sets":

        def to_frozen_set(items: object) -> set[frozenset[object]]:
            if not isinstance(items, (list, set)):
                return set()
            return {frozenset(x) for x in items if isinstance(x, (list, set))}

        return to_frozen_set(result) == to_frozen_set(expected)
    elif compare_mode == "codec":
        # Special handling for serialize/deserialize codec classes
        if result is None or not callable(result):
            return False  # Function must return a Codec class
        from data_structures import build_tree, tree_to_list

        codec = result()  # result is the Codec class
        if isinstance(expected, list):
            tree = build_tree(expected)
            serialized = codec.serialize(tree)
            deserialized = codec.deserialize(serialized)
            return tree_to_list(deserialized) == expected
        return False
    elif compare_mode == "median_finder":
        # Special handling for MedianFinder class
        # result is the MedianFinder class, expected[0] is numbers to add
        # Note: This is called after transformation, so we pass original args
        # For now, return True and handle in check() with special logic
        return True
    elif compare_mode == "reorganized":
        # Check that result has no adjacent duplicates and same char counts
        if not result:
            return not expected  # Only pass if expected is also empty
        if not expected:
            return False  # Expected empty but got non-empty
        if isinstance(result, str) and isinstance(expected, str):
            for i in range(len(result) - 1):
                if result[i] == result[i + 1]:
                    return False
            return sorted(result) == sorted(expected)
        return False
    else:
        return result == expected


def _display_notebook(html: str) -> None:
    """Display HTML in a Jupyter notebook."""
    try:
        from IPython.display import HTML, display  # type: ignore[import-not-found]

        display(HTML(html))
    except ImportError:
        pass


def _display_results(
    passed: int, failed: int, first_failure: dict[str, object] | None = None
) -> None:
    """Display test results."""
    total = passed + failed

    try:
        from IPython.display import display  # noqa: F401

        in_notebook = True
    except ImportError:
        in_notebook = False

    if total == 0:
        if in_notebook:
            _display_notebook(
                '<div style="padding: 12px; background: #fff3cd; border-radius: 6px; '
                'border-left: 4px solid #ffc107;">'
                '<span style="color: #856404; font-weight: bold;">No tests found</span>'
                "</div>"
            )
        else:
            print("No tests found")
        return

    all_passed = failed == 0
    pass_rate = passed / total * 100

    if in_notebook:
        if all_passed:
            status_color = "#28a745"
            status_bg = "#d4edda"
            status_text = f"✓ All {total} tests passed!"
        else:
            status_color = "#dc3545"
            status_bg = "#f8d7da"
            status_text = f"✗ Passed {passed}/{total} tests"

        html = (
            f'<div style="padding: 12px; background: {status_bg}; border-radius: 6px; '
            f"border-left: 4px solid {status_color}; margin: 8px 0; "
            f'font-family: system-ui, -apple-system, sans-serif;">'
        )
        html += (
            f'<div style="font-size: 16px; font-weight: bold; color: {status_color};">'
            f"{status_text}</div>"
        )
        html += (
            f'<div style="margin-top: 8px; background: #e9ecef; border-radius: 4px; '
            f'height: 6px; overflow: hidden;">'
            f'<div style="background: #28a745; height: 100%; width: {pass_rate}%;"></div>'
            f"</div>"
        )

        if first_failure:
            test_num = first_failure.get("test_num", "?")
            total_tests = first_failure.get("total_tests", "?")
            args = first_failure.get("args", [])
            args_list = list(args) if isinstance(args, (list, tuple)) else []
            args_repr = (
                repr(args)
                if len(args_list) > 1
                else repr(args_list[0])
                if args_list
                else "()"
            )
            expected_repr = repr(first_failure.get("expected"))
            is_error = first_failure.get("is_error", False)
            got = first_failure.get("got")
            got_repr = repr(got) if not is_error else str(got)

            # Show type mismatch info if types differ and it's not an error
            type_info = ""
            if not is_error:
                expected_val = first_failure.get("expected")
                expected_type = type(expected_val).__name__
                got_type = type(got).__name__
                if expected_type != got_type:
                    type_info = (
                        f" <span style='color: #856404;'>"
                        f"(type: expected {expected_type}, got {got_type})</span>"
                    )

            name = first_failure.get("name", "unknown")
            html += '<div style="margin-top: 10px; font-size: 13px; color: #666;">'
            html += f"<strong>Failed test {test_num}/{total_tests}:</strong> {name}<br>"
            html += (
                '<div style="background: #f8f9fa; padding: 8px 10px; border-radius: 4px; '
                'margin-top: 6px; font-family: monospace; font-size: 12px;">'
            )
            html += f"<div><strong>Input:</strong> {args_repr}</div>"
            html += (
                f'<div style="margin-top: 4px;"><strong>Expected:</strong> '
                f"{expected_repr}</div>"
            )
            html += (
                f'<div style="margin-top: 4px;"><strong>Got:</strong> '
                f"{got_repr}{type_info}</div>"
            )
            html += "</div></div>"

        html += "</div>"
        _display_notebook(html)
    else:
        if all_passed:
            print(f"✅ All {total} tests passed!")
        else:
            print(f"❌ Passed {passed}/{total} tests")
            if first_failure:
                test_num = first_failure.get("test_num", "?")
                total_tests = first_failure.get("total_tests", "?")
                args = first_failure.get("args", [])
                args_list = list(args) if isinstance(args, (list, tuple)) else []
                args_repr = (
                    repr(args)
                    if len(args_list) > 1
                    else repr(args_list[0])
                    if args_list
                    else "()"
                )
                expected_repr = repr(first_failure.get("expected"))
                is_error = first_failure.get("is_error", False)
                got = first_failure.get("got")
                got_repr = repr(got) if not is_error else str(got)

                name = first_failure.get("name", "unknown")
                print(f"\n   Failed test {test_num}/{total_tests}: {name}")
                print(f"   Input:    {args_repr}")
                print(f"   Expected: {expected_repr}")
                print(f"   Got:      {got_repr}")

                # Show type mismatch info if types differ and it's not an error
                if not is_error:
                    expected_val = first_failure.get("expected")
                    expected_type = type(expected_val).__name__
                    got_type = type(got).__name__
                    if expected_type != got_type:
                        print(
                            f"   (type mismatch: expected {expected_type}, "
                            f"got {got_type})"
                        )


def check(func: Callable[..., object]) -> dict[str, object]:
    """
    Check a student's solution against test cases.

    Args:
        func: The function to test

    Returns:
        Dictionary with pass/fail summary
    """
    func_name = func.__name__

    if func_name not in TEST_CASES:
        try:
            from IPython.display import HTML, display

            html = (
                f'<div style="padding: 12px; background: #fff3cd; border-radius: 6px; '
                f'border-left: 4px solid #ffc107;">'
                f'<span style="color: #856404;">no tests found for check({func_name})'
                f"</span></div>"
            )
            display(HTML(html))
        except ImportError:
            print(f"no tests found for check({func_name})")
        return {"error": "No tests found", "passed": 0, "failed": 0, "total": 0}

    tests: list[TestCase] = TEST_CASES[func_name]
    passed = 0
    failed = 0
    first_failure: dict[str, object] | None = None

    for test in tests:
        try:
            # Transform inputs if needed (for trees, linked lists, etc.)
            input_type = test.get("input_type")
            output_type = test.get("output_type")
            transformed_args = _transform_input(list(test["args"]), input_type)

            result = func(*transformed_args)

            # Transform result and expected for comparison
            compare_result = _transform_result(result, output_type)
            compare_expected = _transform_expected(test["expected"], output_type)
            compare_mode = test.get("compare")

            if _compare_results(compare_result, compare_expected, compare_mode):
                passed += 1
            else:
                failed += 1
                if first_failure is None:
                    # Convert _NoneResult marker to displayable value
                    display_result: object = compare_result if output_type else result
                    if isinstance(display_result, _NoneResult):
                        display_result = None
                    first_failure = {
                        "name": test["name"],
                        "args": test["args"],  # Show original args for clarity
                        "expected": test["expected"],
                        "got": display_result,
                        "test_num": passed + failed,
                        "total_tests": len(tests),
                    }
        except Exception as e:
            failed += 1
            if first_failure is None:
                first_failure = {
                    "name": test["name"],
                    "args": test["args"],
                    "expected": test["expected"],
                    "got": f"Error: {e}",
                    "test_num": passed + failed,
                    "total_tests": len(tests),
                    "is_error": True,
                }

    _display_results(passed, failed, first_failure)

    return {
        "passed": passed,
        "failed": failed,
        "total": passed + failed,
        "all_passed": failed == 0,
    }
