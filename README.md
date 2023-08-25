<h1 align="center">
 Leetcode🫡
</h1>

## Table of Contents
1. [Mapping & Arrays](#mapping-&-arrays)
2. [Stack](#stack)
3. [Linked List](#linked-list)
4. [Trees](#trees)
5. [Binary Search](#binary-search)
6. [Two Pointer](#two-pointer)
7. [Matrix](#matrix)
8. [Sliding Window](#sliding-window)

## Mapping & Arrays
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|1|[Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./easy/TwoSum.py) | Easy | Check for diff and map value to index |
|13|[Roman To Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](./easy/RomanToInteger.py) [C++](./easy/RomanToInteger.cpp) | Easy | Map Roman to Int | 
|27|[Remove Element](https://leetcode.com/problems/remove-element/) | [Python](./easy/RemoveElement.py) | Easy | Keep track of num of elements not in nums | 
|28|[Find the Index of First Occurence in String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Python](./easy/FindIndexOfFirstOccurence.py) | Easy | Slicing | 
|35|[Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](./easy/SearchInsert.py) | Easy | Loop through and compare | 
|217|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](./easy/ContainsDuplicate.py) [C++](./easy/ContainsDuplicate.cpp) | Easy | Use set to check | 
|242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./easy/ValidAnagram.py) [C++](./easy/ValidAnagram.cpp) | Easy | Map with occurences | 
|33|[Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./medium/SearchInRotatedSortedArray.py) | Medium | Binary Search with first and second half of array |
|36|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./medium/ValidSudoku.py) | Medium | Map with R, C, and 3x3 |
|49|[Group Anagams](https://leetcode.com/problems/group-anagrams/) | [Python](./medium/GroupAnagrams.py) [C++](./medium/GroupAnagrams.cpp) | Medium | Use sorted and hash with list|
|128|[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](./medium/LongestConsecutiveSequence.py) [C++](./medium/LongestConsecutiveSequence.cpp) | Medium | Keep track of previous index | 
|238|[Prodcut of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)| [Python](./medium/ProductOfArrayExceptSelf.py) | Medium | Get product of left and right array and match index | 
|347|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)| [Python](./medium/TopKFrequentElements.py) | Medium | Bubble sort | 


## Stack
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|20|[Valid Parenthesses](https://leetcode.com/problems/valid-parentheses/)| [Python](./easy/ValidParentheses.py) [C++](./easy/ValidParenthesses.cpp) | Easy | Pop from stack if valid |
|150|[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](./medium/EvaluateReversePolishNotation.py) | Medium | Pop 2x and append | 
|155|[Min Stack](https://leetcode.com/problems/min-stack/) | [Python](./medium/MinStack.py) | Medium | Blank |
|739|[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)| [Python](./medium/DailyTemperatures.py) | Medium | Create stack of index,value to get duplicate temperatures | 
|853|[Car Fleet](https://leetcode.com/problems/car-fleet/)| [Python](./medium/CarFleet.py) | Medium | Create list of pos and speed then reverse list to get distance (target - pos)/speed | 


## Linked List
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|21|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [Python](./easy/MergeTwoSortedLists.py) | Easy | Traverse and connect head to remaning list1 or list 2 | 
|23|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)| [Python](./hard/MergeKSortedLists.py) | Hard | Create helper function to merge 2 lists and merge first list with rest |
|33|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](./easy/ReverseLinkedList.py) | Easy | Keep Track of prev curr and next | 
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| [Python](./medium/AddTwoNumbers.py) | Medium | Go left to right and keep track of carry |
|19|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)| [Python](./medium/RemoveNthNodeFromEndOfList.py) | Medium | Create dummy node and 2 pointer |
|24|[Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)| [Python](./medium/SwapNodesInPairs.py) | Medium | Keep track of curr.next and curr.next.next |
|138|[Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](./medium/CopyListWithRandomPointer.py) | Medium | Map old node to new node |
|141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](./easy/LinkedListCycle.py) | Easy | Use slow and fast pointer to check for overlap |
|143|[Reorder List](https://leetcode.com/problems/reorder-list/) | [Python](./medium/ReorderList.py) | Medium | Find middle using 2 ptr, reverse list end -> middle, merge | 

## Trees
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./easy/MaxDepthBinaryTree.py) | Easy | Iteraive BFS with stack |
|226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [Python](./easy/InvertTree.py) | Easy | Swap nodes the recurse |
|543|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](./easy/DiameterBinaryTree.py) | Easy | DFS and check for max(left+right+1,max(left,right)) |


## Binary Search
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|153|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](./medium/FindMinimumInRotatedSortedArray.py) | Medium | Set temp ans to top of list and binary search | 
|704|[Binary Search](https://leetcode.com/problems/binary-search/)| [Python](./medium/BinarySearch.py) | Medium | Keep start and end pointers | 
|875|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)| [Python](./medium/KokoEatingBananas.py) | Medium | Binary search and keep track of amount of bannas ate |
|981|[Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)| [Python](./medium/TimeBasedKey-ValueStore.py) | Medium | Map key to list of lists and binary search(left = 0, right = length of key)) |


## Two Pointer
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|9|[Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](./easy/int_palindrome.py) [C++](./easy/PalindromeNumber.cpp) | Easy | Cast to string and 2 pointer | 
|11|[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)| [Python](./medium/ContainerMostWater.py) | Medium | Two pointer  |
|14|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)| [Python](./easy/LongestCommonPrefix.py) | Easy | Create helper function to compare with first string in list |
|167|[Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./medium/TwoSum2.py) | Medium | Two pointer | 
|42|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](./hard/TrappingRainWater.py) | Hard | 2 Pointer and keep track of left and right max |


## Matrix
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|1572|[Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | [Python](./easy/MatrixDiagonalSum.py) [C++](./easy/MatrixDiagonalSum.cpp) | Easy | Two pointer | 
|54|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](./medium/SpiralMatrix.py) | Medium | Keep track of L,R,T,B | 
|73|[Set Matrix Zeros](https://leetcode.com/problems/set-matrix-zeroes/) | [Python](./medium/SetMatrixZeroes.py) | Medium | Create set for rows and cols with zeros | 
|74|[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](./medium/SearchA2DMatrix.py) | Medium | Binary Search | 


## Sliding Window
| # | Problem | Solution | Difficulty | Hint |
|---| ------- | -------- | ---------- | ------------ |
|121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./easy/BestTimeBuyStock.py) | Easy | Keep track of highest |
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](./medium/LongestSubstringWithoutRepeatingCharacters.py) [C++](./medium/LongSubstringWithoutRepeatingCharacters.cpp) | Medium | Slding window |
|567|[Permutation in String](https://leetcode.com/problems/permutation-in-string/)| [Python](./medium/PermutationInString.py) | Medium | Sliding window | 
