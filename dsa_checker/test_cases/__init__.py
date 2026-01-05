"""
Test cases for all DSA topics.
"""
from ..types import TestCasesDict
from .topic_01_big_o import TOPIC_01_TESTS
from .topic_02_arrays_strings import TOPIC_02_TESTS
from .topic_03_hash_tables import TOPIC_03_TESTS
from .topic_04_two_pointers import TOPIC_04_TESTS
from .topic_06_stacks_queues import TOPIC_06_TESTS
from .topic_07_recursion import TOPIC_07_TESTS
from .topic_11_dp import TOPIC_11_TESTS
from .topic_12_greedy import TOPIC_12_TESTS
from .topic_15_intervals import TOPIC_15_TESTS

# Combine all test cases
TEST_CASES: TestCasesDict = {
    **TOPIC_01_TESTS,
    **TOPIC_02_TESTS,
    **TOPIC_03_TESTS,
    **TOPIC_04_TESTS,
    **TOPIC_06_TESTS,
    **TOPIC_07_TESTS,
    **TOPIC_11_TESTS,
    **TOPIC_12_TESTS,
    **TOPIC_15_TESTS,
}

__all__ = ["TEST_CASES"]
