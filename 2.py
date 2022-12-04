# YES, UGLY

rock = ["A", "X"]
paper = ["B", "Y"]
scissor = ["C", "Z"]
rock_value = 1
paper_value = 2
scissor_value = 3
lost = 0
draw = 3
win = 6

with open("2_input.txt") as file:
    strategy = file.readlines()


def my_score_part_one(opponent, me):
    opponent = opponent.strip()
    me = me.strip()

    if me == rock[1]:
        if opponent == rock[0]:
            return draw + rock_value
        if opponent == paper[0]:
            return lost + rock_value
        if opponent == scissor[0]:
            return win + rock_value
    if me == paper[1]:
        if opponent == rock[0]:
            return win + paper_value
        if opponent == paper[0]:
            return draw + paper_value
        if opponent == scissor[0]:
            return lost + paper_value
    if me == scissor[1]:
        if opponent == rock[0]:
            return lost + scissor_value
        if opponent == paper[0]:
            return win + scissor_value
        if opponent == scissor[0]:
            return draw + scissor_value


to_lost = "X"
to_draw = "Y"
to_win = "Z"


def my_score_part_two(opponent, me):
    opponent = opponent.strip()
    me = me.strip()

    if opponent == rock[0]:
        if me == to_lost:
            return lost + scissor_value
        if me == to_draw:
            return draw + rock_value
        if me == to_win:
            return win + paper_value
    if opponent == paper[0]:
        if me == to_lost:
            return lost + rock_value
        if me == to_draw:
            return draw + paper_value
        if me == to_win:
            return win + scissor_value
    if opponent == scissor[0]:
        if me == to_lost:
            return lost + paper_value
        if me == to_draw:
            return draw + scissor_value
        if me == to_win:
            return win + rock_value


my_total_score_part_one = 0
my_total_score_part_two = 0

for match in strategy:
    my_total_score_part_one += my_score_part_one(match[0], match[2])
    my_total_score_part_two += my_score_part_two(match[0], match[2])

print(my_total_score_part_one)
print(my_total_score_part_two)
