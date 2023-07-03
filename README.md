# LeetCode Problems

This repository contains my solutions to various LeetCode problems, organized by data structures and algorithms.

## Table of Contents
- [Arrays](#arrays)
- [Linked Lists](#linked-lists)

## Arrays

| #   | Stack                                           | Solution                                                      | Difficulty | Hint                                  |
| --- | ----------------------------------------------- | ------------------------------------------------------------- | ---------- | ------------------------------------- |
| 20  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)       | [Python](./easy/ValidParentheses.py), [C++](./easy/ValidParentheses.cpp)  | Easy       | Check prev and pop 2x                  |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](./medium/EvaluateReversePolishNotation.py)                   | Medium     | Pop 2x and append                     |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | [Python](./medium/MinStack.py)                                      | Medium     | Blank                                 |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [Python](./medium/DailyTemperatures.py)                            | Medium     | Create stack of index, value to get duplicate temperatures |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | [Python](./medium/CarFleet.py)                                      | Medium     | Create list of pos and speed, then reverse list to get distance (target - pos) / speed |

## Linked Lists

| #   | Linked List                                     | Solution                                                      | Difficulty | Hint                                  |
| --- | ----------------------------------------------- | ------------------------------------------------------------- | ---------- | ------------------------------------- |
| 21  | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](./easy/MergeTwoSortedLists.py)                           | Easy       | Traverse and connect head to remaining list1 or list2 |
| 33  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)       | [Python](./easy/ReverseLinkedList.py)                             | Easy       | Keep track of prev, curr, and next    |
