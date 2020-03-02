import numpy as np

x = np.array([-1, 2, 3, 4])


def process_table(number):
    count = 1
    count += 1
    return np.abs(number)


def add_to_table(number):
    count = 1
    number.append(count)


add_to_table(x)
process_table(x)
