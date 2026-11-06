# CPSC 335 – Project 2
Course: CPSC 335 Algorithm Engineering, Fall 2026  
Submission: Project 2  
Language: Python 3

**Group 7 Members:**
```
 Chase Hales, chales@csu.fullerton.edu
 Chris Reyes, car814435@csu.fullerton.edu
 Alexavier Lualhati, alualhat1@csu.fullerton.edu
 Darren Ngo, dngo18@csu.fullerton.edu
```

## Problem 1: Counting Reverse Pairs (Divide and Conquer)

The algorithm designed modifies merge sort with each call splitting the array in half, recursively counting and sorting each half, and counting the pairs that cross the halves with a single two-pointer pass which will then be merged with the other halves.  

### Pseudocode

```text
function COUNT-REVERSE-PAIRS(nums)
    (sorted, count) ← SORT-AND-COUNT(nums)
    return count

function SORT-AND-COUNT(A[0..n-1])
    if n ≤ 1 then
        return (A, 0)                          // base case: no pairs
    mid ← ⌊n / 2⌋
    (L, leftCount)  ← SORT-AND-COUNT(A[0..mid-1])   // divide + conquer
    (R, rightCount) ← SORT-AND-COUNT(A[mid..n-1])

    // combine step 1: count cross pairs (L and R are sorted ascending)
    crossCount ← 0
    j ← 0
    for i ← 0 to |L| - 1 do
        while j < |R| and L[i] > 2 × R[j] do
            j ← j + 1
        crossCount ← crossCount + j         // R[0..j-1] all pair with L[i]

    // combine step 2: merge the two sorted halves
    M ← empty list;  a ← 0;  b ← 0
    while a < |L| and b < |R| do
        if L[a] ≤ R[b] then append L[a] to M; a ← a + 1
        else                append R[b] to M; b ← b + 1
    append L[a..|L|-1] and R[b..|R|-1] to M

    return (M, leftCount + rightCount + crossCount)
```

**Why the two-pointer pass is correct:**  
Since L is sorted ascending ( L[i] > 2 x R[j] ),  
every element from L[i] in the sorted left half onward forms reverse pairs with R[j] ( L[i+1] >= L[i] > 2 x R[j] ).  

The two-pointer pass ensures that j never has to move backwards, as both halves are sorted in ascending order. Every pair of (i, j), where i < j, will either lie in one half where the recursion will count it, or cross the halves where the pass will count it, so sorting the halves will not change which elements are in the left or right, making the cross count remain valid. 

### Mathematical Analysis

**Step count of the combine work**  
For a subarray of size n: 
- Splitting (copying the two halves into new lists): n steps.  
- Cross-pair pass: the outer loop runs n/2 times, and j increases at most n/2 times in total, so at most n steps.  
- Merge: each step outputs one element, so n steps.  
- Total combine work: f(n) ≤ 3cn for a constant c, so f(n) = Θ(n).

**Recurrence relation**  
Each call makes two recursive calls on halves of the array plus linear combine work:

T(n) = 2T(n/2) + Θ(n),    T(1) = Θ(1)

**Master Theorem**  
The recurrence has the form:  
T(n) = aT(n/b) + f(n) with a = 2, b = 2, and f(n) = Θ(n) 

Then,  
n<sup>log<sub>b</sub> a</sup> = n<sup>log<sub>2</sub> 2</sup> = n<sup>1</sup> = n. Since f(n) = Θ(n<sup>log<sub>b</sub> a</sup>)  

**Case 2** of the Master Theorem applies, which gives T(n) = Θ(n<sup>log<sub>b</sub> a</sup> log n).

Efficiency class: T(n) = Θ(n log n), so O(n log n). Master Theorem Case 2.

Extra space is O(n) for the merged and copied arrays. The recursion depth is ⌈log<sub>2</sub> n⌉.

## Problem 2: Counting Islands in a Grid

The algorithm designed counts the number of islands in the grid, scanning every cell of a given 2D grid map of 1s (land) and 0s (water). The algorithm will run a DFS (depth-first search) when it finds an unvisited island to count it as a new island and mark it as visited, using an explicit stack to prevent overflow on the call stack. 

### Pseudocode

```text
function COUNT-ISLANDS(grid[0..m-1][0..n-1])
    if m = 0 or n = 0 then return 0
    visited[0..m-1][0..n-1] ← false          // all cells unvisited
    islands ← 0
    for r ← 0 to m - 1 do
        for c ← 0 to n - 1 do
            if grid[r][c] = '1' and not visited[r][c] then
                islands ← islands + 1           // found a new island
                visited[r][c] ← true
                stack ← [ (r, c) ]
                while stack is not empty do       // DFS over this island
                    (row, col) ← POP(stack)
                    for each (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)) do
                        nr ← row + dr;  nc ← col + dc
                        if 0 ≤ nr < m and 0 ≤ nc < n
                           and grid[nr][nc] = '1' and not visited[nr][nc] then
                            visited[nr][nc] ← true      // mark when pushed
                            PUSH(stack, (nr, nc))
    return islands
```

### Mathematical Analysis (method: step counts)

Let the grid have m rows and n columns, so it has mn cells.

• **Initializing visited:** one step per cell, so mn steps.  
• **Outer double loop:** runs exactly mn times. Each iteration does a constant amount of work (one test), so this part takes c<sub>1</sub>mn steps.  
• **DFS work:** a cell is pushed onto the stack only when it changes from unvisited to visited, and it never changes back. So each cell is pushed, and later popped, *at most once* over the entire run, and there are at most mn pops. Each pop examines exactly 4 neighbors with constant work per neighbor, so all DFS work combined takes at most 4c<sub>2</sub>mn steps.  
• **Total:** T(m, n) ≤ mn + c<sub>1</sub>mn + 4c<sub>2</sub>mn = (1 + c<sub>1</sub> + 4c<sub>2</sub>)·mn.

Since 1 + c<sub>1</sub> + 4c<sub>2</sub> is a constant, T(m, n) ∈ O(mn). The outer loop alone always performs mn iterations, so T(m, n) ≥ mn, which gives a lower bound of Ω(mn).

Efficiency class: T(m, n) = Θ(mn), so O(m × n).  Method: step counts.

Extra space is O(mn): the visited array has mn entries, and in the worst case (an all-land grid) the stack can hold O(mn) cells.

## Results

Each program runs the three examples from the assignment plus nine extra edge-case tests (empty input, a single element or cell, all negatives, all zeros, sorted input, all water, all land, a checkerboard, a single row, a single column, and an island inside a lake). All 24 runs produce the expected output. Problem 1 also matches the O(n²) brute-force count on every case here and on 5,000 additional random arrays (values from −20 to 20, lengths 0 to 15) checked while testing; none of those arrays was modified by the function.

### Problem 1 output

```text
Problem 1: Counting Reverse Pairs (divide and conquer)
Example 1: nums = [5, 1, 8, 3, 2]
  Output: 4   (expected 4, brute force 4)  PASS
Example 2: nums = [2, 4, 3, 5, 1, 12, 6]
  Output: 3   (expected 3, brute force 3)  PASS
Example 3: nums = [9, 4, -2, 7, 1, 3, 0]
  Output: 13   (expected 13, brute force 13)  PASS

Extra test cases
Empty array: nums = []
  Output: 0   (expected 0, brute force 0)  PASS
Single element: nums = [7]
  Output: 0   (expected 0, brute force 0)  PASS
All negatives, ascending: nums = [-5, -4, -3]
  Output: 3   (expected 3, brute force 3)  PASS
All negatives, descending: nums = [-1, -2, -3, -4]
  Output: 6   (expected 6, brute force 6)  PASS
All zeros: nums = [0, 0, 0]
  Output: 0   (expected 0, brute force 0)  PASS
All equal positives: nums = [2, 2, 2]
  Output: 0   (expected 0, brute force 0)  PASS
Sorted ascending: nums = [1, 2, 3, 4, 5]
  Output: 0   (expected 0, brute force 0)  PASS
Sorted descending: nums = [5, 4, 3, 2, 1]
  Output: 4   (expected 4, brute force 4)  PASS
Positive then negative: nums = [1, -1]
  Output: 1   (expected 1, brute force 1)  PASS
```

### Problem 2 output

```text
Problem 2: Counting Islands in a Grid
Example 1: 5 x 5 grid
  0 1 1 0 0
  0 1 0 0 1
  1 0 0 1 1
  1 0 1 0 0
  0 0 1 1 0
  Output: 4   (expected 4)  PASS
Example 2: 4 x 4 grid
  1 1 1 0
  1 0 1 0
  1 1 1 0
  0 0 0 1
  Output: 2   (expected 2)  PASS
Example 3: 6 x 6 grid
  1 0 1 0 1 0
  1 1 0 0 1 1
  0 0 0 1 0 0
  0 1 1 1 0 1
  0 0 0 0 0 1
  1 1 0 1 0 0
  Output: 7   (expected 7)  PASS

Extra test grids
Empty grid: 0 x 0 grid
  Output: 0   (expected 0)  PASS
Single water cell: 1 x 1 grid
  0
  Output: 0   (expected 0)  PASS
Single land cell: 1 x 1 grid
  1
  Output: 1   (expected 1)  PASS
All water: 3 x 3 grid
  0 0 0
  0 0 0
  0 0 0
  Output: 0   (expected 0)  PASS
All land: 3 x 4 grid
  1 1 1 1
  1 1 1 1
  1 1 1 1
  Output: 1   (expected 1)  PASS
Diagonals do not connect (checkerboard): 3 x 3 grid
  1 0 1
  0 1 0
  1 0 1
  Output: 5   (expected 5)  PASS
Single row: 1 x 6 grid
  1 0 1 1 0 1
  Output: 3   (expected 3)  PASS
Single column: 4 x 1 grid
  1
  1
  0
  1
  Output: 2   (expected 2)  PASS
Island inside a lake: 5 x 5 grid
  1 1 1 1 1
  1 0 0 0 1
  1 0 1 0 1
  1 0 0 0 1
  1 1 1 1 1
  Output: 2   (expected 2)  PASS
```
