import numpy as np


def fill_area(input_file):
    occupied_positions = np.zeros((1000, 1000))
    with open(input_file, 'r') as read_line:
        for line in read_line:
            id, _, position, size = line.split()
            id = int(id.strip('#'))
            x_position, y_position = position[:-1].split(',')
            x_size, y_size = size.split('x')

            occupied_positions[int(x_position):int(x_position)+int(x_size), int(y_position):int(y_position)+int(y_size)] += 1

        #return np.size(np.where(occupied_positions >= 2)[0])
    # Part 2
    with open(input_file, 'r') as read_line:
    for line in read_line:
        id, _, position, size = line.split()
        id = int(id.strip('#'))
        x_position, y_position = position[:-1].split(',')
        x_size, y_size = size.split('x')

        if np.any(occupied_positions[int(x_position):int(x_position)+int(x_size), int(y_position):int(y_position)+int(y_size)] > 1):
            continue
        else:
            return id



if __name__ == '__main__':
    print(fill_area('input'))
