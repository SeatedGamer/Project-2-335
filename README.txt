Chase Hales
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
  The three examples from the assignment for each problem are hard-coded in
  the main() function of each file. No input file or user typing is needed.
  To try a different input, edit the "examples" list in main().

OUTPUT
  Each program prints every example, the computed answer, the expected answer,
  and PASS or FAIL. Problem 1 also prints a brute-force O(n^2) count as a
  cross-check (the brute force is used only for checking, not as the solution).

  Expected results:
    Problem 1: 4, 3, 13
    Problem 2: 4, 2, 7

LIBRARIES / EXTRA FILES
  None. Only the Python standard language is used; no imports or extra files.
