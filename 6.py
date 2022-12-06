# PART 1: get the index+1 of the last char of first 4 different chars

with open("6_input.txt") as file:
    datastream = file.readlines()[0]


def scanner(start, end):
    if len(datastream[start:end]) == len(set(datastream[start:end])):
        return end


# Part 1
def find_start_of_packet(datastream):
    for index in range(len(datastream)):
        result = scanner(index, index + 4)

        if result:
            return result


# Part 2
def find_start_of_message(datastream):
    for index in range(len(datastream)):
        result = scanner(index, index + 14)
        if result:
            return result


print(find_start_of_packet(datastream))
print(find_start_of_message(datastream))


# PART 1: get the index+1 of the last char of first 4 different chars
