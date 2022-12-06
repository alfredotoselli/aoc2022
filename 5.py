# implement a stack DS and arrange the input on a series of them
# use the common stack methods to move elements as described on the input list

with open("5_input.txt") as file:
    input_list = file.readlines()


def create_stack():
    return []


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


empty_row_index = input_list.index("\n")
containers = input_list[:empty_row_index]
instructions = input_list[empty_row_index + 1 :]


stacks = {}
for index, char in enumerate(containers[-1]):
    if char.isdigit():
        stacks[char] = create_stack()
        for row in reversed(containers[: len(containers) - 1]):
            if row[index] != " ":
                push(stacks[char], row[index])


numeric_commands = []
for instruction in instructions:
    splitted = instruction.strip().split(" ")
    numeric_set = []
    for item in splitted:
        if item.isdigit():
            numeric_set.append(item)
    numeric_commands.append(numeric_set)


def move_crate(stack_from, stack_to):
    crate = pop(stack_from)
    push(stack_to, crate)


# Part 1
for command in numeric_commands:
    for _ in range(int(command[0])):
        move_crate(stacks[command[1]], stacks[command[2]])

# Part 2
for command in numeric_commands:
    tmp_stack = create_stack()
    for _ in range(int(command[0])):
        move_crate(stacks[command[1]], tmp_stack)

    for _ in range(int(command[0])):
        move_crate(tmp_stack, stacks[command[2]])


for stack in stacks.values():
    print(stack[-1], end="")
