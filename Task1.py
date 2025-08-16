import random
from timeit import timeit
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    # If the array has fewer than two elements, it is already sorted
    if len(arr) < 2:
        return arr

    # Choose a random index for the pivot element
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Split the array into parts
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right parts, then combine them
    return (
        randomized_quick_sort(left)
        + [pivot] * arr.count(pivot)
        + randomized_quick_sort(right)
    )


def deterministic_quick_sort(arr, pivot_index="mid"):
    if len(arr) <= 1:
        return arr

    # Choose the pivot element of the array
    if pivot_index == "first":
        pivot = arr[0]
    elif pivot_index == "last":
        pivot = arr[-1]
    else:
        pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return (
        deterministic_quick_sort(left, pivot_index)
        + [pivot] * arr.count(pivot)
        + deterministic_quick_sort(right, pivot_index)
    )


if __name__ == "__main__":
    # Sizes of test arrays
    sizes = [10000, 50000, 100000, 500000]
    randomized_times = []
    deterministic_times_pivot_first = []
    deterministic_times_pivot_mid = []
    deterministic_times_pivot_last = []

    # Run the tests
    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]

        # Measure average time for randomized_quick_sort
        rand_time = timeit(lambda: randomized_quick_sort(arr[:]), number=5)

        # Measure average time for deterministic_quick_sort
        det_time_p_first = timeit(
            lambda: deterministic_quick_sort(arr[:], pivot_index="first"), number=5
        )
        det_time_p_mid = timeit(lambda: deterministic_quick_sort(arr[:]), number=5)
        det_time_p_last = timeit(
            lambda: deterministic_quick_sort(arr[:], pivot_index="last"), number=5
        )

        randomized_times.append(rand_time)
        deterministic_times_pivot_first.append(det_time_p_first)
        deterministic_times_pivot_mid.append(det_time_p_mid)
        deterministic_times_pivot_last.append(det_time_p_last)

        print(f"Array size: {size}")
        print(
            f"   Randomized QuickSort                        : {rand_time:.4f} seconds"
        )
        print(
            f"   Deterministic QuickSort (pivot - first)     : {det_time_p_first:.4f} seconds\n"
        )
        print(
            f"   Deterministic QuickSort (pivot - middle)    : {det_time_p_mid:.4f} seconds\n"
        )
        print(
            f"   Deterministic QuickSort (pivot - last)      : {det_time_p_last:.4f} seconds\n"
        )

    # Plot the chart
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, randomized_times, label="Randomized QuickSort", color="blue")
    plt.plot(
        sizes,
        deterministic_times_pivot_first,
        label="Deterministic QuickSort (pivot first)",
        color="orange",
    )
    plt.plot(
        sizes,
        deterministic_times_pivot_mid,
        label="Deterministic QuickSort (pivot mid)",
        color="green",
    )
    plt.plot(
        sizes,
        deterministic_times_pivot_last,
        label="Deterministic QuickSort (pivot last)",
        color="violet",
    )

    plt.xlabel("Array size")
    plt.ylabel("Average execution time (seconds)")
    plt.title("Comparison of Randomized and Deterministic QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()
