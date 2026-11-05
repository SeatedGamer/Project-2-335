# Chase Hales
# CPSC 335 - Algorithm Engineering, Project 2
# Problem 1: Counting Reverse Pairs (divide and conquer)
#
# A reverse pair is a pair of indices (i, j) with i < j and nums[i] > 2 * nums[j].
# The algorithm is a modified merge sort:
#   1. Split the array into two halves.
#   2. Recursively count (and sort) the reverse pairs inside each half.
#   3. Count the pairs that cross the halves with two pointers in one linear pass,
#      which works because both halves are already sorted.
#   4. Merge the two sorted halves and return the total count.
# Running time: T(n) = 2T(n/2) + O(n)  ->  O(n log n) by Case 2 of the Master Theorem.
# (Python integers never overflow, so 2 * nums[j] is always computed exactly.)


def sort_and_count(arr):
    """Return (sorted copy of arr, number of reverse pairs in arr)."""
    n = len(arr)

    # Base case: an array of 0 or 1 elements has no pairs and is already sorted.
    if n <= 1:
        return list(arr), 0

    # Divide: split the array into a left half and a right half.
    mid = n // 2
    left, left_count = sort_and_count(arr[:mid])     # conquer the left half
    right, right_count = sort_and_count(arr[mid:])   # conquer the right half

    # Combine, step 1: count the cross pairs (i in left half, j in right half).
    # Both halves are sorted ascending. For each left[i], advance j while
    # left[i] > 2 * right[j]; every right[0..j-1] then pairs with left[i].
    # Because left is ascending, j never needs to move backward, so the
    # whole pass is linear.
    cross_count = 0
    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        cross_count += j

    # Combine, step 2: standard merge of the two sorted halves.
    merged = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            merged.append(left[a])
            a += 1
        else:
            merged.append(right[b])
            b += 1
    merged.extend(left[a:])    # copy whatever remains in the left half
    merged.extend(right[b:])   # copy whatever remains in the right half

    return merged, left_count + right_count + cross_count


def count_reverse_pairs(nums):
    """Return the number of reverse pairs in nums (the input is not modified)."""
    _, count = sort_and_count(nums)
    return count


def brute_force(nums):
    """O(n^2) baseline used only to double-check the answers."""
    n = len(nums)
    return sum(1 for i in range(n) for j in range(i + 1, n) if nums[i] > 2 * nums[j])


def main():
    # Hard-coded examples from the assignment: (input, expected output).
    examples = [
        ([5, 1, 8, 3, 2], 4),
        ([2, 4, 3, 5, 1, 12, 6], 3),
        ([9, 4, -2, 7, 1, 3, 0], 13),
    ]

    print("Problem 1: Counting Reverse Pairs (divide and conquer)")
    for number, (nums, expected) in enumerate(examples, start=1):
        result = count_reverse_pairs(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Example {number}: nums = {nums}")
        print(f"  Output: {result}   (expected {expected}, brute force {brute_force(nums)})  {status}")


if __name__ == "__main__":
    main()
