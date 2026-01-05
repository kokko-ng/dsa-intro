"""
Type definitions for DSA Checker.
"""
from typing import Any, NotRequired, TypedDict


class TestCase(TypedDict):
    """A single test case."""

    args: list[Any]
    expected: Any
    name: str
    compare: NotRequired[str]


TestCaseList = list[TestCase]
TestCasesDict = dict[str, TestCaseList]
