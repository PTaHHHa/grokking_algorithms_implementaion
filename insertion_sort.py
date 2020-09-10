import random_list_generator
import time


def insertion_sort(random_list_size):
    random_list = random_list_generator.generate_random_list(random_list_size)
    start = time.time()
    print(f'{random_list}')
    print('Sorting start\n')
    for i in range(1, len(random_list)):
        j = i - 1
        key = random_list[i]
        while random_list[j] > key and j >= 0:
            random_list[j + 1] = random_list[j]
            j -= 1
        random_list[j + 1] = key
    stop = time.time()
    total_time = stop - start
    print(random_list)
    print(f'Done!\nTotal sorting time: {total_time:.2f} seconds')


random_list_size_input = input('Enter number of elements in list: ')
insertion_sort(int(random_list_size_input))


