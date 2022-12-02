import heapq

with open('day1.txt') as f:
    input = f.readlines()

max_elf = 0
current_elf = 0
list_elves = []
for line in input:
    line_string = line.replace('\n', '')
    if line_string:
        current_elf += int(line_string)
        if current_elf > max_elf:
            max_elf = current_elf
    else:
        list_elves.append(current_elf)
        current_elf = 0
list_elves.append(current_elf)
print('max elf calories')
print(max_elf)

print('max three elf calories')
print(sum(heapq.nlargest(3, list_elves)))