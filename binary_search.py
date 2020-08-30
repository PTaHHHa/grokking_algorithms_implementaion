import time
import random_list_generator


def binary_search(random_list_size, number):
    generated_list = random_list_generator.generate_random_list(random_list_size)
    generated_list.sort()
    first_index, last_index = 0, random_list_size - 1
    counter = 0
    while first_index <= last_index:
        counter += 1
        middle = (last_index + first_index) / 2
        guessing_number = generated_list[int(middle)]
        if guessing_number == number:
            return print(f'Total steps: {counter}'), print(f'Your number was found on {int(middle)} index')
        elif guessing_number > number:
            last_index = int(middle) - 1
        elif guessing_number < number:
            first_index = int(middle) + 1
    print("Seems like your number wasn't found in randomly generated list. Try again!")
    print(f'Total steps: {counter}')


random_list_size_input = input('Enter number of elements in list: ')
number_input = input('Enter number to find in list: ')
start_time = time.time()
binary_search(int(random_list_size_input), int(number_input))
stop_time = time.time()
total_time = stop_time - start_time
print(f'Total time: {total_time:.2f} seconds')
