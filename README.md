<h1 align="center">
 Leetcode🫡
</h1>

## Table of Contents
1. [Mapping & Arrays](#mapping-&-arrays)
2. [Stack](#stack)
3. [Two Pointer](#two-pointer)
4. [Binary Search](#binary-search)
5. [Matrix](#matrix)
6. [Sliding Window](#sliding-window)
7. [Linked List](#linked-list)
8. [Trees](#trees)
9. [Tries](#tries)
10. [Heap & Priority Queue](#heap--priority-queue)
11. [Backtracking](#backtracking)
12. [Graphs](#graphs)
13. [Dynamic Programing](#dynamic-programming)

## Mapping & Arrays
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./easy/TwoSum.py) | Easy | Check for diff and map value to index |
|[Roman To Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](./easy/RomanToInteger.py) [C++](./easy/RomanToInteger.cpp) | Easy | Map Roman to Int | 
|[Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) | [Python](./easy/WordCount.py) | Easy | Freq Count | 
|[Remove Element](https://leetcode.com/problems/remove-element/) | [Python](./easy/RemoveElement.py) | Easy | Keep track of num of elements not in nums | 
|[Pascal Triangle](https://leetcode.com/problems/pascals-triangle/) | [Python](./easy/PasTriangle.py) | Easy | Check prev values to find curr |
|[Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | [Python](./easy/UniqueEmailAddresses.py) | Easy | Use set | 
|[ Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | [Python](./easy/DiffOfTwoArrays.py) | Easy | create ans = [[], []] and loop thru nums1 and nums2 | 
|[Find the Index of First Occurence in String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Python](./easy/FindIndexOfFirstOccurence.py) | Easy | Slicing | 
|[Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](./easy/SearchInsert.py) | Easy | Loop through and compare | 
|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](./easy/ContainsDuplicate.py) [C++](./easy/ContainsDuplicate.cpp) | Easy | Use set to check | 
|[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | [Python](./easy/ContainsDuplicate2.py) | Easy | Map mp[num]: i |
|[Happy Number](https://leetcode.com/problems/happy-number/) | [Python](./easy/HappyNumber.py) | Easy | Keep track of visited numbers |
|[Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | [Python](./easy/IsoStrings.py) | Easy | Map curr s_char with t_char and keep track of used t_chars |
|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./easy/ValidAnagram.py) [C++](./easy/ValidAnagram.cpp) | Easy | Map with occurences | 
|[Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](./easy/ZigzagConv.py) | Medium | Create list of empty strings size of rows -> check if index at end of list | 
|[Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./medium/SearchInRotatedSortedArray.py) | Medium | Binary Search with first and second half of array |
|[Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [Python](./medium/MaxNumberKSumPairs.py) | Medium | Map difference to count and check if num in dict |
|[Group Anagams](https://leetcode.com/problems/group-anagrams/) | [Python](./medium/GroupAnagrams.py) [C++](./medium/GroupAnagrams.cpp) | Medium | Use sorted and hash with list|
|[Minimum Number of Frogs Croaking](https://leetcode.com/problems/minimum-number-of-frogs-croaking/) | [Python](./medium/MinFrogs.py) | Medium | Update new frog when arrive at 'c' -> map char with count |
|[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](./medium/LongestConsecutiveSequence.py) [C++](./medium/LongestConsecutiveSequence.cpp) | Medium | Keep track of previous index | 
|[Prodcut of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)| [Python](./medium/ProductOfArrayExceptSelf.py) | Medium | create left and right list [1] * len(nums), get product of left and right in nums except [0] and [-1], match index and multiply | 
|[Divide Array Into Arrays With Max Difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/)| [Python](./medium/DivArray.py) | Medium | One pass |
|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)| [Python](./medium/TopKFrequentElements.py) | Medium | Bubble sort | 
|[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)| [Python](./medium/LongestConsecutiveSeq.py) | Medium | Convert nums to a set and check if start of sequence -> end of sequence | 
|[Find the Winner of an Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game/)| [Python](./medium/WinnerofArray.py) | Medium | Compare 0th index continuously |
|[Last Moment Before All Ants Fall Out of a Plank](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/) | [Python](./medium/LastAnt.py) | Medium | Find max ant from falling |
|[Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) | [Python](./medium/Garbage.py) | Medium | Calculate (total time cost) + (trash count) |
|[Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/) | [Python](./medium/NicePairs.py) | Medium | Map num-rev : count |
|[Candy](https://leetcode.com/problems/candy/) | [Python](./hard/Candy.py) | Hard | Two pass and map index: candy_ct  |



## Stack
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Valid Parenthesses](https://leetcode.com/problems/valid-parentheses/)| [Python](./easy/ValidParentheses.py) [C++](./easy/ValidParenthesses.cpp) | Easy | Pop from stack if valid |
|[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](./medium/EvaluateReversePolishNotation.py) | Medium | Pop 2x and append | 
|[Min Stack](https://leetcode.com/problems/min-stack/) | [Python](./medium/MinStack.py) | Medium | Append and tuple and compare with top of stack |
|[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)| [Python](./medium/DailyTemperatures.py) | Medium | Use stack and append with (val, index) then sliding window |
|[Car Fleet](https://leetcode.com/problems/car-fleet/)| [Python](./medium/CarFleet.py) | Medium | Create list of pos and speed then reverse list to get distance (target - pos)/speed | 
|[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)| [Python](./medium/Insert1.py) | Medium | Swap with top of stack and map {val: index} |

## Two Pointer
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](./easy/int_palindrome.py) [C++](./easy/PalindromeNumber.cpp) | Easy | Cast to string and 2 pointer | 
|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)| [Python](./easy/LongestCommonPrefix.py) | Easy | Create helper function to compare with first string in list |
|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)| [Python](./easy/RemoveDuplicatedFromSortedArray.py) | Easy | Recursion or 2 pointer |
|[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)| [Python](./medium/ContainerMostWater.py) | Medium | Two pointer  |
|[Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./medium/TwoSum2.py) | Medium | Two pointer | 
|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [Python](./medium/RemoveDupArray2.py) | Medium | Replace duplicate with long int|
|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](./hard/TrappingRainWater.py) | Hard | 2 Pointer and keep track of left and right max |

## Binary Search
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Binary Search](https://leetcode.com/problems/binary-search/)| [Python](./easy/BinarySearch.py) | Easy | Create left,right, and middle pointer | 
|[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)| [Python](./medium/Search2DMatrix.py) [C++](./medium/Search2DMatrix.cpp)| Medium | Find row by comparing 0th and -1th index -> regular binary search on row | 
|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](./medium/FindMinimumInRotatedSortedArray.py) | Medium | If right pointer greater than curr pointer move window down |
|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Python](./medium/RangeBinarySearch.py) | Medium | Two pass binary search |
|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./medium/SearchInRotatedSortedArray.py) | Medium | Check left -> mid and mid -> bounds to see if sorted |
|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)| [Python](./medium/KokoEatingBananas.py) | Medium | Binary search and keep track of amount of bannas ate |
|[Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)| [Python](./medium/TimeBasedKey-ValueStore.py) | Medium | Map key to list of lists and binary search(left = 0, right = length of key)) |


## Matrix
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | [Python](./easy/MatrixDiagonalSum.py) [C++](./easy/MatrixDiagonalSum.cpp) | Easy | Two pointer | 
|[Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) | [Python](./easy/SpecialPosMatrix.py) | Easy | Map r,c to counts of '1' | 
|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./medium/ValidSudoku.py) [C++](./medium/ValidSudoku.cpp) | Medium | Map with R, C, and 3x3 |
|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](./medium/SpiralMatrix.py) | Medium | Keep track of L,R,T,B | 
|[Set Matrix Zeros](https://leetcode.com/problems/set-matrix-zeroes/) | [Python](./medium/SetMatrixZeroes.py) | Medium | Create set for rows and cols with zeros | 
|[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](./medium/SearchA2DMatrix.py) | Medium | Binary Search | 
|[Game of Life](https://leetcode.com/problems/game-of-life/) | [Python](./medium/GameofLife.py) | Medium | Use set to store indexes for zeros and ones |
|[Rotate Matrix 90 Degrees](https://app.codesignal.com/interview-practice/question/5A8jwLGcEpTPyyjTB/description) | [Python](./code-signal/rotateImage.py) | Medium | Take transpose then go through range n//2 then swap [i][j], [j][i] <-> [i][n-j], [i][j] | 

## Sliding Window
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./easy/BestTimeBuyStock.py) | Easy | Keep track of highest |
|[Maximum Average Subarray l](https://leetcode.com/problems/maximum-average-subarray-i/)| [Python](./easy/MaxSubarrayl.py) | Easy | Find max sum -> return max_sum/k |
|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)| [Python](./medium/BuySellStock2.py) | Medium | Add to profit if profit[i] < profit[i+1] |
|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](./medium/LongestSubstringWithoutRepeatingCharacters.py) [C++](./medium/LongSubstringWithoutRepeatingCharacters.cpp) | Medium | Slding window |
|[Permutation in String](https://leetcode.com/problems/permutation-in-string/)| [Python](./medium/PermutationInString.py) | Medium | Sliding window | 
|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)| [Python](./medium/MergeIntervals.py) | Medium | Sort by start time -> sliding window | 
|[Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)| [Python](./medium/VowelSubstring.py) | Medium | Find count from 0 -> k then sliding window k -> len(s) | 
|[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)| [Python](./medium/MinSizeSubSum.py) | Medium | Sliding window | 
|[Find Longest Subarray By Sum](https://app.codesignal.com/interview-practice/question/izLStwkDr5sMS9CEm/description)| [Python](./code-signal/findLongestSubarrayBySum.py) | Medium | increase window size until sum > target then minimize left side of window until > target | 
|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)| [Python](./hard/MinWindowSubstring.py) | Hard | Update valid matches when ct is == to t[c] and store range in tuple |


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
|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [Python](./medium/ReverseLL2.py) | Medium | 3 pass and use multiple pointers |
|[Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](./medium/CopyListWithRandomPointer.py) | Medium | Map old node to new node |
|[Partition List](https://leetcode.com/problems/partition-list/) | [Python](./medium/PartList.py) | Medium | One pass with 2 dummy nodes |
|[Reorder List](https://leetcode.com/problems/reorder-list/) | [Python](./medium/ReorderList.py) | Medium | Find middle using 2 ptr, reverse list end -> middle, merge | 
|[LRU Cache](https://leetcode.com/problems/lru-cache/)| [Python](./medium/LRUCache.py) | Medium | Use a map and deque |
|[Remove K from List](https://app.codesignal.com/interview-practice/question/gX7NXPBrYThXZuanm/description) | [Python](./code-signal/removedKFromList.py) | Medium | check for curr.next.next and return head if head.val != k | 
|[Convert Sorted Linked List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)| [Python](./medium/ConvertSortedListToBinarySearchTree.py) | Medium | Create list of vals and dfs helper function |
|[Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)| [Python](./medium/SplitLinkedListInParts.py) | Medium | Get length of list and append to ans when part size hit |
|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)| [Python](./hard/MergeKSortedLists.py) | Hard | Create helper function to merge 2 lists and merge first list with rest |

## Trees
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [Python](./easy/DFS.py) | Easy | DFS | 
|[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | [Python](./easy/SumLeftLeaf.py) | Easy | DFS | 
|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [Python](./easy/BinaryTreePostTraversal.py) | Easy | Recrusive DFS or use stack and BFS iterativly and return reversed list | 
|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | [Python](./easy/CountGoodNodes.py) | Easy | BFS and add by length of queue | 
|[Bianry Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [Python](./easy/BinaryTreePaths.py) | Easy | DFS and checkk if not root.left and not root.right | 
|[Path Sum](https://leetcode.com/problems/path-sum/) | [Python](./easy/PathSum.py) | Easy | DFS and keep track of current sum | 
|[Mode in BST](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | [Python](./easy/ModeBST.py) | Easy | DFS and map frequency | 
|[Convert Sorted Array To BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [Python](./easy/ConvertSortedToBST.py) | Easy | Use recursion and keep track of middle to find sub node | 
|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./easy/MaxDepthBinaryTree.py) | Easy | recursive dfs and return 1 + max of left and right subtree |
|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Python](./easy/MinDepthBinaryTree.py) | Easy | DFS and update node count in paramenter |
|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [Python](./easy/InvertTree.py) | Easy | Swap nodes the recurse |
|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](./easy/DiameterBinaryTree.py) | Easy | DFS and check for max(left+right+1,max(left,right)) |
|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](./easy/BalancedBinaryTree.py) | Easy | Create bool variable for ans, dfs and check if max(left,right) - min(left,right) > 1, change ans |
|[Same Tree](https://leetcode.com/problems/same-tree/) | [Python](./easy/SameTree.py) | Easy | dfs and append to 2 lists |
|[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | [Python](./easy/SubtreeofAnotherTree.py) | Easy | dfs until root.val == subRoot.val and use helper function for same tree |
|[Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](./medium/LowestCommonAncestorBST.py) | Medium | DFS until split (root > p.val and root <  q.val (vise versa)) |
|[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](./medium/SumRootToLeafNumbers.py) | Medium | DFS and keep track of int with str |
|[Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) | [Python](./medium/PalindromePath.py) | Medium | DFS -> keep cts of values -> check if max odd value is <= 1 |
|[Path Sum ll](https://leetcode.com/problems/path-sum-ii/) | [Python](./medium/PathSum2.py) | Medium | DFS with stack and check when sum(stack) = target |
|[Path Sum lll](https://leetcode.com/problems/path-sum-iii/) | [Python](./medium/PathSum3.py) | Medium | Brute force and get sum of every root |
|[Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) | [Python](./medium/TreeInfect.py) | Medium | Convert to undirected graph then dfs |
|[Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) | [Python](./medium/MaxDiffAncest.py) | Medium | Return min and max pairs to calculate diff |
|[Symetric Tree](https://leetcode.com/problems/symmetric-tree/) | [Python](./medium/SymetricTree.py) | Medium | DFS with invert recursive call |
|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](./medium/BinaryTreeLevelOrderTraversal.py) | Medium | BFS |
|[Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) | [Python](./medium/LargestValueinTreeRow.py) | Medium | BFS |
|[Kth Largest Sum Binary Tree ](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/) | [Python](./medium/KthLargestSumBinaryTree.py) | Medium | BFS |
|[Binary Tree ZigZag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Python](./medium/BinaryTreeZigZag.py) | Medium | BFS and use list slcing to reverse |
|[Maximum Level Sum of Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | [Python](./medium/MaxLevelSumBinaryTree.py) | Medium | DFS and check if not root.left and not root.right | 
|[Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | [Python](./medium/CountNodesAverage.py) | Medium | DFS and return tuple of previous edges and sum to avoid brute force |
|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](./medium/ValidateBST.py) | Medium | DFS and keep track of curr min and max |
|[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](./medium/BinaryTreeRightSideView.py) | Medium | Create left and right deque and append from end of deque |
|[Count Good Noes in Binary Tree ](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Python](./medium/CountGoodNodesinBinaryTree.py) | Medium | DFS and keep track of curr max |
|[Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Python](./medium/KthSmallestBST.py) | Medium | In order Traversal -> return k-1 |
|[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/) | [Python](./medium/MaximumBinaryTree.py) | Medium | Get max of nums -> -> dfs with left and right subarray |
|[Print Binary Tree](https://leetcode.com/problems/print-binary-tree/) | [Python](./medium/PrintBinaryTree.py) | Medium | Get height -> create matrix -> dfs |
|[Binary Tree Maximum Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Python](./hard/MaxPathSumBinaryTree.py) | Hard | DFS and compare left and right recursive calls with max(0,left or right) to get edge case of root itself being max |
|[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Python](./hard/DesAndSerTree.py) | Hard | DFS to turn tree to str then use refernce incremnter to loop through split data |


## Tries
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Implement Tries (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Python](./medium/ImplementTrie.py) | Medium | Create node class of hashmap to map each char to a unique path |
|[Design Add and Search Words Data Structures](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/) | [Python](./medium/DesignDict.py) | Medium | Create node class of hashmap and dfs for search (explore all paths if char == '.') |

## Heap & Priority Queue
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Python](./easy/kthLargestStream.py) | Easy | Keep min heap size of k and return root |
|[Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/) | [Python](./medium/SeatReservationManager.py) | Medium | Min heap |
|[Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/) | [Python](./medium/MaxNumMonsters.py) | Medium | Use min heap and push when monster will arrive to city by dist[i]/spped[i] |
|[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | [Python](./medium/LastStoneWeight.py) | Medium | Max heap |
|[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | [Python](./medium/ClosestPointsOrigin.py) | Medium | Min heap with tuple |
|[K Largest Element in Array](https://leetcode.com/problems/kth-largest-element-in-an-array) | [Python](./medium/KthLargest.py) | Medium | Max heap or sorted |



## Backtracking
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Subsets](https://leetcode.com/problems/subsets/) | [Python](./medium/subsets.py) | Medium | DFS use stack to take care of 'dont include' descison | 
|[Subsets ll](https://leetcode.com/problems/subsets-ii/) | [Python](./medium/Subset2.py) | Medium | Sort -> dfs and do not include duplicates in choices |
|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [Python](./medium/GenParent.py) | Medium | DFS  -> compare open with n -> compare open with closed |
|[Combination Sum](https://leetcode.com/problems/combination-sum/) | [Python](./medium/CombinationSum.py) | Medium | DFS until index > lenth or sum(stack) == target or sum(stack) > target |
|[Combination Sum ll](https://leetcode.com/problems/combination-sum-ii/) | [Python](./medium/CombinationSum2.py) | Medium | Sort list -> dfs backtrack -> skip over duplicates |
|[Word Search](https://leetcode.com/problems/word-search/) | [Python](./medium/WordSearch.py) | Medium | DFS and keep track of visited and replace board with original values once depth reached |
|[Permutations](https://leetcode.com/problems/permutations/) | [Python](./medium/permutations.py) | Medium | Keep track of choices with boolean list size of nums |
|[Combinations](https://leetcode.com/problems/combinations/) | [Python](./medium/Combinations.py) | Medium | Backtrack |
|[Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | [Python](./medium/BArrangement.py) | Medium | Backtrack |
|[Non Decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/) | [Python](./medium/NonDecSubseq.py) | Medium | Backtrack and store perms in  a set |
|[Palidrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | [Python](./medium/PaliPart.py) | Medium | Dfs and check for palidrome |
|[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | [Python](./hard/SudokuSolver.py) | Hard | Backtrack with checking if next empty spot is valid |
|[N-Queens](https://leetcode.com/problems/n-queens/) | [Python](./hard/NQueens.py) | Hard | Backtrack and keep tract of pos and neg diags (r+c) and (r-c) |


## Graphs
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Flood Fill](https://leetcode.com/problems/flood-fill/) | [Python](./easy/FloodFill.py) | Easy | DFS |
|[Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./medium/NumberOfIslands.py) | Medium | DFS and change '1' to random char | 
|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [Python](./medium/MaxAreaIsland.py) | Medium | DFS use list to store counts to avoid counter resetting |
|[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Python](./medium/PacificAtlanticWaterFlow.py) | Medium | Find paths for atlantic and pacific and store in a set |
|[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | [Python](./medium/SurroundedRegions.py) | Medium | Find invalid regions using dfs and store in a set -> find valid replacements going through orginal board |
|[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [Python](./medium/RottingOranges.py) | Medium | BFS and check neighbors |
|[Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python](./medium/CourseSchedule.py) | Medium | DFS topological sort |
|[Course Schedule ll](https://leetcode.com/problems/course-schedule-ii/) | [Python](./medium/CourseSchedule2.py) | Medium | DFS topological sort and check for courses not in prerequisites |
|[Clone Graph](https://leetcode.com/problems/clone-graph/) | [Python](./medium/CloneGraph.py) | Medium | Map node to new node -> dfs |
|[Redundant Connections](https://leetcode.com/problems/redundant-connection/) | [Python](./medium/RedundantConnection.py) | Medium | DFS |
|[Network Delay Time](https://leetcode.com/problems/network-delay-time/) | [Python](./medium/NetworkDelayTime.py) | Medium | Dijkstra algorithm |
|[Path with Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | [Python](./medium/PathMinEffort.py) | Medium | Dijkstra + memo |
|[Restore the Array From Adjacent Pairs](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/) | [Python](./medium/RestoreAdjPairs.py) | Medium | Create adj list -> find vertex with outdegree of 1 -> create ans iterativly |
|[Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) | [Python](./medium/GeneMutation.py) | Medium | BFS similar to Word Ladder |
|[Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python](./hard/WordLadder.py) | Hard | BFS and get possible paths by using temp char to replace current word |
|[Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Python](./hard/LongIncreasingString.py) | Hard | DFS and memoization |
|[Design Graph With Shortest Path Calculator](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) | [Python](./hard/Dij.py) | Hard | Dijkstra algorithm |


## Dynamic Programming
| Problem | Solution | Difficulty | Hint |
| ------- | -------- | ---------- | ------------ |
|[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | [Python](./easy/ClimbingStairs.py) | Easy | Bottom up and find sum of previous 2 steps |
|[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Python](./easy/MinCostClimbingStairs.py) | Easy | Bottom up and compare minimum of current cost and next 2 steps | 
|[Array Max Consective Sum](https://app.codesignal.com/interview-practice/question/dQD4TCunke2JQ98rj/description) | [Python](./code-signal/maxConsecutiveSum2.py) | Medium | Keep track of curr max and global max and use kadones algorithm |




