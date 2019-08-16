import parse
import numpy as np


def sort_input(input_file):
    with open(input_file, 'r') as file:
        all_formatted_data = []
        for line in file:
            formatted_data = parse.parse('[{year:d}-{month:d}-{day:d} {hour:d}:{minute:d}] {action}', line)
            year = formatted_data['year']
            month = formatted_data['month']
            day = formatted_data['day']
            hour = formatted_data['hour']
            minute = formatted_data['minute']
            action = formatted_data['action']

            all_formatted_data.append([year, month, day, hour, minute, action])
        all_formatted_data.sort(key=lambda data_line: (data_line[0], data_line[1], data_line[2], data_line[3], data_line[4]))
    return all_formatted_data


def get_most_sleeping_guard(input_file):
    guard_sleep_count = []
    id = -1
    sleep_start = -1
    for line in input_file:
        action = line[5]
        if action.find('#') != -1:
            extract_id = parse.parse('Guard #{id:d}{}', action)
            id = extract_id['id']
            if id not in guard_sleep_count:
                guard_sleep_count.append([id, 0])
        elif is_asleep(action):
            # Falls asleep in this moment
            minute = line[4]
            sleep_start = minute
        else:
            # Woken up
            minute = line[4]
            for guard in guard_sleep_count:
                if id == guard[0]:
                    guard[1] += minute-sleep_start

    return max(guard_sleep_count, key=lambda attribute: attribute[1])


def is_asleep(action):
    return action.find('asleep') != -1


def get_most_slept_minute(input_file, guard_id):
    # Initialize
    slept_minutes = np.zeros(60)
    right_guard = False
    sleep_start = -1

    for line in input_file:
        action = line[5]
        if action.find('#') != -1:
            extract_id = parse.parse('Guard #{id:d}{}', action)
            id = extract_id['id']
            if id == guard_id:
                right_guard = True
            else:
                right_guard = False
            continue
        if right_guard:
            if is_asleep(action):
                minute = line[4]
                sleep_start = minute
            else:
                # Woken up
                minute = line[4]
                slept_minutes[sleep_start:minute] += 1

    return np.argmax(slept_minutes)


if __name__ == '__main__':
    sorted_input = sort_input('input')
    guard_id = get_most_sleeping_guard(sorted_input)
    guard_minutes = get_most_slept_minute(sorted_input, guard_id[0])

    print('Guard ID: {}, Number of minutes slept: {}, Most slept minute: {}'.format(guard_id[0], guard_id[1], guard_minutes))
    print(guard_id[0] * guard_minutes)

