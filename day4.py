with open('day4.txt') as f:
    input = f.readlines()

def process_task(task):
    task_range = task.split('-')
    lower_bd, upper_bd = task_range[0], task_range[1]
    return (int(lower_bd), int(upper_bd))

total_value = 0
for line in input:
    line_string = line.replace('\n', '')
    assignments = line_string.split(',')
    first_bds, second_bds = process_task(assignments[0]), process_task(assignments[1])
    if (first_bds[0] >= second_bds[0] and first_bds[1] <= second_bds[1]) or (second_bds[0] >= first_bds[0] and second_bds[1] <= first_bds[1]):
        total_value += 1

print('total encapulated')
print(total_value)

total_value = 0
for line in input:
    line_string = line.replace('\n', '')
    assignments = line_string.split(',')
    first_bds, second_bds = process_task(assignments[0]), process_task(assignments[1])
    if ((first_bds[0] >= second_bds[0] and first_bds[0] <= second_bds[1]) or
        (second_bds[0] >= first_bds[0] and second_bds[0] <= first_bds[1])):
        total_value += 1

print('any overlap')
print(total_value)