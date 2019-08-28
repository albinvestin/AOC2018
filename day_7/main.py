from string import ascii_lowercase


def read_file(file):
    dependencies = []
    with open(file,'r') as read_lines:
        for line in read_lines:
            dependency_step = line[5]
            _, current_step = line.split('step ')
            current_step = current_step[0]
            dependencies.append([dependency_step, current_step])
    return dependencies


class Node:
    def __init__(self, name, prev_dep, next_dep):
        self.name = name
        self.prev_dep = prev_dep
        self.next_dep = next_dep


def generate_nodes(connections):
    available_nodes = []
    for connection in connections:
        append_left, append_right = True, True
        for node in available_nodes:
            if node.name == connection[0]:
                node.next_dep.append(connection[1])
                append_left = False
            elif node.name == connection[1]:
                node.prev_dep.append(connection[0])
                append_right = False
        if append_left:
            available_nodes.append(Node(connection[0], [], [connection[1]]))
        if append_right:
            available_nodes.append(Node(connection[1], [connection[0]], []))
    return available_nodes


def get_build_order(available_nodes, completed_nodes):
    build_order = ''
    while len(completed_nodes) < len(available_nodes):
        executable_nodes = get_executable_nodes(available_nodes, completed_nodes)
        build_order += executable_nodes[0]
        completed_nodes.append(executable_nodes[0])
    return build_order


def any_previous_dependencies(current_node, completed_nodes):
    # returns False if any previous dependency is not completed
    return all(dependency in completed_nodes for dependency in current_node.prev_dep)


# Part 2
def get_execution_time(letter):
    # Create dictionary with letter and number
    LETTERS = {letter : value for value, letter in enumerate(ascii_lowercase, start=1)}
    return LETTERS[letter.lower()] + 60


class Worker:
    task = ''
    start_time = 0
    work_length = 0

    def is_idle(self):
        return self.task == ''

    def new_task(self, task, start_time, work_length):
        self.task = task
        self.start_time = start_time
        self.work_length = work_length

    def finish_task(self, time):
        if time == self.start_time+self.work_length:
            finished_task = self.task
            self.task = ''
            return finished_task
        else:
            return ''


def get_executable_nodes(available_nodes, completed_nodes):
    executable_nodes = []
    for node in available_nodes:
        if node.name not in completed_nodes:
            if len(node.prev_dep) == 0 or any_previous_dependencies(node, completed_nodes):
                executable_nodes.append(node.name)
    executable_nodes.sort()
    return executable_nodes



def get_completion_time(available_nodes, no_workers):
    # Initiate
    time = 0
    completed_nodes = []
    completion_timers = []
    in_progress = []
    workers = [Worker() for i in range(no_workers)]

    while len(available_nodes) > len(completed_nodes):
        # Check what is done at current time and set workers to idle
        finished_timers = [index for index, value in enumerate(completion_timers) if value == time]
        if finished_timers:
            finished_task = ''.join(worker.finish_task(time) for worker in workers)
            for task in finished_task:
                completed_nodes.append(task)
                in_progress.remove(task)

        executable_nodes = get_executable_nodes(available_nodes, completed_nodes)
        executable_nodes = [node for node in executable_nodes if node not in in_progress]
        for node_name in executable_nodes:
            for worker in workers:
                if worker.is_idle():
                    execution_time = get_execution_time(node_name)
                    worker.new_task(node_name, time, execution_time)
                    completion_timers.append(time+execution_time)
                    in_progress.append(node_name)
                    # Next node
                    break

        time += 1
    return time - 1


if __name__ == '__main__':
    connections = read_file('input')
    available_nodes = generate_nodes(connections)
    build_order = get_build_order(available_nodes, completed_nodes=[])
    print(build_order)

    # Part 2
    completion_time = get_completion_time(available_nodes, no_workers=5)
    print(completion_time)



