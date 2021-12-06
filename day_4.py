from copy import deepcopy

def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def bingo_check(card):
    for item in card:
        row = True
        for number in item:
            if number[1] == "n":
                row = False
                break
        if row:
            return True
    print(card)

    for i in range(5):
        column = True
        n = 0
        while column and n < 5:
            print(card[n][i])
            if card[n][i][1] == "n":
                print("make false")
                column = False
                break
            n += 1
        if column:
            return True


    return False


def mark_numbers(number, card):
    for element in card:  # card == [[],[],[],[],[]]   element = [(),(),(),(),()]
        for item in element:  # item == ()
            if item[0] == number:
                new_item = (item[0], "y")
                element[element.index(item)] = new_item
    return card


def check_winner_card(card):
    winner_sum = 0
    for element in card:
        for item in element:
            if item[1] == "n":
                winner_sum += int(item[0])
    return winner_sum


def play_bingo(clean_list):
    print(clean_list)
    numbers = clean_list[0].split(",")
    print(numbers)
    rest = clean_list[1:]
    table_of_cards = []
    i = 0
    winner_card = ""
    winner_sum = 0
    winner_number = 0
    while i < len(rest):
        current_card = []
        for n in range(1, 6):
            # rest[i+n].split()
            current_card.append([(x, "n") for x in rest[i+n].split()])
        table_of_cards.append(deepcopy(current_card))
        i += 6

    n = 0
    finish = False
    while not finish and n < len(numbers):
        for i, item in enumerate(table_of_cards):
            marked_card = mark_numbers(numbers[n], item)
            check = bingo_check(marked_card)
            table_of_cards[i] = marked_card
            if not check:
                continue
            elif check:
                winner_card = marked_card
                winner_number = numbers[n]
                finish = True
                break
        n += 1

    winner_sum = check_winner_card(winner_card)

    return winner_sum*int(winner_number)



def main():
    content = read_file("input_day4.txt")
    print(play_bingo(content))


if __name__ == "__main__":
    main()