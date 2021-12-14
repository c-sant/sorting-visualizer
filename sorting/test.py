import random
from time import perf_counter
from typing import Callable, Tuple

def test_sort(
    sorting_algorithm: Callable[[list], list], 
    size: int = 10,
    value_range: Tuple[int, int] = (0, 255)):
    """
    Tests a sorting algorithm in a random array with specified size (default size is 10)
    and within specified range.
    """

    array = random.sample(range(*value_range), size)

    start = perf_counter()

    sorted_array = sorting_algorithm(array)

    end = perf_counter()

    total_time = end - start

    result = {
        'selected_algorithm': sorting_algorithm.__name__,
        'unsorted_array': array,
        'sorted_array': sorted_array,
        'total_time': total_time
    }

    return result