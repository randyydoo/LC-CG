<h1 align="center">
 Leetcode🫡
</h1>

## Table of Contents
1. [Mapping & Arrays](#mapping-&-arrays)
2. [Stack](#stack)
3. [Linked List](#linked-list)
4. [Trees](#trees)
5. [Backtracking](#backtracking)
6. [Graphs](#graphs)
7. [Dynamic Programing](#dynamic-programming)
8. [Binary Search](#binary-search)
9. [Two Pointer](#two-pointer)
10. [Matrix](#matrix)
11. [Sliding Window](#sliding-window)

## Mapping & Arrays
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./easy/TwoSum.py) | Easy | Check for diff and map value to index |
|[Roman To Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](./easy/RomanToInteger.py) [C++](./easy/RomanToInteger.cpp) | Easy | Map Roman to Int | 
|[Remove Element](https://leetcode.com/problems/remove-element/) | [Python](./easy/RemoveElement.py) | Easy | Keep track of num of elements not in nums | 
|[ Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | [Python](./easy/DiffOfTwoArrays.py) | Easy | create ans = [[], []] and loop thru nums1 and nums2 | 
|[Find the Index of First Occurence in String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Python](./easy/FindIndexOfFirstOccurence.py) | Easy | Slicing | 
|[Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](./easy/SearchInsert.py) | Easy | Loop through and compare | 
|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](./easy/ContainsDuplicate.py) [C++](./easy/ContainsDuplicate.cpp) | Easy | Use set to check | 
|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./easy/ValidAnagram.py) [C++](./easy/ValidAnagram.cpp) | Easy | Map with occurences | 
|[Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./medium/SearchInRotatedSortedArray.py) | Medium | Binary Search with first and second half of array |
|[Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [Python](./medium/MaxNumberKSumPairs.py) | Medium | Map difference to count and check if num in dict |
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
|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](./easy/ReverseLinkedList.py) | Easy | Keep Track of prev curr and next | 
|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [Python](./easy/MergeTwoSortedLists.py) | Easy | Traverse and connect head to remaning list1 or list 2 | 
|[Remove Duplicates From Sorted Linked List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [Python](./easy/RemoveDuplicatesFromSortedList.py) | Easy | Keep track of next node and check if curr.next |
|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](./easy/LinkedListCycle.py) | Easy | Use slow and fast pointer to check for overlap |
|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| [Python](./medium/AddTwoNumbers.py) | Medium | Go left to right and keep track of carry |
|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)| [Python](./medium/RemoveNthNodeFromEndOfList.py) | Medium | Create dummy node and 2 pointer |
|[Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)| [Python](./medium/SwapNodesInPairs.py) | Medium | Keep track of curr.next and curr.next.next |
|[Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](./medium/CopyListWithRandomPointer.py) | Medium | Map old node to new node |
|[Reorder List](https://leetcode.com/problems/reorder-list/) | [Python](./medium/ReorderList.py) | Medium | Find middle using 2 ptr, reverse list end -> middle, merge | 
|[Remove K from List](https://app.codesignal.com/interview-practice/question/gX7NXPBrYThXZuanm/description) | [Python](./code-signal/removedKFromList.py) | Medium | check for curr.next.next and return head if head.val != k | 
|[Convert Sorted Linked List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)| [Python](./medium/ConvertSortedListToBinarySearchTree.py) | Medium | Create list of vals and dfs helper function |
|[Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)| [Python](./medium/SplitLinkedListInParts.py) | Medium | Get length of list and append to ans when part size hit |
|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)| [Python](./hard/MergeKSortedLists.py) | Hard | Create helper function to merge 2 lists and merge first list with rest |

## Trees
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Bianry Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [Python](./easy/BinaryTreePaths.py) | Easy | DFS and checkk if not root.left and not root.right | 
|[Mode in BST](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | [Python](./easy/ModeBST.py) | Easy | DFS and map frequency | 
|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./easy/MaxDepthBinaryTree.py) | Easy | recursive dfs and return 1 + max of left and right subtree |
|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [Python](./easy/InvertTree.py) | Easy | Swap nodes the recurse |
|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](./easy/DiameterBinaryTree.py) | Easy | DFS and check for max(left+right+1,max(left,right)) |
|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](./easy/BalancedBinaryTree.py) | Easy | Create bool variable for ans, dfs and check if max(left,right) - min(left,right) > 1, change ans |
|[Same Tree](https://leetcode.com/problems/same-tree/) | [Python](./easy/SameTree.py) | Easy | dfs and append to 2 lists |
|[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | [Python](./easy/SubtreeofAnotherTree.py) | Easy | dfs until root.val == subRoot.val and use helper function for same tree |
|[Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](./medium/LowestCommonAncestorBST.py) | Medium | DFS until split (root > p.val and root <  q.val (vise versa)) |
|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](./medium/BinaryTreeLevelOrderTraversal.py) | Medium | BFS |
|[Maximum Level Sum of Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | [Python](./medium/MaxLevelSumBinaryTree.py) | Easy | DFS and checkk if not root.left and not root.right | 
|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](./medium/ValidateBST.py) | Medium | DFS and keep track of curr min and max |
|[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](./medium/BinaryTreeRightSideView.py) | Medium | Create left and right deque and append from end of deque |
|[Count Good Noes in Binary Tree ](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Python](./medium/CountGoodNodesinBinaryTree.py) | Medium | DFS and keep track of curr max |
|[Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Python](./medium/KthSmallestBST.py) | Medium | DFS to append to list and use sorted OR in order DFS and decrement k |
|[Binary Tree Maximum Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Python](./hard/MaxPathSumBinaryTree.py) | Hard | DFS and compare left and right recursive calls with max(0,left or right) to get edge case of root itself being max |


## Backtracking
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Subsets](https://leetcode.com/problems/subsets/) | [Python](./medium/subsets.py) | Medium | DFS use stack to take care of 'dont include' descison | 
|[Combination Sum](https://leetcode.com/problems/combination-sum/) | [Python](./medium/CombinationSum.py) | Medium | DFS until index > lenth or sum(stack) == target or sum(stack) > target |
|[ Word Search ](https://leetcode.com/problems/word-search/) | [Python](./medium/WordSearch.py) | Medium | DFS and keep track of visited and replace board with original values once depth reached |




## Graphs
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./medium/NumberOfIslands.py) | Medium | DFS and change '1' to random char | 

## Dynamic Programming
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Array Max Consective Sum](https://app.codesignal.com/interview-practice/question/dQD4TCunke2JQ98rj/description) | [Python](./code-signal/maxConsecutiveSum2.py) | Medium | Keep track of curr max and global max and use kadones algorithm |


## Binary Search
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Binary Search](https://leetcode.com/problems/binary-search/)| [Python](./easy/BinarySearch.py) | Easy | Create left,right, and middle pointer | 
|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](./medium/FindMinimumInRotatedSortedArray.py) | Medium | Set temp ans to top of list and binary search | 
|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)| [Python](./medium/KokoEatingBananas.py) | Medium | Binary search and keep track of amount of bannas ate |
|[Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)| [Python](./medium/TimeBasedKey-ValueStore.py) | Medium | Map key to list of lists and binary search(left = 0, right = length of key)) |


## Two Pointer
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](./easy/int_palindrome.py) [C++](./easy/PalindromeNumber.cpp) | Easy | Cast to string and 2 pointer | 
|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)| [Python](./easy/LongestCommonPrefix.py) | Easy | Create helper function to compare with first string in list |
|[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)| [Python](./medium/ContainerMostWater.py) | Medium | Two pointer  |
|[Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./medium/TwoSum2.py) | Medium | Two pointer | 
|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](./hard/TrappingRainWater.py) | Hard | 2 Pointer and keep track of left and right max |


## Matrix
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | [Python](./easy/MatrixDiagonalSum.py) [C++](./easy/MatrixDiagonalSum.cpp) | Easy | Two pointer | 
|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./medium/ValidSudoku.py) | Medium | Map with R, C, and 3x3 |
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

