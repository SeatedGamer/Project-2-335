# Chase Hales, Chris Reyes
# CPSC 335 - Algorithm Engineering, Project 2
# Problem 2: Counting Islands in a Grid (graph traversal)
#
# Idea: treat every '1' cell as a node in a graph, joined to any '1' cell that
# touches it directly (up, down, left or right). One island = one connected
# group of nodes.
# Method: walk over the whole grid. Whenever we reach a '1' we have not seen
# before, that is a brand-new island, so add 1 to the count and run an
# iterative depth-first search (DFS) from there to mark every '1' in the same
# island as visited. The DFS keeps its own stack instead of recursing, so a
# huge island cannot trigger Python's recursion limit.
# Running time: O(m * n). Each cell is looked at once by the scan and goes onto
# the stack at most once, and every cell taken off the stack checks 4 neighbors.

# Allowed moves: up, down, left, right. Diagonals do not connect land.
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_islands(grid):
    """Count the islands in an m x n grid whose cells are the strings '1' (land) and '0' (water)."""
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]   # True once (r, c) has been seen
    islands = 0

    for r in range(m):
        for c in range(n):
            # Unseen land means we have found a new island.
            if grid[r][c] == '1' and not visited[r][c]:
                islands += 1
                visited[r][c] = True
                stack = [(r, c)]

                # DFS: visit every land cell reachable from (r, c).
                while stack:
                    row, col = stack.pop()
                    for dr, dc in DIRECTIONS:
                        nr, nc = row + dr, col + dc
                        # Only step onto unseen land that is inside the grid.
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and not visited[nr][nc]:
                            visited[nr][nc] = True   # mark now, at push time, so a cell is never pushed twice
                            stack.append((nr, nc))

    return islands


# Examples from the assignment: (grid, expected output).
EXAMPLES = [
    ([["0", "1", "1", "0", "0"],
      ["0", "1", "0", "0", "1"],
      ["1", "0", "0", "1", "1"],
      ["1", "0", "1", "0", "0"],
      ["0", "0", "1", "1", "0"]], 4),
    ([["1", "1", "1", "0"],
      ["1", "0", "1", "0"],
      ["1", "1", "1", "0"],
      ["0", "0", "0", "1"]], 2),
    ([["1", "0", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "1", "1"],
      ["0", "0", "0", "1", "0", "0"],
      ["0", "1", "1", "1", "0", "1"],
      ["0", "0", "0", "0", "0", "1"],
      ["1", "1", "0", "1", "0", "0"]], 7),
]

# Extra test grids added for edge cases: (label, grid, expected output).
EXTRA_CASES = [
    ("empty grid", [], 0),
    ("single water cell", [["0"]], 0),
    ("single land cell", [["1"]], 1),
    ("all water", [["0", "0", "0"],
                   ["0", "0", "0"],
                   ["0", "0", "0"]], 0),
    ("all land", [["1", "1", "1", "1"],
                  ["1", "1", "1", "1"],
                  ["1", "1", "1", "1"]], 1),
    ("diagonals do not connect (checkerboard)", [["1", "0", "1"],
                                                 ["0", "1", "0"],
                                                 ["1", "0", "1"]], 5),
    ("single row", [["1", "0", "1", "1", "0", "1"]], 3),
    ("single column", [["1"], ["1"], ["0"], ["1"]], 2),
    ("island inside a lake", [["1", "1", "1", "1", "1"],
                              ["1", "0", "0", "0", "1"],
                              ["1", "0", "1", "0", "1"],
                              ["1", "0", "0", "0", "1"],
                              ["1", "1", "1", "1", "1"]], 2),
]


def run_case(title, grid, expected):
    result = count_islands(grid)
    status = "PASS" if result == expected else "FAIL"
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    print(f"{title}: {rows} x {cols} grid")
    for row in grid:
        print("  " + " ".join(row))
    print(f"  Output: {result}   (expected {expected})  {status}")


def main():
    print("Problem 2: Counting Islands in a Grid")
    for number, (grid, expected) in enumerate(EXAMPLES, start=1):
        run_case(f"Example {number}", grid, expected)

    print()
    print("Extra test grids")
    for label, grid, expected in EXTRA_CASES:
        run_case(label.capitalize(), grid, expected)


if __name__ == "__main__":
    main()
