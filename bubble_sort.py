import random_list_generator
import time


def bubble_sort(random_list_size):
    random_list = random_list_generator.generate_random_list(random_list_size)
    print(random_list)
    swapped = True
    print('Sorting start\n')
    start = time.time()
    while swapped:
        swapped = False
        for i in range(len(random_list)-1):
            if random_list[i] > random_list[i + 1]:
                random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
                swapped = True
    stop = time.time()
    total_time = stop - start
    print(random_list)
    print(f'Done!\nTotal sorting time: {total_time:.2f} seconds')


random_list_size_input = input('Enter number of elements in list: ')
bubble_sort(int(random_list_size_input))
