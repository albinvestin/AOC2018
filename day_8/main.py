
def read_file(input):
    with open(input, 'r') as file:
        for line in file:
            sequence = list(map(int, line.split(' ')))
    return sequence


class Node:
    def __init__(self, no_children, meta_data_length):
        self.no_children = no_children
        self.meta_data_length = meta_data_length


def get_sum_meta_data_iterative(sequence):
    # Initialize
    sum_meta_data = 0
    stored_nodes = []
    pop_stored_flag = False

    # Calculate three
    while len(sequence) > 0 or len(stored_nodes) > 0:
        if pop_stored_flag:
            node = stored_nodes.pop()
            no_children = node.no_children - 1
            meta_data_length = node.meta_data_length
        else:
            no_children = sequence.pop(0)
            meta_data_length = sequence.pop(0)

        if no_children == 0:
            sum_meta_data += sum([sequence.pop(0) for i in range(meta_data_length)])
            pop_stored_flag = True
        else:
            pop_stored_flag = False
            stored_nodes.append(Node(no_children, meta_data_length))

    return sum_meta_data


if __name__ == '__main__':
    sequence = read_file('input')
    sum_meta_data = get_sum_meta_data_iterative(sequence)
    print(sum_meta_data)