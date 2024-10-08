import timeit
import random
import heapq


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Функція для генерації масивів
def generate_array(size, order='random'):
    if order == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif order == 'sorted':
        return list(range(size))
    elif order == 'reversed':
        return list(range(size, 0, -1))

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    stmt = lambda: sort_func(arr.copy())
    return timeit.timeit(stmt, number=1)

# Основна функція для порівняння алгоритмів
def compare_sorts():
    sizes = [1000, 5000, 10000]
    orders = ['random', 'sorted', 'reversed']
    algorithms = [
        ('Insertion Sort', insertion_sort),
        ('Merge Sort', merge_sort),
        ('Timsort', lambda x: x.sort())
    ]

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        for order in orders:
            print(f"\nПорядок масиву: {order}")
            arr = generate_array(size, order)
            for name, func in algorithms:
                time = measure_time(func, arr)
                print(f"{name}: {time:.6f} секунд")


if __name__ == "__main__":
    compare_sorts()

    def merge_k_lists(lists):
        heap = []
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], idx, 0))

        result = []
        while heap:
            val, list_idx, element_idx = heapq.heappop(heap)
            result.append(val)
            if element_idx + 1 < len(lists[list_idx]):
                next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
                heapq.heappush(heap, next_tuple)
        return result

    # Приклад використання функції merge_k_lists
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("\nВідсортований список:", merged_list)