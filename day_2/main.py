import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_check_sum('test_input'), 1)


def get_check_sum(input_file):
    sum_of_two = 0
    sum_of_three = 0
    with open(input_file, 'r') as read_input:
        for line in read_input:
            sum_of_two += check_appearance(line, 2)
            sum_of_three += check_appearance(line, 3)
        return sum_of_two * sum_of_three


def check_appearance(line, appearance_number):
    seen_characters = []
    for character in line:
        seen_characters.append(character)
    for character in seen_characters:
        if sum(1 for char in seen_characters if char == character) == appearance_number:
            return 1
    return 0


def find_matching_ids(input_file):
    seen_ids = []
    with open(input_file, 'r') as read_input:
        for line in read_input:
            seen_ids.append(line)

        for left_id in seen_ids:
            for right_id in seen_ids:
                if left_id is right_id:
                    continue
                else:
                    if valid_match(left_id, right_id):
                        return left_id, right_id


def valid_match(left_id, right_id):
    character_misses = 0

    for left_char, right_char in zip(left_id, right_id):
        if left_char == right_char:
            continue
        else:
            character_misses += 1
    if character_misses < 2:
        return True
    else:
        return False



if __name__ == '__main__':
    #unittest.main()
    #print(get_check_sum('input'))
    print(find_matching_ids('input'))