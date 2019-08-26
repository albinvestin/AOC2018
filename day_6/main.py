import numpy as np

def get_grid_size(coordinates, boarder):
    # coordinates at form [(x1,y1),(x2,y2),...]
    max_x, min_x = -1,1e10
    max_y, min_y = -1,1e10
    for cord_pair in coordinates:
        if cord_pair[0] < min_x:
            min_x = cord_pair[0]
        if cord_pair[0] > max_x:
            max_x = cord_pair[0]
        if cord_pair[1] < min_y:
            min_y = cord_pair[1]
        if cord_pair[1] > max_y:
            max_y = cord_pair[1]
    return max_x+boarder,min_x+boarder,max_y+boarder,min_y-boarder


def read_file(input_file):
    with open(input_file,'r') as file:
        coordinates = []
        for line in file:
            x_pos, y_pos = line.split(', ')
            coordinates.append([int(x_pos), int(y_pos)])
    return coordinates


def search_positions(size, origin_x, origin_y):
    # Returns the positions
    positions = [[origin_x,origin_y]]
    for i in range(0, size):
        positions.append([origin_x-size+i, origin_y+i])
        positions.append([origin_x+i,origin_y+size-i])
        positions.append([origin_x+size-i,origin_y-i])
        positions.append([origin_x-i,origin_y-size+i])
    return positions


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_closest_location_and_size(locations, current_x, current_y):
    closest_location_and_size = [-1, -1, 1e10]
    count = 1
    for location in locations:
        distance = manhattan_distance(location, [current_x, current_y])
        if distance <= closest_location_and_size[2]:
            if distance == closest_location_and_size[2]:
                count += 1
            else:
                closest_location_and_size = [location[0], location[1], distance]
                count = 1
    if count > 1:
        return [-1, -1, -1]
    else:
        return closest_location_and_size

def fill_grid(grid, grid_size, locations):
    # returns grid with [closest_x, closest_y, closest_length]
    for curr_y in range(grid_size[3], grid_size[2]):
        for curr_x in range(grid_size[1], grid_size[0]):
            grid[curr_x][curr_y] = get_closest_location_and_size(locations,curr_x,curr_y)
    return grid


def count_area(grid, grid_size):
    ids_and_area = []
    for curr_y in range(grid_size[3], grid_size[2]):
        for curr_x in range(grid_size[1], grid_size[0]):
            current_id_x, current_id_y = grid[curr_x][curr_y][0:2]
            append_flag = True
            for index, seen_id in enumerate(ids_and_area):
                if current_id_x != -1:
                    if current_id_x == seen_id[0] and current_id_y == seen_id[1]:
                        ids_and_area[index][2] += 1
                        append_flag = False
                        break
                    else:
                        append_flag = True
                else:
                    append_flag = False
            if append_flag:
                ids_and_area.append([current_id_x, current_id_y, 1])
    return ids_and_area



def get_max_id_and_area(ids_and_area, grid_size):
    max_id_and_area = [-1, -1, -1]

    max_x, min_x, max_y, min_y = grid_size
    for seen_id in ids_and_area:
        if seen_id[0] > min_x and seen_id[0] < max_x  and seen_id[1] < max_y  and seen_id[1] > min_y:
            if seen_id[2] > max_id_and_area[2]:
                max_id_and_area = seen_id
    return max_id_and_area


def get_finite_ids_and_areas(ids_and_area_small, ids_and_area_large):
    # returns finite ids
    finite_ids_and_areas = []
    for seen_id_small in ids_and_area_small:
        for seen_id_large in ids_and_area_large:
            if seen_id_small[0] == seen_id_large[0] and seen_id_small[1] == seen_id_large[1]:
                if seen_id_small[2] < seen_id_large[2]:
                    # It is infinite
                    continue
                else:
                    finite_ids_and_areas.append(seen_id_small)
    return finite_ids_and_areas


if __name__ == '__main__':
    locations = read_file('input')

    # Create two grids and compare which areas increase => infinite
    grid_size_small = get_grid_size(locations, boarder=10)
    grid_small = np.zeros((grid_size_small[0], grid_size_small[2], 3))
    grid_small = fill_grid(grid_small, grid_size_small, locations)

    grid_size_large = get_grid_size(locations, boarder=20)
    grid_large = np.zeros((grid_size_large[0], grid_size_large[2], 3))
    grid_large = fill_grid(grid_large, grid_size_large, locations)

    ids_and_area_small = count_area(grid_small, grid_size_small)
    ids_and_area_large = count_area(grid_large, grid_size_large)

    finite_ids_and_areas = get_finite_ids_and_areas(ids_and_area_small, ids_and_area_large)
    max_area = get_max_id_and_area(finite_ids_and_areas, grid_size_small)

    print(max_area)







