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
            if not number[1]:
                row = False
                break
        if row:
            return True

    for i in range(5):
        column = True
        n = 0
        while column and n < 5:
            if not card[n][i][1]:
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
                new_item = (item[0], True)
                element[element.index(item)] = new_item
    return card


def check_winner_card(card):
    winner_sum = 0
    for element in card:
        for item in element:
            if not item[1]:
                winner_sum += int(item[0])
    return winner_sum


def play_bingo(clean_list):
    numbers = clean_list[0].split(",")
    rest = clean_list[1:]
    table_of_cards = []
    i = 0
    looser_card = []
    looser_number = 0
    while i < len(rest):
        current_card = []
        for n in range(1, 6):
            # rest[i+n].split()
            current_card.append([(x, False) for x in rest[i+n].split()])
        table_of_cards.append(deepcopy(current_card))
        i += 6
    n = 0
    finish = False
    while not finish and n < len(numbers):
        list_to_remove = []
        for i, item in enumerate(table_of_cards):
            marked_card = mark_numbers(numbers[n], item)
            check = bingo_check(marked_card, )
            table_of_cards[i] = marked_card
            if check:
                list_to_remove.append(marked_card)
            if len(table_of_cards) == 1 and bingo_check(table_of_cards[0]):
                looser_card = table_of_cards[0]
                looser_number = numbers[n]
                finish = True
        table_of_cards = [x for x in table_of_cards if x not in list_to_remove]
        n += 1

    looser_card_sum = check_winner_card(looser_card)

    return looser_card_sum*int(looser_number)


def main():
    content = read_file("input_day4.txt")
    print(play_bingo(content))


if __name__ == "__main__":
    main()