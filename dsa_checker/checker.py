"""
Core check() implementation - standalone without pytest.
"""
from typing import Callable, Dict, Any, List

# Test cases for each function
TEST_CASES = {
    # =========================================================================
    # Topic 01: Big O Notation & Complexity Analysis
    # =========================================================================
    "sum_array": [
        {"args": [[1, 2, 3, 4, 5]], "expected": 15, "name": "basic positive"},
        {"args": [[-1, 1, -2, 2]], "expected": 0, "name": "basic mixed"},
        {"args": [[]], "expected": 0, "name": "edge empty"},
        {"args": [[42]], "expected": 42, "name": "edge single"},
        {"args": [[-1, -2, -3]], "expected": -6, "name": "edge negative"},
        {"args": [list(range(10000))], "expected": sum(range(10000)), "name": "perf large"},
    ],
    "has_duplicates": [
        {"args": [[1, 2, 3, 1]], "expected": True, "name": "basic true"},
        {"args": [[1, 2, 3, 4]], "expected": False, "name": "basic false"},
        {"args": [[]], "expected": False, "name": "edge empty"},
        {"args": [[1]], "expected": False, "name": "edge single"},
        {"args": [[5, 5, 5, 5]], "expected": True, "name": "edge all same"},
        {"args": [[-1, -2, -1]], "expected": True, "name": "edge negative"},
    ],
    "find_pair_with_sum": [
        {"args": [[2, 7, 11, 15], 9], "expected": True, "name": "basic true"},
        {"args": [[1, 2, 3, 4], 10], "expected": False, "name": "basic false"},
        {"args": [[3, 3], 6], "expected": True, "name": "edge duplicates"},
        {"args": [[1, 2], 10], "expected": False, "name": "edge two elements no"},
        {"args": [[-1, -2, -3, 4], 1], "expected": True, "name": "edge negative"},
        {"args": [[-5, 5, 1, 2], 0], "expected": True, "name": "edge zero target"},
    ],
    "print_pairs": [
        {"args": [[1, 2, 3]], "expected": [[1, 2], [1, 3], [2, 3]], "name": "basic"},
        {"args": [[1, 2, 3, 4]], "expected": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "name": "basic four"},
        {"args": [[]], "expected": [], "name": "edge empty"},
        {"args": [[1]], "expected": [], "name": "edge single"},
        {"args": [[5, 10]], "expected": [[5, 10]], "name": "edge two"},
    ],
    "binary_search": [
        {"args": [[-1, 0, 3, 5, 9, 12], 9], "expected": 4, "name": "basic found"},
        {"args": [[-1, 0, 3, 5, 9, 12], 2], "expected": -1, "name": "basic not found"},
        {"args": [[1, 2, 3, 4, 5], 1], "expected": 0, "name": "basic first"},
        {"args": [[1, 2, 3, 4, 5], 5], "expected": 4, "name": "basic last"},
        {"args": [[], 5], "expected": -1, "name": "edge empty"},
        {"args": [[5], 5], "expected": 0, "name": "edge single found"},
        {"args": [[5], 3], "expected": -1, "name": "edge single not found"},
        {"args": [[1, 3], 3], "expected": 1, "name": "edge two elements"},
    ],
    # =========================================================================
    # Topic 02: Arrays & Strings
    # =========================================================================
    "two_sum": [
        {"args": [[2, 7, 11, 15], 9], "expected": [0, 1], "name": "basic"},
        {"args": [[3, 2, 4], 6], "expected": [1, 2], "name": "basic middle"},
        {"args": [[3, 3], 6], "expected": [0, 1], "name": "edge duplicates"},
    ],
    "best_time_to_buy_sell": [
        {"args": [[7, 1, 5, 3, 6, 4]], "expected": 5, "name": "basic"},
        {"args": [[7, 6, 4, 3, 1]], "expected": 0, "name": "decreasing"},
        {"args": [[1, 2]], "expected": 1, "name": "edge two elements"},
    ],
    "contains_duplicate": [
        {"args": [[1, 2, 3, 1]], "expected": True, "name": "basic true"},
        {"args": [[1, 2, 3, 4]], "expected": False, "name": "basic false"},
        {"args": [[]], "expected": False, "name": "edge empty"},
    ],
    "max_subarray": [
        {"args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "expected": 6, "name": "basic"},
        {"args": [[1]], "expected": 1, "name": "edge single"},
        {"args": [[5, 4, -1, 7, 8]], "expected": 23, "name": "basic positive"},
    ],
    "rotate_array": [
        {"args": [[1, 2, 3, 4, 5, 6, 7], 3], "expected": [5, 6, 7, 1, 2, 3, 4], "name": "basic"},
        {"args": [[-1, -100, 3, 99], 2], "expected": [3, 99, -1, -100], "name": "basic negative"},
    ],
    "reverse_string": [
        {"args": [["h", "e", "l", "l", "o"]], "expected": ["o", "l", "l", "e", "h"], "name": "basic"},
        {"args": [["H", "a", "n", "n", "a", "h"]], "expected": ["h", "a", "n", "n", "a", "H"], "name": "basic palindrome"},
    ],
    "valid_anagram": [
        {"args": ["anagram", "nagaram"], "expected": True, "name": "basic true"},
        {"args": ["rat", "car"], "expected": False, "name": "basic false"},
        {"args": ["", ""], "expected": True, "name": "edge empty"},
    ],
    "longest_common_prefix": [
        {"args": [["flower", "flow", "flight"]], "expected": "fl", "name": "basic"},
        {"args": [["dog", "racecar", "car"]], "expected": "", "name": "no common"},
        {"args": [[]], "expected": "", "name": "edge empty"},
    ],
    "product_except_self": [
        {"args": [[1, 2, 3, 4]], "expected": [24, 12, 8, 6], "name": "basic"},
        {"args": [[-1, 1, 0, -3, 3]], "expected": [0, 0, 9, 0, 0], "name": "with zero"},
    ],
    # =========================================================================
    # Topic 03: Hash Tables
    # =========================================================================
    "first_unique_char": [
        {"args": ["leetcode"], "expected": 0, "name": "basic"},
        {"args": ["loveleetcode"], "expected": 2, "name": "basic middle"},
        {"args": ["aabb"], "expected": -1, "name": "no unique"},
    ],
    "group_anagrams": [
        {"args": [["eat", "tea", "tan", "ate", "nat", "bat"]], "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], "name": "basic", "compare": "set_of_sets"},
    ],
    "isomorphic_strings": [
        {"args": ["egg", "add"], "expected": True, "name": "basic true"},
        {"args": ["foo", "bar"], "expected": False, "name": "basic false"},
        {"args": ["paper", "title"], "expected": True, "name": "basic longer"},
    ],
    "word_pattern": [
        {"args": ["abba", "dog cat cat dog"], "expected": True, "name": "basic true"},
        {"args": ["abba", "dog cat cat fish"], "expected": False, "name": "basic false"},
    ],
    "longest_consecutive": [
        {"args": [[100, 4, 200, 1, 3, 2]], "expected": 4, "name": "basic"},
        {"args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9, "name": "longer"},
    ],
    "subarray_sum_equals_k": [
        {"args": [[1, 1, 1], 2], "expected": 2, "name": "basic"},
        {"args": [[1, 2, 3], 3], "expected": 2, "name": "basic two ways"},
    ],
    "top_k_frequent": [
        {"args": [[1, 1, 1, 2, 2, 3], 2], "expected": [1, 2], "name": "basic", "compare": "set"},
    ],
    # =========================================================================
    # Topic 04: Two Pointers & Sliding Window
    # =========================================================================
    "valid_palindrome": [
        {"args": ["A man, a plan, a canal: Panama"], "expected": True, "name": "basic true"},
        {"args": ["race a car"], "expected": False, "name": "basic false"},
        {"args": [" "], "expected": True, "name": "edge empty"},
    ],
    "two_sum_sorted": [
        {"args": [[2, 7, 11, 15], 9], "expected": [1, 2], "name": "basic"},
        {"args": [[2, 3, 4], 6], "expected": [1, 3], "name": "basic middle"},
    ],
    "three_sum": [
        {"args": [[-1, 0, 1, 2, -1, -4]], "expected": [[-1, -1, 2], [-1, 0, 1]], "name": "basic", "compare": "set_of_tuples"},
        {"args": [[0, 1, 1]], "expected": [], "name": "no triplet"},
        {"args": [[0, 0, 0]], "expected": [[0, 0, 0]], "name": "all zeros"},
    ],
    "container_with_most_water": [
        {"args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expected": 49, "name": "basic"},
        {"args": [[1, 1]], "expected": 1, "name": "edge two"},
    ],
    "max_sum_subarray_k": [
        {"args": [[1, 4, 2, 10, 23, 3, 1, 0, 20], 4], "expected": 39, "name": "basic"},
    ],
    "longest_substring_without_repeating": [
        {"args": ["abcabcbb"], "expected": 3, "name": "basic"},
        {"args": ["bbbbb"], "expected": 1, "name": "all same"},
        {"args": ["pwwkew"], "expected": 3, "name": "basic middle"},
    ],
    # =========================================================================
    # Topic 05: Linked Lists (simplified - would need ListNode class)
    # =========================================================================
    # =========================================================================
    # Topic 06: Stacks & Queues
    # =========================================================================
    "valid_parentheses": [
        {"args": ["()"], "expected": True, "name": "basic simple"},
        {"args": ["()[]{}"], "expected": True, "name": "basic mixed"},
        {"args": ["(]"], "expected": False, "name": "basic false"},
        {"args": ["([)]"], "expected": False, "name": "interleaved"},
        {"args": ["{[]}"], "expected": True, "name": "nested"},
    ],
    "evaluate_rpn": [
        {"args": [["2", "1", "+", "3", "*"]], "expected": 9, "name": "basic"},
        {"args": [["4", "13", "5", "/", "+"]], "expected": 6, "name": "with division"},
    ],
    "daily_temperatures": [
        {"args": [[73, 74, 75, 71, 69, 72, 76, 73]], "expected": [1, 1, 4, 2, 1, 1, 0, 0], "name": "basic"},
    ],
    # =========================================================================
    # Topic 07: Recursion & Backtracking
    # =========================================================================
    "fibonacci": [
        {"args": [0], "expected": 0, "name": "base zero"},
        {"args": [1], "expected": 1, "name": "base one"},
        {"args": [10], "expected": 55, "name": "basic"},
    ],
    "factorial": [
        {"args": [0], "expected": 1, "name": "base zero"},
        {"args": [1], "expected": 1, "name": "base one"},
        {"args": [5], "expected": 120, "name": "basic"},
    ],
    "subsets": [
        {"args": [[1, 2, 3]], "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], "name": "basic", "compare": "set_of_tuples"},
    ],
    "permutations": [
        {"args": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], "name": "basic", "compare": "set_of_tuples"},
    ],
    "generate_parentheses": [
        {"args": [3], "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"], "name": "basic", "compare": "set"},
    ],
    # =========================================================================
    # Topic 11: Dynamic Programming
    # =========================================================================
    "climbing_stairs": [
        {"args": [2], "expected": 2, "name": "basic two"},
        {"args": [3], "expected": 3, "name": "basic three"},
        {"args": [4], "expected": 5, "name": "basic four"},
    ],
    "house_robber": [
        {"args": [[1, 2, 3, 1]], "expected": 4, "name": "basic"},
        {"args": [[2, 7, 9, 3, 1]], "expected": 12, "name": "basic longer"},
    ],
    "coin_change": [
        {"args": [[1, 2, 5], 11], "expected": 3, "name": "basic"},
        {"args": [[2], 3], "expected": -1, "name": "impossible"},
        {"args": [[1], 0], "expected": 0, "name": "zero amount"},
    ],
    "longest_increasing_subsequence": [
        {"args": [[10, 9, 2, 5, 3, 7, 101, 18]], "expected": 4, "name": "basic"},
        {"args": [[0, 1, 0, 3, 2, 3]], "expected": 4, "name": "basic with dups"},
    ],
    "unique_paths": [
        {"args": [3, 7], "expected": 28, "name": "basic"},
        {"args": [3, 2], "expected": 3, "name": "basic smaller"},
    ],
    "word_break": [
        {"args": ["leetcode", ["leet", "code"]], "expected": True, "name": "basic true"},
        {"args": ["applepenapple", ["apple", "pen"]], "expected": True, "name": "basic reuse"},
        {"args": ["catsandog", ["cats", "dog", "sand", "and", "cat"]], "expected": False, "name": "basic false"},
    ],
}


def _compare_results(result, expected, compare_mode=None):
    """Compare results with special handling for unordered collections."""
    if compare_mode == "set":
        return set(result) == set(expected)
    elif compare_mode == "set_of_tuples":
        return set(tuple(x) if isinstance(x, list) else x for x in result) == \
               set(tuple(x) if isinstance(x, list) else x for x in expected)
    elif compare_mode == "set_of_sets":
        return set(frozenset(x) for x in result) == set(frozenset(x) for x in expected)
    else:
        return result == expected


def _display_results(passed: int, failed: int, first_failure: dict = None):
    """Display test results."""
    total = passed + failed

    try:
        from IPython.display import display, HTML
        in_notebook = True
    except ImportError:
        in_notebook = False

    if total == 0:
        if in_notebook:
            html = """
            <div style="padding: 12px; background: #fff3cd; border-radius: 6px; border-left: 4px solid #ffc107;">
                <span style="color: #856404; font-weight: bold;">No tests found</span>
            </div>
            """
            display(HTML(html))
        else:
            print("No tests found")
        return

    all_passed = failed == 0
    pass_rate = (passed / total * 100)

    if in_notebook:
        if all_passed:
            status_color = "#28a745"
            status_bg = "#d4edda"
            status_text = f"✓ All {total} tests passed!"
        else:
            status_color = "#dc3545"
            status_bg = "#f8d7da"
            status_text = f"✗ Passed {passed}/{total} tests"

        html = f"""
        <div style="padding: 12px; background: {status_bg}; border-radius: 6px; border-left: 4px solid {status_color}; margin: 8px 0; font-family: system-ui, -apple-system, sans-serif;">
            <div style="font-size: 16px; font-weight: bold; color: {status_color};">
                {status_text}
            </div>
            <div style="margin-top: 8px; background: #e9ecef; border-radius: 4px; height: 6px; overflow: hidden;">
                <div style="background: #28a745; height: 100%; width: {pass_rate}%;"></div>
            </div>
        """

        if first_failure:
            html += f"""
            <div style="margin-top: 10px; font-size: 13px; color: #666;">
                <strong>First failure:</strong> {first_failure['name']}<br>
                <code style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px;">
                    Expected: {first_failure['expected']}, Got: {first_failure['got']}
                </code>
            </div>
            """

        html += '</div>'
        display(HTML(html))
    else:
        if all_passed:
            print(f"✅ All {total} tests passed!")
        else:
            print(f"❌ Passed {passed}/{total} tests")
            if first_failure:
                print(f"   First failure: {first_failure['name']}")
                print(f"   Expected: {first_failure['expected']}, Got: {first_failure['got']}")


def check(func: Callable) -> Dict[str, Any]:
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
            from IPython.display import display, HTML
            html = f"""
            <div style="padding: 12px; background: #fff3cd; border-radius: 6px; border-left: 4px solid #ffc107;">
                <span style="color: #856404;">no tests found for check({func_name})</span>
            </div>
            """
            display(HTML(html))
        except ImportError:
            print(f"no tests found for check({func_name})")
        return {"error": "No tests found", "passed": 0, "failed": 0, "total": 0}

    tests = TEST_CASES[func_name]
    passed = 0
    failed = 0
    first_failure = None

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
                        "expected": test["expected"],
                        "got": result
                    }
        except Exception as e:
            failed += 1
            if first_failure is None:
                first_failure = {
                    "name": test["name"],
                    "expected": test["expected"],
                    "got": f"Error: {e}"
                }

    _display_results(passed, failed, first_failure)

    return {
        "passed": passed,
        "failed": failed,
        "total": passed + failed,
        "all_passed": failed == 0
    }


def get_solution(func_name: str):
    """Compatibility function for existing tests."""
    return None
