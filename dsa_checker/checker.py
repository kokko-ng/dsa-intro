"""
Core check() implementation using pytest programmatically.
"""
import pytest
import sys
import os
from typing import Callable, Optional, Dict, Any, List
from dataclasses import dataclass
from enum import Enum
from io import StringIO

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    ERROR = "error"


@dataclass
class TestResult:
    name: str
    status: TestStatus
    category: str  # "basic", "edge", "performance"


class ResultCollectorPlugin:
    """Custom pytest plugin to collect results without exposing test details."""

    def __init__(self):
        self.results: List[TestResult] = []
        self.total = 0
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            self.total += 1

            # Extract category from test name
            category = self._extract_category(report.nodeid)

            if report.passed:
                self.passed += 1
                status = TestStatus.PASSED
            else:
                self.failed += 1
                status = TestStatus.FAILED

            # Extract human-readable test name
            test_name = self._humanize_test_name(report.nodeid)

            self.results.append(TestResult(
                name=test_name,
                status=status,
                category=category
            ))

    def _extract_category(self, nodeid: str) -> str:
        """Extract category from test name patterns."""
        nodeid_lower = nodeid.lower()
        if "edge" in nodeid_lower:
            return "edge"
        elif "perf" in nodeid_lower or "large" in nodeid_lower:
            return "performance"
        else:
            return "basic"

    def _humanize_test_name(self, nodeid: str) -> str:
        """Convert test function name to readable format."""
        # Get just the function name after ::
        parts = nodeid.split("::")
        func_name = parts[-1] if parts else nodeid

        # Remove 'test_' prefix and convert underscores to spaces
        if func_name.startswith("test_"):
            func_name = func_name[5:]

        # Convert underscores to spaces and capitalize
        return func_name.replace("_", " ").title()


def _display_results(collector: ResultCollectorPlugin):
    """Display test results in Jupyter-friendly format."""
    try:
        from IPython.display import display, HTML
        in_notebook = True
    except ImportError:
        in_notebook = False

    if collector.total == 0:
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

    all_passed = collector.failed == 0
    pass_rate = (collector.passed / collector.total * 100)

    if in_notebook:
        # Rich HTML output for Jupyter
        if all_passed:
            status_icon = "&#10003;"  # checkmark
            status_color = "#28a745"
            status_bg = "#d4edda"
            status_text = "All tests passed!"
        else:
            status_icon = "&#10007;"  # X mark
            status_color = "#dc3545"
            status_bg = "#f8d7da"
            status_text = f"Passed {collector.passed}/{collector.total} tests"

        html = f"""
        <div style="padding: 12px; background: {status_bg}; border-radius: 6px; border-left: 4px solid {status_color}; margin: 8px 0; font-family: system-ui, -apple-system, sans-serif;">
            <div style="font-size: 16px; font-weight: bold; color: {status_color};">
                {status_icon} {status_text}
            </div>
            <div style="margin-top: 8px; background: #e9ecef; border-radius: 4px; height: 6px; overflow: hidden;">
                <div style="background: #28a745; height: 100%; width: {pass_rate}%;"></div>
            </div>
        """

        # Show failed categories (not specific tests)
        if not all_passed:
            failed_categories = set()
            for result in collector.results:
                if result.status == TestStatus.FAILED:
                    failed_categories.add(result.category)

            if failed_categories:
                html += '<div style="margin-top: 10px; font-size: 14px; color: #666;">'
                html += '<strong>Failed categories:</strong> '
                category_labels = {
                    "basic": "Basic cases",
                    "edge": "Edge cases",
                    "performance": "Performance"
                }
                labels = [category_labels.get(c, c) for c in sorted(failed_categories)]
                html += ", ".join(labels)
                html += '</div>'

        html += '</div>'
        display(HTML(html))
    else:
        # Plain text output for terminal
        if all_passed:
            print(f"✓ All tests passed! ({collector.total}/{collector.total})")
        else:
            print(f"✗ Passed {collector.passed}/{collector.total} tests")
            failed_categories = set()
            for result in collector.results:
                if result.status == TestStatus.FAILED:
                    failed_categories.add(result.category)
            if failed_categories:
                print(f"  Failed categories: {', '.join(sorted(failed_categories))}")


# Global storage for student solutions
_student_solutions: Dict[str, Callable] = {}


def check(func: Callable) -> Dict[str, Any]:
    """
    Check a student's solution against hidden test cases.

    Args:
        func: The function to test (passed by reference)

    Returns:
        Dictionary with pass/fail summary

    Example:
        >>> def two_sum(nums, target):
        ...     # your implementation
        ...     pass
        >>> check(two_sum)
        ✓ Passed: 8/10 tests
    """
    from .registry import get_test_info

    func_name = func.__name__

    # Store the function globally so tests can access it
    _student_solutions[func_name] = func

    # Get test file and pattern
    test_info = get_test_info(func_name)

    if test_info is None:
        try:
            from IPython.display import display, HTML
            html = f"""
            <div style="padding: 12px; background: #f8d7da; border-radius: 6px; border-left: 4px solid #dc3545;">
                <span style="color: #721c24; font-weight: bold;">Error:</span> No tests found for function '{func_name}'
            </div>
            """
            display(HTML(html))
        except ImportError:
            print(f"Error: No tests found for function '{func_name}'")
        return {"error": "No tests found", "passed": 0, "failed": 0, "total": 0}

    test_file, test_pattern = test_info
    test_path = os.path.join(PROJECT_ROOT, "tests", test_file)

    if not os.path.exists(test_path):
        try:
            from IPython.display import display, HTML
            html = f"""
            <div style="padding: 12px; background: #f8d7da; border-radius: 6px; border-left: 4px solid #dc3545;">
                <span style="color: #721c24; font-weight: bold;">Error:</span> Test file not found: {test_file}
            </div>
            """
            display(HTML(html))
        except ImportError:
            print(f"Error: Test file not found: {test_file}")
        return {"error": "Test file not found", "passed": 0, "failed": 0, "total": 0}

    # Create result collector plugin
    collector = ResultCollectorPlugin()

    # Capture stdout/stderr to hide pytest output
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()

    try:
        # Run pytest programmatically
        pytest.main(
            [
                test_path,
                "-k", test_pattern,
                "-q",
                "--tb=no",
                "--no-header",
                "-p", "no:cacheprovider",
                "--timeout=5",
            ],
            plugins=[collector]
        )
    finally:
        # Restore stdout/stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr

    # Display results
    _display_results(collector)

    return {
        "passed": collector.passed,
        "failed": collector.failed,
        "total": collector.total,
        "all_passed": collector.failed == 0
    }


def get_solution(func_name: str) -> Optional[Callable]:
    """Get a stored student solution by name. Used by test files."""
    return _student_solutions.get(func_name)
