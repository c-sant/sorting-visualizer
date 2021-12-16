from sorting import *
from sorting.view import *

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

def main():
    while True:
        opt = input(
            'Choose an option:\n'
            '1) Test algorithms in console.\n'
            '2) Test algorithms in a visual environment.\n'
        ).strip()
        if opt == '1':
            while True:
                try:
                    sample_size = int(input('Insert sample size: ').strip())
                    
                    if sample_size <= 2:
                        print('\nPlease insert a value larger than 2.\n')
                        continue

                    test_all_algorithms(sample_size)
                    return
                except:
                    print('\nPlease insert a valid integer for the sample size.')
        
        elif opt == '2':
            start_visualizer()
            return
        else:
            print('\nPlease choose an option between 1 and 2.\n')
            continue 

if __name__ == '__main__':
    main()
        
        