# # Пузырьковый
import time
import random
def bubble(arr):
    n = len(arr)
    for i in  range(n):
        swapped = False

        for j in range(0,n - i -1):

            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True


        if not swapped:
            break




arr = []
for i in range(10000):
    arr.append(random.randint(1,10000))
start_time = time.time()
bubble(arr)
end_time = time.time()
elapsed = end_time - start_time
print(arr)
print(f'Затраченное время: {elapsed:.4f}')


# # Пирамидальный


def heapify(arr, n, i):
    largest = i # Инициализируем корень как самый большой элемент
    left = 2 * i + 1 # левый дочерний элемент
    right = 2 * i + 2 # правый дочерний элемент

    if left < n and arr[left] > arr[largest]:
        largest=left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

    # Перемещаем текущий корень в конец
        heapify(arr, i, 0) # Вызываем heapify на уменьшение кучи

arr = []
for i in range(10000):
    arr.append(random.randint(1,10000))

start_time = time.time()
heap_sort(arr)
end_time = time.time()
elapsed = end_time - start_time


print(arr)
print(f'Затраченное время: {elapsed:.4f}')


# # Метод Шелла
#
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i-inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc*5.0//11)

    return data
data = []
for i in range(10000):
    data.append(random.randint(1,10000))

start_time = time.time()
shell(data)
end_time = time.time()
elapsed = end_time - start_time
print(data)
print(f'Затраченное время: {elapsed:.4f}')

#
# # #Сортировка вставками

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


alist = []

for i in range(1,10000):
    alist.append(random.randint(1,10000))

start_time = time.time()
insertion_sort(alist)
end_time = time.time()
elapsed = end_time - start_time
print(alist)
print(f'Затраченное время: {elapsed:.4f}')
#

# # # БЫстрая сортировка
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = []
for i in range(1,1000000):
    data.append(random.randint(1,1000000))

print("Unsorted Array")
print(data)

size = len(data)
start_time = time.time()
quickSort(data, 0, size - 1)
end_time = time.time()
elapsed = end_time - start_time

print('Sorted Array in Ascending Order:')
print(data)
print(f'Затраченное время: {elapsed:.4f}')


# # Метод слияния
import random
import time
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

nums = []
for i in range(1,10000):
    nums.append(random.randint(1,10000))
start_time = time.time()
merge_sort(nums)
end_time = time.time()
elapsed = end_time - start_time
print(nums)
print(f'Затраченное время: {elapsed:.4f}')