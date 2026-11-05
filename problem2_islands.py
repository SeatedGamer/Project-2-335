# Chase Hales
# CPSC 335 - Algorithm Engineering, Project 2
# Problem 2: Counting Islands in a Grid (graph traversal)
#
# Each '1' cell is a vertex of a graph, with an edge to every '1' cell directly
# above, below, left or right of it. An island is a connected component.
# We scan every cell; each time we find an unvisited '1', we count a new island
# and run an iterative depth-first search (DFS) from it to mark every connected
# '1' as visited. An explicit stack is used instead of recursion so that large
# grids cannot hit Python's recursion limit.
# Running time: O(m * n), because every cell is scanned once and pushed onto
# the stack at most once, and each pop checks only 4 neighbors.

# The four allowed directions: up, down, left, right (no diagonals).
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_islands(grid):
    """Return the number of islands in an m x n grid of '1' and '0' characters."""
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]   # visited[r][c] is True once (r, c) is explored
    islands = 0

    for r in range(m):
        for c in range(n):
            # A new island starts at any land cell we have not explored yet.
            if grid[r][c] == '1' and not visited[r][c]:
                islands += 1
                visited[r][c] = True
                stack = [(r, c)]

                # Iterative DFS: mark every land cell connected to (r, c).
                while stack:
                    row, col = stack.pop()
                    for dr, dc in DIRECTIONS:
                        nr, nc = row + dr, col + dc
                        # Stay inside the grid, and only follow unvisited land.
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and not visited[nr][nc]:
                            visited[nr][nc] = True   # mark when pushed so no cell is pushed twice
                            stack.append((nr, nc))

    return islands


def main():
    # Hard-coded examples from the assignment: (grid, expected output).
    examples = [
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

    print("Problem 2: Counting Islands in a Grid")
    for number, (grid, expected) in enumerate(examples, start=1):
        result = count_islands(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"Example {number}: {len(grid)} x {len(grid[0])} grid")
        for row in grid:
            print("  " + " ".join(row))
        print(f"  Output: {result}   (expected {expected})  {status}")


if __name__ == "__main__":
    main()
