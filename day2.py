def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        return f.readlines()


def parse_input(content) -> list:
    list_of_values = []
    for line in content:
        line = line.strip()
        direction, amount = line.split()
        list_of_values.append((direction, amount))
    return list_of_values


def calculate_place(list_of_values) -> int:
    horizontal = 0
    depth = 0

    for item in list_of_values:
        direction, amount = item
        if direction == "forward":
            horizontal += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)

    return horizontal*depth


def main():
    input_content = read_file("input_day2.txt")
    parsed_input = parse_input(input_content)
    final_value = calculate_place(parsed_input)
    print(final_value)


if __name__ == "__main__":
    main()

