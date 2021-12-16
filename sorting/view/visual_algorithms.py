from tkinter import Canvas, Tk
from tkinter.constants import TRUE
from .render import render_array
from time import sleep

##########
# Colors #
##########

RED = '#d80000'
YELLOW = '#fbff00'
WHITE = '#ffffff'
PURPLE = '#5800ca'

######################
# Sorting Algorithms #
######################

# Bubble Sort

def bubble_sort(window: Tk, canva: Canvas, array: list, speed: float) -> None:
    """
    Visualization of Bubble Sort algorithm.
    """

    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - 1 - i):
            colors = [WHITE if k != j else RED for k in range(len(array))]

            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
                
                colors = [WHITE if k not in (j, j + 1) else YELLOW for k in range(len(array))]
            
            render_array(window, canva, array, colors, speed)
        
        if not swapped:
            break

# Insertion Sort

def insertion_sort(window: Tk, canva: Canvas, array: list, speed: float) -> None:
    """
    Visualization of Insertion Sort algorithm.
    """

    n = len(array)

    for j in range(1, n):
        colors = [WHITE if k != j else RED for k in range(n)]

        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

            colors = [WHITE if k not in (j, j - 1) else YELLOW for k in range(n)]
            render_array(window, canva, array, colors, speed)
        
        render_array(window, canva, array, colors, speed)

# Selection Sort

def selection_sort(window: Tk, canva: Canvas, array: list, speed: float) -> None:
    """
    Visualization of Selection Sort algorithm.
    """

    n = len(array)

    for i in range(n):
        smallest_value = array[i]
        smallest_index = i
        for j in range(i, n):
            if array[j] < smallest_value:
                smallest_value = array[j]
                smallest_index = j

            colors = [WHITE if k not in (j, smallest_index) else (RED if k == j else PURPLE) for k in range(n)]
            render_array(window, canva, array, colors, speed)
        
        if smallest_index != i:
            array[smallest_index], array[i] = array[i], array[smallest_index]
            colors = [WHITE if k not in (i, smallest_index) else YELLOW for k in range(n)]
            render_array(window, canva, array, colors, speed)
            
# Merge Sort

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

def merge_sort(window: Tk, canva: Canvas, array: list, speed: float, start: int = 0, end: int = None):
    """
    Visualization of the Merge Sort algorithm.
    """

    if end == None:
        end = len(array) - 1

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(window, canva, array, speed, start, mid)
        merge_sort(window, canva, array, speed, mid + 1, end)

        _merge(array, start, mid, end)

        colors = [WHITE if (x < start) or (x > end) else (RED if x in (start, end) else YELLOW) for x in range(len(array))]
        render_array(window, canva, array, colors, speed)

# Quick Sort

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

def quick_sort(window: Tk, canva: Canvas, array: list, speed: float, start: int = 0, end: int = None):
    """
    Visualization of the Quick Sort algorithm
    """

    if end == None:
        end = len(array) - 1

    if start < end:
        p = _partition(array, start, end)

        quick_sort(window, canva, array, speed, start, p - 1)
        quick_sort(window, canva, array, speed, p + 1, end)

        colors = [WHITE if (x < start) or (x > end) else (RED if x in (start, end) else YELLOW) for x in range(len(array))]
        render_array(window, canva, array, colors, speed)