import string

with open("3_input.txt") as file:
    rucksacks_file = file.readlines()

# split rucksack string in two comp
# verify if exist an equal letter (case sensitive) on the compartment, put it in a list of error_items
# get the priority value of each error item and sum them

priority_values = {}

priority_counter = 1
for letter in string.ascii_lowercase:
    priority_values[letter] = priority_counter
    priority_counter += 1

priority_counter = 27
for letter in string.ascii_uppercase:
    priority_values[letter] = priority_counter
    priority_counter += 1


error_items = []
for rucksack_dirty in rucksacks_file:
    rucksack = rucksack_dirty.strip()
    comp_divider = int(len(rucksack) / 2)
    comp_1 = rucksack[:comp_divider]
    comp_2 = rucksack[comp_divider:]
    for item1 in comp_1:
        if item1 in comp_2:
            error_items.append(item1)
            break


def get_tot_value(items):
    tot_priority_value = 0
    for item in items:
        tot_priority_value += priority_values[item]
    return tot_priority_value


print("Part 1:", get_tot_value(error_items))

# PART 2

# divide the input in groups of 3 rucksack
# find the common item for each group
# sum the priority value of each gropu badge

rucksack_groups = []

counter = 1
group = []
for item in rucksacks_file:
    group.append(item.strip())
    if counter % 3 == 0:
        rucksack_groups.append(group)
        group = []

    counter += 1


badges = []
for indexgroup, group in enumerate(rucksack_groups):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badges.append(item)
            break

print("Part 2:", get_tot_value(badges))
