import random
import time


def generate_random_list(random_list_size):
    start = time.time()
    print('\nGenerating random list...')
    random_list = [random.randint(1, random_list_size) for i in range(random_list_size)]
    stop = time.time()
    total_time = stop-start
    print(f'Total time to generate list: {total_time:.2f} seconds')
    return random_list
