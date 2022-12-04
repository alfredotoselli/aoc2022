with open("1_input.txt") as file:
    calories_list = file.readlines()

tot_elf_cal_list = []
elf_cal = 0
for calories in calories_list:
    if calories != "\n":
        elf_cal += int(calories.strip())
    else:
        tot_elf_cal_list.append(elf_cal)
        elf_cal = 0

tot_elf_cal_list.sort()
three_most_cal_elf = tot_elf_cal_list[-3:]
print(sum(three_most_cal_elf))
# iterates over rows summing each element
# if element not \n I remove \n and convert the last item to num
# else \n i append the counter and reset the counter
