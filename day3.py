from tokenize import group


with open('day3.txt') as f:
    input = f.readlines()

max_elf = 0
current_elf = 0
list_elves = []

def character_value(character):
    if isinstance(character, str) and character.isupper():
        return ord(character) - 64 + 26
    else:
        return ord(character) - 96

total_value = 0
for line in input:
    line_string = line.replace('\n', '')
    first_sack, second_sack = line_string[:int(len(line_string)/2)], line_string[int(len(line_string)/2):]
    first_inventory = {}
    for item in first_sack:
        if item not in first_inventory:
            first_inventory[item] = 1
    for item in second_sack:
        if item in first_inventory:
            total_value += character_value(item)
            break
print('Total value')
print(total_value)
        
#Breaking out into groups of 3
total_value = 0
group_ordering = 0
first_dictionary, second_dictionary = {}, {}
for line in input:
    line_string = line.replace('\n', '')
    for item in line_string:
        if group_ordering == 0:
            first_dictionary[item] = 1
        elif group_ordering == 1: 
            second_dictionary[item] = 1
        elif group_ordering == 2 and item in first_dictionary and item in second_dictionary:
            total_value += character_value(item)
            break
    group_ordering += 1
    # Resetting vars after each group run
    if group_ordering == 3:
        group_ordering = 0
        first_dictionary, second_dictionary = {}, {}
print('total value of the priority of items per group of 3')
print(total_value)