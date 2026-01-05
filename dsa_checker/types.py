"""
Type definitions for DSA Checker.
"""
from typing import NotRequired, TypedDict


class TestCase(TypedDict):
    """A single test case."""

    args: list[object]
    expected: object
    name: str
    compare: NotRequired[str]
    input_type: NotRequired[str]
    output_type: NotRequired[str]


TestCaseList = list[TestCase]
TestCasesDict = dict[str, TestCaseList]
