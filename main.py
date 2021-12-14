from sorting import *

def test_all_algorithms(sample_size: int = 100):
    """
    Tests each of the sorting algorithms and prints how much time each one of
    them took. Arrays have randomized order of numbers from 0 to specified size.
    """

    # tested algorithms
    algorithms = [ bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort ]

    # expected result - sorting is ok if the final result is this everytime
    expected_result = [*range(sample_size)]

    # tests
    for algorithm in algorithms:
        time = []
        success = True

        for i in range(10):
            attempt = test_sort(algorithm, sample_size, (0, sample_size))

            if attempt['sorted_array'] != expected_result:
                print(
                    f"[Average time: no data] {attempt['selected_algorithm']}: ERROR\n\n"
                    "input:\n"
                    f"{attempt['unsorted_array']}\n"
                    "result:\n"
                    f"{attempt['sorted_array']}"
                )

                success = False
                break
            
            time.append(attempt['total_time'])
        
        if success:
            print(f'[Average time: {(sum(time) / len(time)):.2f}s] {algorithm.__name__}: OK')
        else:
            break

if __name__ == '__main__':
    test_all_algorithms(2500)