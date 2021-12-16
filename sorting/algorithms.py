#################
# Aux Functions #
#################

# Merge (Merge Sort)

def _merge(
    array: list, 
    start: int, 
    mid: int, 
    end: int):
    """
    Auxiliary function to merge and sort two arrays.
    """
    temp = []

    i, j = start, mid + 1

    while (i <= mid) and (j <= end):
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1
    
    while j <= end:
        temp.append(array[j])
        j += 1

    for k in range(len(temp)):
        array[start + k] = temp[k]

# Partition (Quick Sort)

def _partition(array, start, end):
    """
    Auxiliary function to get pivot index.
    """
    pivot = array[end]

    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[end] = array[end], array[i + 1]

    return i + 1

######################
# Sorting Algorithms #
######################

# Bubble Sort

def bubble_sort(
    array: list, 
    inplace: bool = False):
    """
    A sorting algorithm that loops through an unsorted array, comparing each element
    with it's adjacent and swaping them if they are in the wrong order. This process
    is repeated until the array is completely sorted.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
    if not inplace:
        return array

# Insertion Sort

def insertion_sort(
    array: list, 
    inplace: bool = False):
    """
    A sorting algorithm that organizes values in an array one at a time. It loops
    through the inserted array until it finds a value in a wrong position. Then,
    it shifts the value's position until it fits. The process is repeated until
    every value is in it's place.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for j in range(1, n):
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

    if not inplace:
        return array

# Selection Sort

def selection_sort(
    array: list,
    inplace: bool = False):
    """
    A comparison sorting algorithm which sorts a given array by moving it's
    smallest values to the beggining one at a time.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for i in range(n):
        smallest_value = array[i]
        smallest_index = i
        for j in range(i, n):
            if array[j] < smallest_value:
                smallest_value = array[j]
                smallest_index = j
        
        array[smallest_index], array[i] = array[i], array[smallest_index]

    if not inplace:
        return array

# Merge Sort

def merge_sort(
    array: list,
    start: int = 0,
    end: int = None,
    inplace: bool = False):
    """
    A "divide and conquer" sorting algorithm that divides the input array into two
    and applies itself in each of them to sort them before merging them together 
    afterwards.
    """

    if not inplace:
        array = array.copy()

    if end == None:
        end = len(array) - 1

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(array, start, mid, True)
        merge_sort(array, mid + 1, end, True)

        _merge(array, start, mid, end)

    if not inplace:
        return array

# Quick Sort

def quick_sort(
    array: list,
    start: int = 0,
    end: int = None,
    inplace: bool = False):
    """
    A "divide and conquer" algorithm based on picking an element 
    as pivot and dividing a given array based on it.
    """

    if not inplace:
        array = array.copy()

    if end == None:
        end = len(array) - 1

    if start < end:
        p = _partition(array, start, end)

        quick_sort(array, start, p - 1, True)
        quick_sort(array, p + 1, end, True)

    if not inplace:
        return array