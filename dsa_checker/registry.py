"""
Registry mapping function names to their test files and patterns.
"""
from typing import Tuple, Optional

# Registry: function_name -> (test_file, test_pattern)
# test_pattern is used with pytest -k to select matching tests
FUNCTION_REGISTRY = {
    # =========================================================================
    # Topic 01: Big O Notation & Complexity Analysis
    # =========================================================================
    "sum_array": ("test_01_big_o.py", "test_sum_array"),
    "has_duplicates": ("test_01_big_o.py", "test_has_duplicates"),
    "find_pair_with_sum": ("test_01_big_o.py", "test_find_pair_with_sum"),
    "print_pairs": ("test_01_big_o.py", "test_print_pairs"),
    "binary_search": ("test_01_big_o.py", "test_binary_search"),

    # =========================================================================
    # Topic 02: Arrays & Strings
    # =========================================================================
    "two_sum": ("test_02_arrays_strings.py", "test_two_sum"),
    "best_time_to_buy_sell": ("test_02_arrays_strings.py", "test_best_time_to_buy_sell"),
    "contains_duplicate": ("test_02_arrays_strings.py", "test_contains_duplicate"),
    "max_subarray": ("test_02_arrays_strings.py", "test_max_subarray"),
    "rotate_array": ("test_02_arrays_strings.py", "test_rotate_array"),
    "reverse_string": ("test_02_arrays_strings.py", "test_reverse_string"),
    "valid_anagram": ("test_02_arrays_strings.py", "test_valid_anagram"),
    "longest_common_prefix": ("test_02_arrays_strings.py", "test_longest_common_prefix"),
    "string_to_integer": ("test_02_arrays_strings.py", "test_string_to_integer"),
    "product_except_self": ("test_02_arrays_strings.py", "test_product_except_self"),

    # =========================================================================
    # Topic 03: Hash Tables
    # =========================================================================
    "first_unique_char": ("test_03_hash_tables.py", "test_first_unique_char"),
    "group_anagrams": ("test_03_hash_tables.py", "test_group_anagrams"),
    "isomorphic_strings": ("test_03_hash_tables.py", "test_isomorphic_strings"),
    "word_pattern": ("test_03_hash_tables.py", "test_word_pattern"),
    "intersection_of_arrays": ("test_03_hash_tables.py", "test_intersection_of_arrays"),
    "longest_consecutive": ("test_03_hash_tables.py", "test_longest_consecutive"),
    "subarray_sum_equals_k": ("test_03_hash_tables.py", "test_subarray_sum_equals_k"),
    "top_k_frequent": ("test_03_hash_tables.py", "test_top_k_frequent"),

    # =========================================================================
    # Topic 04: Two Pointers & Sliding Window
    # =========================================================================
    "valid_palindrome": ("test_04_two_pointers.py", "test_valid_palindrome"),
    "two_sum_sorted": ("test_04_two_pointers.py", "test_two_sum_sorted"),
    "three_sum": ("test_04_two_pointers.py", "test_three_sum"),
    "container_with_most_water": ("test_04_two_pointers.py", "test_container_with_most_water"),
    "remove_duplicates_sorted": ("test_04_two_pointers.py", "test_remove_duplicates_sorted"),
    "max_sum_subarray_k": ("test_04_two_pointers.py", "test_max_sum_subarray_k"),
    "longest_substring_without_repeating": ("test_04_two_pointers.py", "test_longest_substring_without_repeating"),
    "minimum_window_substring": ("test_04_two_pointers.py", "test_minimum_window_substring"),

    # =========================================================================
    # Topic 05: Linked Lists
    # =========================================================================
    "reverse_list": ("test_05_linked_lists.py", "test_reverse_list"),
    "merge_two_lists": ("test_05_linked_lists.py", "test_merge_two_lists"),
    "has_cycle": ("test_05_linked_lists.py", "test_has_cycle"),
    "remove_nth_from_end": ("test_05_linked_lists.py", "test_remove_nth_from_end"),
    "find_middle": ("test_05_linked_lists.py", "test_find_middle"),
    "is_palindrome_list": ("test_05_linked_lists.py", "test_is_palindrome_list"),
    "add_two_numbers": ("test_05_linked_lists.py", "test_add_two_numbers"),
    "reorder_list": ("test_05_linked_lists.py", "test_reorder_list"),

    # =========================================================================
    # Topic 06: Stacks & Queues
    # =========================================================================
    "valid_parentheses": ("test_06_stacks_queues.py", "test_valid_parentheses"),
    "min_stack": ("test_06_stacks_queues.py", "test_min_stack"),
    "evaluate_rpn": ("test_06_stacks_queues.py", "test_evaluate_rpn"),
    "daily_temperatures": ("test_06_stacks_queues.py", "test_daily_temperatures"),
    "next_greater_element": ("test_06_stacks_queues.py", "test_next_greater_element"),
    "implement_queue_with_stacks": ("test_06_stacks_queues.py", "test_implement_queue_with_stacks"),
    "simplify_path": ("test_06_stacks_queues.py", "test_simplify_path"),
    "largest_rectangle_histogram": ("test_06_stacks_queues.py", "test_largest_rectangle_histogram"),

    # =========================================================================
    # Topic 07: Recursion & Backtracking
    # =========================================================================
    "fibonacci": ("test_07_recursion.py", "test_fibonacci"),
    "factorial": ("test_07_recursion.py", "test_factorial"),
    "subsets": ("test_07_recursion.py", "test_subsets"),
    "permutations": ("test_07_recursion.py", "test_permutations"),
    "combination_sum": ("test_07_recursion.py", "test_combination_sum"),
    "letter_combinations": ("test_07_recursion.py", "test_letter_combinations"),
    "generate_parentheses": ("test_07_recursion.py", "test_generate_parentheses"),
    "word_search": ("test_07_recursion.py", "test_word_search"),
    "n_queens": ("test_07_recursion.py", "test_n_queens"),
    "sudoku_solver": ("test_07_recursion.py", "test_sudoku_solver"),

    # =========================================================================
    # Topic 08: Trees
    # =========================================================================
    "max_depth": ("test_08_trees.py", "test_max_depth"),
    "invert_tree": ("test_08_trees.py", "test_invert_tree"),
    "is_same_tree": ("test_08_trees.py", "test_is_same_tree"),
    "is_symmetric": ("test_08_trees.py", "test_is_symmetric"),
    "level_order": ("test_08_trees.py", "test_level_order"),
    "validate_bst": ("test_08_trees.py", "test_validate_bst"),
    "lowest_common_ancestor": ("test_08_trees.py", "test_lowest_common_ancestor"),
    "kth_smallest_bst": ("test_08_trees.py", "test_kth_smallest_bst"),
    "build_tree_from_traversals": ("test_08_trees.py", "test_build_tree_from_traversals"),
    "serialize_deserialize": ("test_08_trees.py", "test_serialize_deserialize"),

    # =========================================================================
    # Topic 09: Heaps & Priority Queues
    # =========================================================================
    "kth_largest_element": ("test_09_heaps.py", "test_kth_largest_element"),
    "merge_k_lists": ("test_09_heaps.py", "test_merge_k_lists"),
    "top_k_frequent_elements": ("test_09_heaps.py", "test_top_k_frequent_elements"),
    "find_median": ("test_09_heaps.py", "test_find_median"),
    "k_closest_points": ("test_09_heaps.py", "test_k_closest_points"),
    "reorganize_string": ("test_09_heaps.py", "test_reorganize_string"),
    "task_scheduler": ("test_09_heaps.py", "test_task_scheduler"),

    # =========================================================================
    # Topic 10: Graphs
    # =========================================================================
    "num_islands": ("test_10_graphs.py", "test_num_islands"),
    "clone_graph": ("test_10_graphs.py", "test_clone_graph"),
    "course_schedule": ("test_10_graphs.py", "test_course_schedule"),
    "course_schedule_order": ("test_10_graphs.py", "test_course_schedule_order"),
    "pacific_atlantic": ("test_10_graphs.py", "test_pacific_atlantic"),
    "word_ladder": ("test_10_graphs.py", "test_word_ladder"),
    "surrounded_regions": ("test_10_graphs.py", "test_surrounded_regions"),
    "graph_valid_tree": ("test_10_graphs.py", "test_graph_valid_tree"),
    "count_connected_components": ("test_10_graphs.py", "test_count_connected_components"),
    "alien_dictionary": ("test_10_graphs.py", "test_alien_dictionary"),

    # =========================================================================
    # Topic 11: Dynamic Programming
    # =========================================================================
    "climbing_stairs": ("test_11_dp.py", "test_climbing_stairs"),
    "house_robber": ("test_11_dp.py", "test_house_robber"),
    "coin_change": ("test_11_dp.py", "test_coin_change"),
    "longest_increasing_subsequence": ("test_11_dp.py", "test_longest_increasing_subsequence"),
    "unique_paths": ("test_11_dp.py", "test_unique_paths"),
    "decode_ways": ("test_11_dp.py", "test_decode_ways"),
    "word_break": ("test_11_dp.py", "test_word_break"),
    "longest_common_subsequence": ("test_11_dp.py", "test_longest_common_subsequence"),
    "edit_distance": ("test_11_dp.py", "test_edit_distance"),
    "max_product_subarray": ("test_11_dp.py", "test_max_product_subarray"),

    # =========================================================================
    # Topic 12: Greedy Algorithms
    # =========================================================================
    "jump_game": ("test_12_greedy.py", "test_jump_game"),
    "jump_game_ii": ("test_12_greedy.py", "test_jump_game_ii"),
    "gas_station": ("test_12_greedy.py", "test_gas_station"),
    "candy": ("test_12_greedy.py", "test_candy"),
    "partition_labels": ("test_12_greedy.py", "test_partition_labels"),
    "valid_parenthesis_string": ("test_12_greedy.py", "test_valid_parenthesis_string"),
    "maximum_subarray_greedy": ("test_12_greedy.py", "test_maximum_subarray_greedy"),

    # =========================================================================
    # Topic 13: Tries
    # =========================================================================
    "implement_trie": ("test_13_tries.py", "test_implement_trie"),
    "word_search_ii": ("test_13_tries.py", "test_word_search_ii"),
    "add_and_search_word": ("test_13_tries.py", "test_add_and_search_word"),
    "replace_words": ("test_13_tries.py", "test_replace_words"),
    "longest_word": ("test_13_tries.py", "test_longest_word"),
    "map_sum": ("test_13_tries.py", "test_map_sum"),

    # =========================================================================
    # Topic 14: Union-Find
    # =========================================================================
    "implement_union_find": ("test_14_union_find.py", "test_implement_union_find"),
    "num_connected_components": ("test_14_union_find.py", "test_num_connected_components"),
    "redundant_connection": ("test_14_union_find.py", "test_redundant_connection"),
    "accounts_merge": ("test_14_union_find.py", "test_accounts_merge"),
    "longest_consecutive_uf": ("test_14_union_find.py", "test_longest_consecutive_uf"),
    "satisfiability_of_equations": ("test_14_union_find.py", "test_satisfiability_of_equations"),

    # =========================================================================
    # Topic 15: Intervals & Sorting Patterns
    # =========================================================================
    "merge_intervals": ("test_15_intervals.py", "test_merge_intervals"),
    "insert_interval": ("test_15_intervals.py", "test_insert_interval"),
    "meeting_rooms": ("test_15_intervals.py", "test_meeting_rooms"),
    "meeting_rooms_ii": ("test_15_intervals.py", "test_meeting_rooms_ii"),
    "non_overlapping_intervals": ("test_15_intervals.py", "test_non_overlapping_intervals"),
    "minimum_number_of_arrows": ("test_15_intervals.py", "test_minimum_number_of_arrows"),
    "interval_list_intersections": ("test_15_intervals.py", "test_interval_list_intersections"),
}


def get_test_info(func_name: str) -> Optional[Tuple[str, str]]:
    """
    Get the test file and pattern for a function name.

    Returns:
        Tuple of (test_file, test_pattern) or None if not found
    """
    return FUNCTION_REGISTRY.get(func_name)


def register_function(func_name: str, test_file: str, test_pattern: str):
    """Dynamically register a function (useful for custom exercises)."""
    FUNCTION_REGISTRY[func_name] = (test_file, test_pattern)
