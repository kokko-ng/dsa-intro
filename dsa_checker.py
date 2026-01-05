"""
DSA Checker - Test runner for DSA exercises
"""

# Test cases for each exercise
TEST_CASES = {
    "sum_array": [
        {"input": {"nums": [1, 2, 3, 4, 5]}, "expected": 15},
        {"input": {"nums": []}, "expected": 0},
        {"input": {"nums": [10]}, "expected": 10},
        {"input": {"nums": [-1, -2, -3]}, "expected": -6},
        {"input": {"nums": [-1, 1, -2, 2]}, "expected": 0},
    ],
    "has_duplicates": [
        {"input": {"nums": [1, 2, 3, 1]}, "expected": True},
        {"input": {"nums": [1, 2, 3, 4]}, "expected": False},
        {"input": {"nums": []}, "expected": False},
        {"input": {"nums": [1]}, "expected": False},
        {"input": {"nums": [1, 1, 1, 1]}, "expected": True},
    ],
    "find_pair_with_sum": [
        {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": True},
        {"input": {"nums": [1, 2, 3, 4], "target": 10}, "expected": False},
        {"input": {"nums": [3, 3], "target": 6}, "expected": True},
        {"input": {"nums": [], "target": 5}, "expected": False},
        {"input": {"nums": [1], "target": 2}, "expected": False},
        {"input": {"nums": [-1, 2, 3, -4], "target": -5}, "expected": True},
    ],
    "print_pairs": [
        {"input": {"nums": [1, 2, 3]}, "expected": [[1, 2], [1, 3], [2, 3]]},
        {"input": {"nums": [1]}, "expected": []},
        {"input": {"nums": []}, "expected": []},
        {"input": {"nums": [1, 2]}, "expected": [[1, 2]]},
        {"input": {"nums": [4, 5, 6, 7]}, "expected": [[4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]},
    ],
    "binary_search": [
        {"input": {"nums": [-1, 0, 3, 5, 9, 12], "target": 9}, "expected": 4},
        {"input": {"nums": [-1, 0, 3, 5, 9, 12], "target": 2}, "expected": -1},
        {"input": {"nums": [], "target": 5}, "expected": -1},
        {"input": {"nums": [5], "target": 5}, "expected": 0},
        {"input": {"nums": [1, 2, 3], "target": 0}, "expected": -1},
        {"input": {"nums": [1, 2, 3], "target": 4}, "expected": -1},
        {"input": {"nums": [1, 2, 3, 4, 5], "target": 1}, "expected": 0},
        {"input": {"nums": [1, 2, 3, 4, 5], "target": 5}, "expected": 4},
    ],
}


def check(func):
    """
    Run test cases for the given function.

    Args:
        func: The function to test
    """
    func_name = func.__name__

    if func_name not in TEST_CASES:
        print(f"no tests found for check({func_name})")
        return

    tests = TEST_CASES[func_name]
    passed = 0
    failed = 0

    for i, test in enumerate(tests):
        try:
            result = func(**test["input"])
            expected = test["expected"]

            if result == expected:
                passed += 1
            else:
                failed += 1
                if failed == 1:
                    print(f"❌ Test {i + 1} FAILED")
                    print(f"   Input: {test['input']}")
                    print(f"   Expected: {expected}")
                    print(f"   Got: {result}")
        except Exception as e:
            failed += 1
            if failed == 1:
                print(f"❌ Test {i + 1} ERROR")
                print(f"   Input: {test['input']}")
                print(f"   Error: {e}")

    total = passed + failed
    if failed == 0:
        print(f"✅ All {total} tests passed!")
    else:
        print(f"\n📊 Results: {passed}/{total} tests passed")
