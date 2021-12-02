from day2 import read_file, parse_input


def calculate_place_aim(list_of_values):
    aim = 0
    horizontal = 0
    depth = 0

    for item in list_of_values:
        direction, amount = item
        if direction == "forward":
            horizontal += int(amount)
            depth += aim * int(amount)
        elif direction == "up":
            aim -= int(amount)
        elif direction == "down":
            aim += int(amount)

    return horizontal*depth


def main():
    input_content = read_file("input_day2.txt")
    parsed_input = parse_input(input_content)
    final_value = calculate_place_aim(parsed_input)
    print(final_value)


if __name__ == "__main__":
    main()