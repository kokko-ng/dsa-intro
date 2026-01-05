# DSA Intro

A comprehensive Data Structures & Algorithms learning curriculum with interactive Jupyter notebooks and automated testing.

## Overview

This repository provides a structured, self-paced learning platform for mastering fundamental computer science concepts. Each topic includes theoretical explanations, visual examples, and hands-on coding exercises with immediate feedback through an automated testing system.

## Features

- **15 comprehensive topics** covering essential DSA concepts
- **100+ coding exercises** with progressive difficulty
- **Automated testing** with the `check()` function for instant feedback
- **Interactive Jupyter notebooks** combining theory and practice
- **Categorized tests** (basic, edge cases, performance)
- **Helper data structures** for linked lists, trees, and graphs

## Topics Covered

| # | Topic | Key Concepts |
|---|-------|--------------|
| 01 | Big O Notation | Complexity analysis, growth rates |
| 02 | Arrays & Strings | Two-sum, Kadane's algorithm, palindromes |
| 03 | Hash Tables | Frequency maps, group anagrams, longest consecutive |
| 04 | Two Pointers & Sliding Window | Container problems, subarray sums |
| 05 | Linked Lists | Reversal, cycle detection, merge operations |
| 06 | Stacks & Queues | Parentheses matching, monotonic stacks |
| 07 | Recursion & Backtracking | Subsets, permutations, N-queens |
| 08 | Trees | Traversals, BST validation, LCA |
| 09 | Heaps & Priority Queues | Kth largest, merge K lists |
| 10 | Graphs | BFS/DFS, topological sort, shortest paths |
| 11 | Dynamic Programming | Climbing stairs, coin change, edit distance |
| 12 | Greedy Algorithms | Jump game, interval scheduling |
| 13 | Tries | Prefix trees, word search |
| 14 | Union-Find | Disjoint sets, connected components |
| 15 | Intervals & Sorting | Interval merging, meeting rooms |

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd dsa-intro
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

4. Open any notebook from the `notebooks/` directory to begin learning.

## Usage

### Working Through Notebooks

Each notebook follows a consistent structure:
1. **Learning objectives** for the topic
2. **Conceptual explanations** with examples
3. **Complexity analysis** for each algorithm
4. **Coding exercises** to implement

### Validating Your Solutions

After implementing a function, use the `check()` function to validate your solution:

```python
from dsa_checker import check

def two_sum(nums, target):
    # Your implementation here
    pass

check(two_sum)
```

The checker will run your solution against hidden test cases and display:
- Pass/fail status for each test category
- Visual feedback in the notebook
- Hints about which test types are failing (basic, edge, or performance)

## Project Structure

```
dsa-intro/
├── notebooks/           # 15 Jupyter notebooks with exercises
├── tests/               # Test files for all exercises
├── data_structures/     # Helper classes (ListNode, TreeNode, GraphNode)
├── dsa_checker/         # Automated testing framework
├── requirements.txt     # Python dependencies
└── pyproject.toml       # Project configuration
```

## Data Structures

The `data_structures` module provides helper classes for working with common structures:

```python
from data_structures import ListNode, create_linked_list, linked_list_to_list
from data_structures import TreeNode, build_tree, tree_to_list
from data_structures import GraphNode, build_graph_from_edges
```

## Requirements

- jupyter >= 1.0.0
- notebook >= 7.0.0
- ipykernel >= 6.0.0
- ipython >= 8.0.0
