"""
DSA Checker - Standalone test runner for DSA exercises.
"""
from __future__ import annotations

from typing import Any, Callable, Optional, cast

from .test_cases import TEST_CASES


def _compare_results(
    result: Any, expected: Any, compare_mode: Optional[str] = None
) -> bool:
    """Compare results with special handling for unordered collections."""
    if compare_mode == "set":
        return set(result) == set(expected)
    elif compare_mode == "set_of_tuples":
        def to_tuple_set(items: Any) -> set[Any]:
            return {tuple(cast(list[Any], x)) if isinstance(x, list) else x for x in items}
        return to_tuple_set(result) == to_tuple_set(expected)
    elif compare_mode == "set_of_sets":
        def to_frozen_set(items: Any) -> set[frozenset[Any]]:
            return {frozenset(cast(list[Any], x)) for x in items}
        return to_frozen_set(result) == to_frozen_set(expected)
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
    passed: int, failed: int, first_failure: Optional[dict[str, Any]] = None
) -> None:
    """Display test results."""
    total = passed + failed

    try:
        from IPython.display import display  # type: ignore[import-not-found]  # noqa: F401

        in_notebook = True
    except ImportError:
        in_notebook = False

    if total == 0:
        if in_notebook:
            _display_notebook(
                '<div style="padding: 12px; background: #fff3cd; border-radius: 6px; border-left: 4px solid #ffc107; width: 350px; box-sizing: border-box;">'
                '<span style="color: #856404; font-weight: bold;">No tests found</span></div>'
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

        html = f'<div style="padding: 12px; background: {status_bg}; border-radius: 6px; border-left: 4px solid {status_color}; margin: 8px 0; font-family: system-ui, -apple-system, sans-serif; width: 350px; box-sizing: border-box;">'
        html += f'<div style="font-size: 16px; font-weight: bold; color: {status_color};">{status_text}</div>'
        html += f'<div style="margin-top: 8px; background: #e9ecef; border-radius: 4px; height: 6px; overflow: hidden;"><div style="background: #28a745; height: 100%; width: {pass_rate}%;"></div></div>'

        if first_failure:
            test_num = first_failure.get('test_num', '?')
            total_tests = first_failure.get('total_tests', '?')
            args_repr = repr(first_failure['args']) if len(first_failure.get('args', [])) > 1 else repr(first_failure['args'][0]) if first_failure.get('args') else '()'
            expected_repr = repr(first_failure['expected'])
            got_repr = repr(first_failure['got']) if not first_failure.get('is_error') else first_failure['got']

            # Show type mismatch info if types differ and it's not an error
            type_info = ""
            if not first_failure.get('is_error'):
                expected_type = type(first_failure['expected']).__name__
                got_type = type(first_failure['got']).__name__
                if expected_type != got_type:
                    type_info = f" <span style='color: #856404;'>(type: expected {expected_type}, got {got_type})</span>"

            html += f'<div style="margin-top: 10px; font-size: 13px; color: #666;">'
            html += f'<strong>Failed test {test_num}/{total_tests}:</strong> {first_failure["name"]}<br>'
            html += f'<div style="background: #f8f9fa; padding: 8px 10px; border-radius: 4px; margin-top: 6px; font-family: monospace; font-size: 12px;">'
            html += f'<div><strong>Input:</strong> {args_repr}</div>'
            html += f'<div style="margin-top: 4px;"><strong>Expected:</strong> {expected_repr}</div>'
            html += f'<div style="margin-top: 4px;"><strong>Got:</strong> {got_repr}{type_info}</div>'
            html += '</div></div>'

        html += "</div>"
        _display_notebook(html)
    else:
        if all_passed:
            print(f"✅ All {total} tests passed!")
        else:
            print(f"❌ Passed {passed}/{total} tests")
            if first_failure:
                test_num = first_failure.get('test_num', '?')
                total_tests = first_failure.get('total_tests', '?')
                args_repr = repr(first_failure['args']) if len(first_failure.get('args', [])) > 1 else repr(first_failure['args'][0]) if first_failure.get('args') else '()'
                expected_repr = repr(first_failure['expected'])
                got_repr = repr(first_failure['got']) if not first_failure.get('is_error') else first_failure['got']

                print(f"\n   Failed test {test_num}/{total_tests}: {first_failure['name']}")
                print(f"   Input:    {args_repr}")
                print(f"   Expected: {expected_repr}")
                print(f"   Got:      {got_repr}")

                # Show type mismatch info if types differ and it's not an error
                if not first_failure.get('is_error'):
                    expected_type = type(first_failure['expected']).__name__
                    got_type = type(first_failure['got']).__name__
                    if expected_type != got_type:
                        print(f"   (type mismatch: expected {expected_type}, got {got_type})")


def check(func: Callable[..., Any]) -> dict[str, Any]:
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
            from IPython.display import HTML, display  # type: ignore[import-not-found]

            html = (
                f'<div style="padding: 12px; background: #fff3cd; border-radius: 6px; border-left: 4px solid #ffc107; width: 350px; box-sizing: border-box;">'
                f'<span style="color: #856404;">no tests found for check({func_name})</span></div>'
            )
            display(HTML(html))
        except ImportError:
            print(f"no tests found for check({func_name})")
        return {"error": "No tests found", "passed": 0, "failed": 0, "total": 0}

    tests = TEST_CASES[func_name]
    passed = 0
    failed = 0
    first_failure: Optional[dict[str, Any]] = None

    for test in tests:
        try:
            result = func(*test["args"])
            compare_mode = test.get("compare")

            if _compare_results(result, test["expected"], compare_mode):
                passed += 1
            else:
                failed += 1
                if first_failure is None:
                    first_failure = {
                        "name": test["name"],
                        "args": test["args"],
                        "expected": test["expected"],
                        "got": result,
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
