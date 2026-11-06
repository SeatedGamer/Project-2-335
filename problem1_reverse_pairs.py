# Chase Hales, Chris Reyes, Alexavier Lualhati, Darren Ngo
# CPSC 335 - Algorithm Engineering, Project 2
# Problem 1: Counting Reverse Pairs (divide and conquer)
#
# A reverse pair is two positions i < j where nums[i] > 2 * nums[j].
#
# Approach: a merge sort that counts pairs while it sorts.
#   1. Cut the array into a left half and a right half.
#   2. Recursively sort each half, and get the number of pairs inside each.
#   3. Count the pairs that straddle the cut (one value from each half). Both
#      halves are sorted at this point, so one left-to-right sweep with two
#      pointers is enough.
#   4. Merge the two sorted halves and return the sorted list plus the total.
# Running time: T(n) = 2T(n/2) + O(n), which is O(n log n) (Master Theorem, Case 2).
# Python ints are unbounded, so 2 * nums[j] can never overflow.


def sort_and_count(arr):
    """Return a sorted copy of arr together with its reverse-pair count."""
    n = len(arr)

    # Base case: with 0 or 1 elements there is nothing to pair and nothing to sort.
    if n <= 1:
        return list(arr), 0

    # Divide: find the middle and split into two halves.
    mid = n // 2
    left, left_count = sort_and_count(arr[:mid])     # solve the left half
    right, right_count = sort_and_count(arr[mid:])   # solve the right half

    # Combine, part 1: count pairs with one value in each half.
    # Both halves are ascending. For each left[i], move j forward while
    # left[i] > 2 * right[j]; at that point right[0..j-1] all form a pair with
    # left[i]. A larger left[i+1] satisfies everything left[i] did, so j never
    # has to back up and the sweep is linear.
    cross_count = 0
    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        cross_count += j

    # Combine, part 2: ordinary merge of the two sorted halves.
    merged = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            merged.append(left[a])
            a += 1
        else:
            merged.append(right[b])
            b += 1
    merged.extend(left[a:])    # leftover values from the left half
    merged.extend(right[b:])   # leftover values from the right half

    return merged, left_count + right_count + cross_count


def count_reverse_pairs(nums):
    """Return the number of reverse pairs in nums (nums itself is left unchanged)."""
    _, count = sort_and_count(nums)
    return count


def brute_force(nums):
    """Slow O(n^2) check of every pair; used only to verify the fast version."""
    n = len(nums)
    return sum(1 for i in range(n) for j in range(i + 1, n) if nums[i] > 2 * nums[j])


# Examples from the assignment: (input, expected output).
EXAMPLES = [
    ([5, 1, 8, 3, 2], 4),
    ([2, 4, 3, 5, 1, 12, 6], 3),
    ([9, 4, -2, 7, 1, 3, 0], 13),
]

# Extra edge cases added for testing: (label, input, expected output).
EXTRA_CASES = [
    ("empty array", [], 0),
    ("single element", [7], 0),
    ("all negatives, ascending", [-5, -4, -3], 3),
    ("all negatives, descending", [-1, -2, -3, -4], 6),
    ("all zeros", [0, 0, 0], 0),
    ("all equal positives", [2, 2, 2], 0),
    ("sorted ascending", [1, 2, 3, 4, 5], 0),
    ("sorted descending", [5, 4, 3, 2, 1], 4),
    ("positive then negative", [1, -1], 1),
]


def run_case(title, nums, expected):
    result = count_reverse_pairs(nums)
    status = "PASS" if result == expected else "FAIL"
    print(f"{title}: nums = {nums}")
    print(f"  Output: {result}   (expected {expected}, brute force {brute_force(nums)})  {status}")


def main():
    print("Problem 1: Counting Reverse Pairs (divide and conquer)")
    for number, (nums, expected) in enumerate(EXAMPLES, start=1):
        run_case(f"Example {number}", nums, expected)

    print()
    print("Extra test cases")
    for label, nums, expected in EXTRA_CASES:
        run_case(label.capitalize(), nums, expected)


if __name__ == "__main__":
    main()
