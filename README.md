<h1 align="center">
 Leetcode🫡
</h1>

## Table of Contents
1. [Mapping & Arrays](#mapping-&-arrays)
2. [Stack](#stack)
3. [Linked List](#linked-list)
4. [Trees](#trees)
5. [Dynamic Programing](#dynamic-programming)
6. [Binary Search](#binary-search)
7. [Two Pointer](#two-pointer)
8. [Matrix](#matrix)
9. [Sliding Window](#sliding-window)

## Mapping & Arrays
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./easy/TwoSum.py) | Easy | Check for diff and map value to index |
|[Roman To Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](./easy/RomanToInteger.py) [C++](./easy/RomanToInteger.cpp) | Easy | Map Roman to Int | 
|[Remove Element](https://leetcode.com/problems/remove-element/) | [Python](./easy/RemoveElement.py) | Easy | Keep track of num of elements not in nums | 
|[Find the Index of First Occurence in String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Python](./easy/FindIndexOfFirstOccurence.py) | Easy | Slicing | 
|[Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](./easy/SearchInsert.py) | Easy | Loop through and compare | 
|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](./easy/ContainsDuplicate.py) [C++](./easy/ContainsDuplicate.cpp) | Easy | Use set to check | 
|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./easy/ValidAnagram.py) [C++](./easy/ValidAnagram.cpp) | Easy | Map with occurences | 
|[Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./medium/SearchInRotatedSortedArray.py) | Medium | Binary Search with first and second half of array |
|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./medium/ValidSudoku.py) | Medium | Map with R, C, and 3x3 |
|[Group Anagams](https://leetcode.com/problems/group-anagrams/) | [Python](./medium/GroupAnagrams.py) [C++](./medium/GroupAnagrams.cpp) | Medium | Use sorted and hash with list|
|[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](./medium/LongestConsecutiveSequence.py) [C++](./medium/LongestConsecutiveSequence.cpp) | Medium | Keep track of previous index | 
|[Prodcut of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)| [Python](./medium/ProductOfArrayExceptSelf.py) | Medium | create left and right list [1] * len(nums), get product of left and right in nums except [0] and [-1], match index and multiply | 
|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)| [Python](./medium/TopKFrequentElements.py) | Medium | Bubble sort | 


## Stack
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Valid Parenthesses](https://leetcode.com/problems/valid-parentheses/)| [Python](./easy/ValidParentheses.py) [C++](./easy/ValidParenthesses.cpp) | Easy | Pop from stack if valid |
|[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](./medium/EvaluateReversePolishNotation.py) | Medium | Pop 2x and append | 
|[Min Stack](https://leetcode.com/problems/min-stack/) | [Python](./medium/MinStack.py) | Medium | Blank |
|[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)| [Python](./medium/DailyTemperatures.py) | Medium | Create stack of index,value to get duplicate temperatures | 
|[Car Fleet](https://leetcode.com/problems/car-fleet/)| [Python](./medium/CarFleet.py) | Medium | Create list of pos and speed then reverse list to get distance (target - pos)/speed | 


## Linked List
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [Python](./easy/MergeTwoSortedLists.py) | Easy | Traverse and connect head to remaning list1 or list 2 | 
|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)| [Python](./hard/MergeKSortedLists.py) | Hard | Create helper function to merge 2 lists and merge first list with rest |
|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](./easy/ReverseLinkedList.py) | Easy | Keep Track of prev curr and next | 
|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| [Python](./medium/AddTwoNumbers.py) | Medium | Go left to right and keep track of carry |
|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)| [Python](./medium/RemoveNthNodeFromEndOfList.py) | Medium | Create dummy node and 2 pointer |
|[Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)| [Python](./medium/SwapNodesInPairs.py) | Medium | Keep track of curr.next and curr.next.next |
|[Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](./medium/CopyListWithRandomPointer.py) | Medium | Map old node to new node |
|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](./easy/LinkedListCycle.py) | Easy | Use slow and fast pointer to check for overlap |
|[Reorder List](https://leetcode.com/problems/reorder-list/) | [Python](./medium/ReorderList.py) | Medium | Find middle using 2 ptr, reverse list end -> middle, merge | 
|[Remove K from List](https://app.codesignal.com/interview-practice/question/gX7NXPBrYThXZuanm/description) | [Python](./code-signal/removedKFromList.py) | Medium | check for curr.next.next and return head if head.val != k | 
|[Remove Duplicates From Sorted Linked List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [Python](./easy/RemoveDuplicatesFromSortedList.py) | Easy | Keep track of next node and check if curr.next |
|[Convert Sorted Linked List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)| [Python](./medium/ConvertSortedListToBinarySearchTree.py) | Medium | Create list of vals and dfs helper function |


## Trees
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./easy/MaxDepthBinaryTree.py) | Easy | recursive dfs and return 1 + max of left and right subtree |
|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [Python](./easy/InvertTree.py) | Easy | Swap nodes the recurse |
|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](./easy/DiameterBinaryTree.py) | Easy | DFS and check for max(left+right+1,max(left,right)) |
|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](./easy/BalancedBinaryTree.py) | Easy | Create bool variable for ans, dfs and check if max(left,right) - min(left,right) > 1, change ans |

## Dynamic Programming
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Array Max Consective Sum](https://app.codesignal.com/interview-practice/question/dQD4TCunke2JQ98rj/description) | [Python](./code-signal/maxConsecutiveSum2.py) | Medium | Keep track of curr max and global max and use kadones algorithm |


## Binary Search
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](./medium/FindMinimumInRotatedSortedArray.py) | Medium | Set temp ans to top of list and binary search | 
|[Binary Search](https://leetcode.com/problems/binary-search/)| [Python](./medium/BinarySearch.py) | Medium | Update left and right pointers to [(right + left) // 2] +/- 1 | 
|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)| [Python](./medium/KokoEatingBananas.py) | Medium | Binary search and keep track of amount of bannas ate |
|[Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)| [Python](./medium/TimeBasedKey-ValueStore.py) | Medium | Map key to list of lists and binary search(left = 0, right = length of key)) |


## Two Pointer
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](./easy/int_palindrome.py) [C++](./easy/PalindromeNumber.cpp) | Easy | Cast to string and 2 pointer | 
|[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)| [Python](./medium/ContainerMostWater.py) | Medium | Two pointer  |
|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)| [Python](./easy/LongestCommonPrefix.py) | Easy | Create helper function to compare with first string in list |
|[Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./medium/TwoSum2.py) | Medium | Two pointer | 
|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](./hard/TrappingRainWater.py) | Hard | 2 Pointer and keep track of left and right max |


## Matrix
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | [Python](./easy/MatrixDiagonalSum.py) [C++](./easy/MatrixDiagonalSum.cpp) | Easy | Two pointer | 
|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](./medium/SpiralMatrix.py) | Medium | Keep track of L,R,T,B | 
|[Set Matrix Zeros](https://leetcode.com/problems/set-matrix-zeroes/) | [Python](./medium/SetMatrixZeroes.py) | Medium | Create set for rows and cols with zeros | 
|[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](./medium/SearchA2DMatrix.py) | Medium | Binary Search | 
|[Rotate Matrix 90 Degrees](https://app.codesignal.com/interview-practice/question/5A8jwLGcEpTPyyjTB/description) | [Python](./code-signal/rotateImage.py) | Medium | Take transpose then go through range n//2 then swap [i][j], [j][i] <-> [i][n-j], [i][j] | 



## Sliding Window
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./easy/BestTimeBuyStock.py) | Easy | Keep track of highest |
|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](./medium/LongestSubstringWithoutRepeatingCharacters.py) [C++](./medium/LongSubstringWithoutRepeatingCharacters.cpp) | Medium | Slding window |
|[Permutation in String](https://leetcode.com/problems/permutation-in-string/)| [Python](./medium/PermutationInString.py) | Medium | Sliding window | 
|[Find Longest Subarray By Sum](https://app.codesignal.com/interview-practice/question/izLStwkDr5sMS9CEm/description)| [Python](./code-signal/findLongestSubarrayBySum.py) | Medium | increase window size until sum > target then minimize left side of window until > target | 

