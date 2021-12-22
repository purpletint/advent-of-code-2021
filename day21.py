from copy import deepcopy
def decide_on_values(i):
    values_to_add = sum([i % 100 + 1, (i + 1) % 100 + 1, (i + 2) % 100 + 1])
    j = i + 3
    return values_to_add, j


def count_position(player1, player2):
    player1_score = 0
    player2_score = 0
    i = 0
    dice_roll = 0
    while True:
        # dice = [x for x in range(1, 101)]
        # print(dice)
        # for player1
        to_add, j = decide_on_values(i)
        dice_roll += 3
        player1_score += ((to_add % 10 + player1 - 1) % 10) + 1
        player1 = ((to_add % 10 + player1 - 1) % 10) + 1

        if player1_score >= 1000:
            return dice_roll * player2_score
        i = deepcopy(j)
        to_add, k = decide_on_values(i)
        dice_roll += 3
        player2_score += ((to_add % 10 + player2 - 1) % 10) + 1
        player2 = ((to_add % 10 + player2 - 1) % 10) + 1

        if player2_score >= 1000:
            return dice_roll * player1_score
        i = deepcopy(k)

def main():
    player1 = 6
    player2 = 7
    print(count_position(6,7))


if __name__ == "__main__":
    main()