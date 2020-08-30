import random
import time


def generate_random_list(random_list_size):
    start = time.time()
    random_list = []
    print('\nGenerating random list...')
    for i in range(random_list_size):
        random_number = random.randint(1, random_list_size)
        random_list.append(random_number)
    stop = time.time()
    total_time = stop-start
    print(f'Total time to generate list: {total_time:.2f} seconds')
    return random_list
