with open('day2.txt') as f:
    input = f.readlines()
#A opponent tosses 🪨
#B opponent tosses 📄
#C opponent tosses ✂️
#X you toss 🪨, 1 pt
#Y you toss 📄, 2 pt
#Z you toss ✂️, 3 pt
# Lose = 0 pt, Draw = 3 pt, Win = 6 pt

#Strategy get the win or lost of each and what you play

# returns 0 if you lose and 1 if you win
def play_rps(opponent, you):
    results = {
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3
        }
    }
    return results[opponent][you]

total_pts = 0
for line in input:
    line_string = line.replace('\n', '')
    #Split by space to get the tuple
    rps_tuple = line_string.split(' ')
    total_pts += play_rps(rps_tuple[0], rps_tuple[1])
    if rps_tuple[1] == 'X':
        total_pts += 1
    elif rps_tuple[1] == 'Y':
        total_pts += 2
    else:
        total_pts += 3

print('Total points of playing by the strategy')
print(total_pts) 

# X means lose
# Y means draw
# Z means win

#function to extend first function written without rewriting code of original
def rigged_play_rps(opponent, desired_state):
    results = {
        'A': {
            'DRAW': 'X',
            'WIN': 'Y',
            'LOSE': 'Z'
        },
        'B': {
            'LOSE': 'X',
            'DRAW': 'Y',
            'WIN': 'Z'
        },
        'C': {
            'WIN': 'X',
            'LOSE': 'Y',
            'DRAW': 'Z'
        }
    }
    if desired_state == 'X': #lose
        move = results[opponent]['LOSE']
    elif desired_state == 'Y':
        move = results[opponent]['DRAW']
    else:
        move = results[opponent]['WIN']
    return (play_rps(opponent, move), move)

#Resetting total_pts for next challenge
total_pts = 0
for line in input:
    line_string = line.replace('\n', '')
    #Split by space to get the tuple
    rps_tuple = line_string.split(' ')
    rigged_results = rigged_play_rps(rps_tuple[0], rps_tuple[1])
    total_pts += rigged_results[0]
    if rigged_results[1] == 'X':
        total_pts += 1
    elif rigged_results[1] == 'Y':
        total_pts += 2
    else:
        total_pts += 3

print('Total points of playing by the strategy of having a desired state')
print(total_pts)