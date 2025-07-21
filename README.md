# dsa

A collection of Python solutions and notes for common Data Structures and Algorithms problems.

## Overview

This repository is for my personal practice of DSA and serves as a log and notes of my learning sessions. Here, I document solutions, explanations, and code for various DSA problems, using Python. Many problems are inspired by coding platforms such as GeeksforGeeks and LeetCode.

## Structure

The repository is organized into directories by topic:

- **`arrays/`** – Array problems, divided by difficulty:
  - `easy/` – Basic array operations and simple algorithms
  - `medium/` – Intermediate problems like matrix operations and optimization
  - `hard/` – Complex problems like 3Sum and 4Sum
- **`sorting/`** – Sorting algorithm implementations
- **`binary-search/`** – Binary search variations and applications
- **`hashing/`** – Hash table and frequency-based problems
- **`linked-list/`** – Linked list operations and algorithms
- **`strings/`** – String manipulation and pattern problems
- **`recursion/`** – Recursive problem solutions
- **`basic-maths/`** – Mathematical algorithms and number theory

Each Python file typically contains a class `Solution` with methods solving the respective problem, references to the original problem statement, and comments on time and space complexity.

## Implemented Problems

### Sorting Algorithms
- [Bubble Sort](sorting/bubble-sort) – Basic comparison-based sorting
- [Selection Sort](sorting/selection-sort.py) – Find minimum and swap approach
- [Insertion Sort](sorting/insertion-sort.py) – Build sorted array incrementally
- [Merge Sort](sorting/merge-sort.py) – Divide and conquer approach (in-place and new array versions)
- [Quick Sort (Lomuto)](sorting/quick-sort-lomuto-scheme—pivot-at-end.py) – Partition with pivot at end
- [Quick Sort (Hoare)](sorting/quick-sort-hoare-partition-scheme—pivot-at-start.py) – Efficient partition scheme

### Array Problems

#### Easy
- [Check if Array is Sorted](arrays/easy/check-if-an-array-is-sorted.py)
- [Largest Element in Array](arrays/easy/largest-element-in-array.py)
- [Second Order Elements](arrays/easy/second-order-elements.py)
- [Remove Duplicates from Sorted Array](arrays/easy/remove-duplicates-from-sorted-array.py)
- [Rotate Array](arrays/easy/rotate-array.py)
- [Move Zeroes](arrays/easy/move-zeroes.py)
- [Max Consecutive Ones](arrays/easy/max-consecutive-ones.py)
- [Missing Number](arrays/easy/missing-number.py)
- [Search Element in Array](arrays/easy/search-an-element-in-an-array.py)
- [Union of Two Sorted Arrays](arrays/easy/union-of-two-sorted-arrays.py)

#### Medium
- [Two Sum](arrays/medium/two-sum.py)
- [Best Time to Buy and Sell Stock](arrays/medium/best-time-to-buy-and-sell-stock.py)
- [Rearrange Array Elements by Sign](arrays/medium/rearrange-array-elements-by-sign.py)
- [Maximum Subarray (Kadane's Algorithm)](arrays/medium/maximum-subarray-kadane-algorithm.py)
- [Longest Consecutive Sequence](arrays/medium/longest-consecutive-sequence.py)
- [Spiral Matrix](arrays/medium/spiral-matrix.py)
- [Rotate Image (Matrix)](arrays/medium/rotate-image.py)
- [Set Matrix Zeroes](arrays/medium/set-matrix-zeroes.py)
- [Find K-Distant Indices](arrays/medium/find-all-k-distant-indices-in-an-array.py)

#### Hard
- [3Sum](arrays/hard/3sum.py) – Multiple approaches with complexity analysis
- [4Sum](arrays/hard/4sum.py) – Two-pointer and hashing solutions

### Binary Search
- [Binary Search (Iterative)](binary-search/binary-search-iterative.py)
- [Binary Search (Recursive)](binary-search/binary-search-recursive.py)
- [Search Insert Position](binary-search/search-insert-position.py)
- [Find First and Last Position](binary-search/find-first-and-last-position-of-element-in-sorted-array.py)
- [Search in Rotated Sorted Array](binary-search/search-in-rotated-sorted-array.py)
- [Search in Rotated Sorted Array II](binary-search/search-in-rotated-sorted-array-ii.py)
- [Find Minimum in Rotated Sorted Array](binary-search/find-minimum-in-rotated-sorted-array.py)
- [Number of Occurrences](binary-search/number-of-occurrence.py)
- [Floor in Sorted Array](binary-search/floor-in-a-sorted-array.py)
- [Ceiling and Floor](binary-search/ceiling-floor-in-a-sorted-array.py)
- [Upper Bound Implementation](binary-search/implement-upper-bound.py)

### Hashing Problems
- [Frequency of Array Elements](hashing/frequency-of-array-elements.py)
- [Find Frequency of Element](hashing/find-the-frequency.py)
- [Find Lucky Integer in Array](hashing/find-lucky-integer-in-an-array.py) – Find integer equal to its frequency
- [Finding Pairs with Certain Sum](arrays/hard/finding-pairs-with-a-certain-sum.py) – Dynamic pair counting with updates

### Recursion
- [Print 1 to N without Loops](recursion/print-1-to-n-without-using-loops.py)
- [Print N to 1 without Loop](recursion/print-n-to-1-without-loop.py)
- [Print GFG N Times](recursion/print-gfg-n-times.py)
- [Fibonacci Number](recursion/fibonacci-number.py)
- [Factorial Numbers ≤ N](recursion/find-all-factorial-numbers-less-than-or-equal-to-n.py)
- [Sum of Cube of First N Terms](recursion/sum-of-cube-of-first-n-terms)
- [Palindrome String (Recursive)](recursion/palindrome-string.py)
- [Reverse Sub-array](recursion/reverse-sub-array.py)

### Basic Mathematics
- [Count Digits](basic-maths/number-of-digits.py)
- [Palindrome Number](basic-maths/palindrome-number.py)
- [Reverse Integer](basic-maths/reverse-integer.py)
- [LCM and GCD](basic-maths/lcm-and-gcd.py)

### String Problems
- [Valid Anagram](strings/valid-anagram.py) – Check if two strings are anagrams using frequency counting
- [Group Anagrams](strings/group-anagrams.py) – Group strings that are anagrams of each other
- [Find the K-th Character in String Game I](strings/find-the-k-th-character-in-string-game-i.py) – String transformation game problem

### Linked List Problems
- [Introduction to Linked List](linked-list/introduction-to-linked-list.py) – Basic linked list construction
- [Design Linked List](linked-list/design-linked-list.py) – Complete linked list implementation with all operations
- [Count Nodes of Linked List](linked-list/count-nodes-of-linked-list.py) – Count total nodes in a linked list
- [Search in Linked List](linked-list/search-in-linked-list.py) – Search for an element in linked list
- [Linked List Insertion](linked-list/linked-list-insertion.py) – Insert at end of linked list
- [Reverse Linked List](linked-list/reverse-linked-list.py) – Reverse a singly linked list
- [Delete Node without Head](linked-list/delete-node-in-a-linked-list-no-head-special-case.py) – Special case deletion
- [Odd Even Linked List](linked-list/odd-even-linked-list.py) – Rearrange nodes by position parity

#### Tortoise-Hare Algorithm Problems
- [Linked List Cycle](linked-list/tortoise-hare-linked-list-cycle.py) – Detect cycle using Floyd's algorithm
- [Linked List Cycle II](linked-list/tortoise-hare-linked-list-cycle-ii.py) – Find cycle start node
- [Find Length of Loop](linked-list/tortoise-hare-find-length-of-loop.py) – Count nodes in cycle
- [Middle of Linked List](linked-list/tortoise-hare-middle-of-the-linked-list.py) – Find middle node efficiently
- [Remove Nth Node from End](linked-list/tortoise-hare-remove-nth-node-from-end-of-list.py) – Remove node from end

## Pattern Wise Questions

<details>
<summary><strong>Click to expand pattern-wise problem categorization</strong></summary>

### 1. Two Pointers
- **Easy**: [Remove Duplicates from Sorted Array](arrays/easy/remove-duplicates-from-sorted-array.py), [Move Zeroes](arrays/easy/move-zeroes.py)
- **Medium**: [Rearrange Array Elements by Sign](arrays/medium/rearrange-array-elements-by-sign.py)
- **Hard**: [3Sum](arrays/hard/3sum.py), [4Sum](arrays/hard/4sum.py)
- **Utility**: [Union of Two Sorted Arrays](arrays/easy/union-of-two-sorted-arrays.py)

### 2. Binary Search
- **Basic**: [Binary Search (Iterative)](binary-search/binary-search-iterative.py), [Binary Search (Recursive)](binary-search/binary-search-recursive.py)
- **Bounds**: [Search Insert Position](binary-search/search-insert-position.py), [Upper Bound Implementation](binary-search/implement-upper-bound.py), [Floor in Sorted Array](binary-search/floor-in-a-sorted-array.py), [Ceiling and Floor](binary-search/ceiling-floor-in-a-sorted-array.py)
- **Range Queries**: [Find First and Last Position](binary-search/find-first-and-last-position-of-element-in-sorted-array.py), [Number of Occurrences](binary-search/number-of-occurrence.py)
- **Rotated Arrays**: [Search in Rotated Sorted Array](binary-search/search-in-rotated-sorted-array.py), [Search in Rotated Sorted Array II](binary-search/search-in-rotated-sorted-array-ii.py), [Find Minimum in Rotated Sorted Array](binary-search/find-minimum-in-rotated-sorted-array.py)

### 3. Hashing/Hash Maps
- **Frequency Counting**: [Valid Anagram](strings/valid-anagram.py), [Frequency of Array Elements](hashing/frequency-of-array-elements.py), [Find Frequency of Element](hashing/find-the-frequency.py)
- **Complement Lookup**: [Two Sum](arrays/medium/two-sum.py), [3Sum](arrays/hard/3sum.py) (hashing approach), [4Sum](arrays/hard/4sum.py) (hashing approach)
- **Sequence Problems**: [Longest Consecutive Sequence](arrays/medium/longest-consecutive-sequence.py), [Missing Number](arrays/easy/missing-number.py)

### 4. Greedy Algorithms
- **Optimization**: [Best Time to Buy and Sell Stock](arrays/medium/best-time-to-buy-and-sell-stock.py), [Maximum Subarray (Kadane's Algorithm)](arrays/medium/maximum-subarray-kadane-algorithm.py)
- **Counting**: [Max Consecutive Ones](arrays/easy/max-consecutive-ones.py)

### 5. Matrix Manipulation
- **Traversal**: [Spiral Matrix](arrays/medium/spiral-matrix.py)
- **Transformation**: [Rotate Image](arrays/medium/rotate-image.py), [Set Matrix Zeroes](arrays/medium/set-matrix-zeroes.py)

### 6. Divide and Conquer
- **Sorting**: [Merge Sort](sorting/merge-sort.py), [Quick Sort (Lomuto)](sorting/quick-sort-lomuto-scheme—pivot-at-end.py), [Quick Sort (Hoare)](sorting/quick-sort-hoare-partition-scheme—pivot-at-start.py)

### 7. Basic Recursion
- **Mathematical**: [Fibonacci Number](recursion/fibonacci-number.py), [Factorial Numbers ≤ N](recursion/find-all-factorial-numbers-less-than-or-equal-to-n.py), [Sum of Cube of First N Terms](recursion/sum-of-cube-of-first-n-terms)
- **String/Array**: [Palindrome String (Recursive)](recursion/palindrome-string.py), [Reverse Sub-array](recursion/reverse-sub-array.py)
- **Print Patterns**: [Print 1 to N without Loops](recursion/print-1-to-n-without-using-loops.py), [Print N to 1 without Loop](recursion/print-n-to-1-without-loop.py), [Print GFG N Times](recursion/print-gfg-n-times.py)

### 8. Mathematical Patterns
- **Number Theory**: [LCM and GCD](basic-maths/lcm-and-gcd.py), [Count Digits](basic-maths/number-of-digits.py)
- **Digit Manipulation**: [Palindrome Number](basic-maths/palindrome-number.py), [Reverse Integer](basic-maths/reverse-integer.py)

### 9. Array Rearrangement
- **In-place Operations**: [Rotate Array](arrays/easy/rotate-array.py), [Rearrange Array Elements by Sign](arrays/medium/rearrange-array-elements-by-sign.py)

### 10. Sorting Algorithms
- **Comparison-based**: [Bubble Sort](sorting/bubble-sort), [Selection Sort](sorting/selection-sort.py), [Insertion Sort](sorting/insertion-sort.py)
- **Advanced**: [Merge Sort](sorting/merge-sort.py), [Quick Sort variants](sorting/)

### 11. Linear Scan Patterns
- **Single Pass**: [Largest Element in Array](arrays/easy/largest-element-in-array.py), [Second Order Elements](arrays/easy/second-order-elements.py), [Check if Array is Sorted](arrays/easy/check-if-an-array-is-sorted.py)
- **Search**: [Search Element in Array](arrays/easy/search-an-element-in-an-array.py)

### 12. Range-based Problems
- **Distance Calculations**: [Find K-Distant Indices](arrays/medium/find-all-k-distant-indices-in-an-array.py)

### 13. Linked List Patterns
- **Basic Operations**: [Introduction to Linked List](linked-list/introduction-to-linked-list.py), [Linked List Insertion](linked-list/linked-list-insertion.py), [Count Nodes](linked-list/count-nodes-of-linked-list.py)
- **Search & Manipulation**: [Search in Linked List](linked-list/search-in-linked-list.py), [Reverse Linked List](linked-list/reverse-linked-list.py), [Odd Even Linked List](linked-list/odd-even-linked-list.py)
- **Tortoise-Hare**: [Linked List Cycle](linked-list/tortoise-hare-linked-list-cycle.py), [Find Middle](linked-list/tortoise-hare-middle-of-the-linked-list.py), [Remove Nth from End](linked-list/tortoise-hare-remove-nth-node-from-end-of-list.py)
- **Advanced**: [Design Linked List](linked-list/design-linked-list.py), [Delete Node Special Case](linked-list/delete-node-in-a-linked-list-no-head-special-case.py)

### 14. String Processing
- **Anagram Problems**: [Valid Anagram](strings/valid-anagram.py), [Group Anagrams](strings/group-anagrams.py)
- **Character Manipulation**: [Find K-th Character in String Game](strings/find-the-k-th-character-in-string-game-i.py)

### 15. Dynamic Data Structures
- **Real-time Updates**: [Finding Pairs with Certain Sum](arrays/hard/finding-pairs-with-a-certain-sum.py)

</details>

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/anujjainbatu/dsa.git
   ```
2. Navigate to the desired directory and open the Python file for the problem you're interested in.
3. Each file contains a `Solution` class you can import and use, or run directly for experimentation and learning.

## Features

- **Comprehensive Coverage**: Problems spanning from basic to advanced difficulty levels
- **Multiple Approaches**: Many problems include different solution methods with complexity analysis
- **Well-Documented**: Each solution includes problem links, time/space complexity, and explanatory comments
- **Organized Structure**: Clear categorization by topic and difficulty for easy navigation

## Purpose

- Practice DSA coding problems systematically
- Log and track my progress and different approaches
- Maintain notes and explanations for future reference
- Build a comprehensive problem-solving toolkit

## Contributing

This repository is primarily for my own learning, but feel free to fork the repo and submit pull requests for new problems, improved solutions, or optimizations. 

---

> **Owner:** [anujjainbatu](https://github.com/anujjainbatu)
