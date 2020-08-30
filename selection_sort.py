import random_list_generator
import time


def selection_sort(random_list_size):
    random_list = random_list_generator.generate_random_list(random_list_size)
    start = time.time()
    print(f'{random_list}\n')
    for i in range(len(random_list)):
        for j in range(i+1, len(random_list)):
            if random_list[j] < random_list[i]:
                random_list[i], random_list[j] = random_list[j], random_list[i]
    stop = time.time()
    total_time = stop - start
    print(random_list)
    print(f'Done!\nTotal sorting time: {total_time:.2f} seconds')


random_list_size_input = input('Enter number of elements in list: ')
selection_sort(int(random_list_size_input))
