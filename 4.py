# PART 1
# Identify each pair.
# Check if one part of the pair fully contains the other.
# Get the number of pairs with a section that fully contains the other

with open("4_input.txt") as file:
    pairs_file = file.readlines()

pair_list = []
for dirty_pair in pairs_file:
    pair = []
    for section in dirty_pair.strip().split(","):
        pair.append([int(item) for item in section.split("-")])
    pair_list.append(pair)


fully_overlap = 0
overlap = 0
for pair in pair_list:
    section1 = pair[0]
    section2 = pair[1]

    if section1[0] <= section2[0] and section1[1] >= section2[1]:
        fully_overlap += 1
    elif section1[0] >= section2[0] and section1[1] <= section2[1]:
        fully_overlap += 1
    # PART 2
    # Check if sections pair overlap at all
    elif section1[1] >= section2[0] and section2[1] >= section1[0]:
        overlap += 1


print("Part 1:", fully_overlap)
print("Part 2:", overlap + fully_overlap)
