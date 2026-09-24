import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr
    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def count_time(fun, arr):
    arr = arr.copy()
    start = time.perf_counter()
    fun(arr)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed


sizes = [10_000, 50_000, 100_000, 500_000]

n = 5
random_results = []
deterministic_results = []

for size in sizes:
    int_array = [random.randint(0, size+1) for _ in range(size)]
    random_times = []
    deterministic_times = []
    for _ in range(n):
        time_random = count_time(randomized_quick_sort, int_array)
        random_times.append(time_random)
        time_deterministic = count_time(deterministic_quick_sort, int_array)
        deterministic_times.append(time_deterministic)
    average_random_time = sum(random_times) / n
    random_results.append(average_random_time)
    average_deterministic_time = sum(deterministic_times) / n
    deterministic_results.append(average_deterministic_time)

print("\nРезультати:")
print("-" * 60)
print(f"{'Розмір':<15}{'Randomized':<20}{'Deterministic':<20}")
print("-" * 60)

for i in range(len(sizes)):
    print(
        f"{sizes[i]:<15}"
        f"{random_results[i]:<20.4f}"
        f"{deterministic_results[i]:<20.4f}"
    )

fig = plt.figure("QuickSort comparison")
plt.plot(sizes, random_results, label="Рандомізований QuickSort")
plt.plot(sizes, deterministic_results, label="Детермінований QuickSort")

plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid()
plt.show()