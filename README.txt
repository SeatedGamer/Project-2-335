Chase Hales, Chris Reyes
CPSC 335 - Algorithm Engineering, Fall 2026
Project 2: Counting Reverse Pairs and Counting Islands in a Grid

LANGUAGE AND VERSION
  Python 3 (tested with Python 3.13; any Python 3.8 or newer works).
  Python is interpreted, so there is no separate compile step.

FILES
  problem1_reverse_pairs.py   Problem 1 - Counting Reverse Pairs (divide and conquer)
  problem2_islands.py         Problem 2 - Counting Islands in a Grid (iterative DFS)

HOW TO RUN
  Open a terminal in the folder that contains the files, then run:

    Problem 1:   python3 problem1_reverse_pairs.py
    Problem 2:   python3 problem2_islands.py

  On Windows, use "python" or "py" instead of "python3" if needed, for example:
    py problem1_reverse_pairs.py

INPUT
  The three examples from the assignment for each problem are hard-coded at the
  top of each file in the EXAMPLES list, followed by a list of extra edge-case
  tests in EXTRA_CASES. No input file or typing is needed.
  To try a different input, add an entry to either list.

OUTPUT
  Each program prints every example and extra test case, the computed answer,
  the expected answer, and PASS or FAIL. Problem 1 also prints a brute-force O(n^2) count as a
  cross-check (the brute force is used only for checking, not as the solution).

  Expected results for the three assignment examples:
    Problem 1: 4, 3, 13
    Problem 2: 4, 2, 7
  Every extra test case should also print PASS (nine for each problem).

LIBRARIES / EXTRA FILES
  None. Only built-in Python is used; there are no imports or extra files.
