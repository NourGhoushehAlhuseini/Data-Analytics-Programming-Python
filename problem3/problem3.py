problem = "problem3"
student_name = "nour"
student_number = "t0326796"

import random
import time

# bubble sort
def bubble_sort(L):
    n = len(L)
    comparisons = 0
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1  # counts comparison
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        if not swapped:
            break  # if no swaps occur, list is already sorted
    return comparisons

# selection sort
def selection_sort(L):
    n = len(L)
    comparisons = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1  # counts the comparison
            if L[j] < L[min_index]:
                min_index = j  # update the index of smallest element
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]  # Swap
    return comparisons

# merge sort
def merge_sort(L):
    if len(L) <= 1:
        return L, 0  # already sorted
    mid = len(L) // 2
    left, left_comparisons = merge_sort(L[:mid])
    right, right_comparisons = merge_sort(L[mid:])
    merged, merge_comparisons = merge(left, right)
    return merged, left_comparisons + right_comparisons + merge_comparisons

def merge(left, right):
    result = []
    i = j = merge_comparisons = 0
    while i < len(left) and j < len(right):
        merge_comparisons += 1  # count the comparison
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, merge_comparisons

def sort_comparison(list_size, sorted=False):
    # generates the list: Sorted or Random
    arr = list(range(1, list_size + 1)) if sorted else random.sample(range(1, list_size * 10), list_size)

    # prints the generated list
    print(f"\nList of size {list_size} to sort is: {arr}\n")

    # copies lists for each sorting algorithm
    list_bubble = arr[:]
    list_selection = arr[:]
    list_merge = arr[:]

    # accurate time measurement
    start_time = time.perf_counter()
    bubble_cmp = bubble_sort(list_bubble)
    bubble_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    selection_cmp = selection_sort(list_selection)
    selection_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    _, merge_cmp = merge_sort(list_merge)
    merge_time = time.perf_counter() - start_time

    # displays the results
    print(f"Number of comparisons for Bubble Sort: {bubble_cmp}")
    print(f"Number of comparisons for Selection Sort: {selection_cmp}")
    print(f"Number of comparisons for Merge Sort: {merge_cmp}")

    print("\nExecution Times:")
    print(f"Bubble Sort Time: {bubble_time:.10f} seconds")
    print(f"Selection Sort Time: {selection_time:.10f} seconds")
    print(f"Merge Sort Time: {merge_time:.10f} seconds")

def main():
    # gets the list size from user
    while True:
        try:
            list_size = int(input("\nEnter the size of the list to sort: "))
            if list_size <= 0:
                raise ValueError("List size must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")

    # asks if the list should be pre sorted
    while True:
        is_sorted_input = input("Do you want to sort an already sorted list? (yes/no): ").strip().lower()
        if is_sorted_input in ["yes", "no"]:
            is_sorted = is_sorted_input == "yes"
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    sort_comparison(list_size, is_sorted)

if __name__ == "__main__":
    main()
