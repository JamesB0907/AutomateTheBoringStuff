import random

print('Heads or Tails?')
print('How many times do you want to flip the coin?')
flips = int(input())

def flip_a_coin(flips):
    coins_flipped = []
    for i in range(flips):
        flip_act = random.randint(0, 1)
        if flip_act == 0:
            coins_flipped.append('H')
        elif flip_act == 1:
            coins_flipped.append('T')
    return coins_flipped


def streaks(flips):
    coins_flipped = flip_a_coin(flips)
    print(coins_flipped)
    number_of_streaks = 0
    streak = 0
    for i in range(len(coins_flipped)):
        if coins_flipped[i] == coins_flipped[i - 1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            number_of_streaks += 1
    print('Number of streaks: ' + str(number_of_streaks))

streaks(flips)
