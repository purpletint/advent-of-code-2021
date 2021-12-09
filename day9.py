from timeit import default_timer as timer


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    return [line.strip() for line in content]


def parse_text(content) -> list:
    return [[int(n) for n in element] for element in content]


def check_for_low_level(value, list_directions) -> bool:
    is_lowest = True
    for element in list_directions:
        if element is None:
            continue
        elif element <= value:
            is_lowest = False
            break
    return is_lowest


def calculate_risk(content) -> int:
    sum_of_risk_levels = 0

    for i, element in enumerate(content):
        for j in range(len(element)):
            value = content[i][j]
            up = None if i == 0 else content[i - 1][j]
            down = None if i == (len(content) - 1) else content[i + 1][j]
            right = None if j == (len(element) - 1) else content[i][j + 1]
            left = None if j == 0 else content[i][j - 1]
            if check_for_low_level(value, [up, down, right, left]):
                sum_of_risk_levels += 1 + content[i][j]
    return sum_of_risk_levels


def main():
    start = timer()
    content = read_file("input_day9.txt")
    parsed_data = parse_text(content)
    print(calculate_risk(parsed_data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
