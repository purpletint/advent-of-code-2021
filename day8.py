def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def parse_input(content):
    only_endings = []
    for element in content:
        elements = element.split(" | ")[1].split()
        only_endings += [len(x) for x in elements]
    return only_endings


def seven_segment_display_calculation(content):
    print(content)
    correct_values = [2, 4, 3, 7]
    counter = 0
    for element in content:
        for item in element:
            if len(item) in correct_values:
                counter += 1
    return counter



def main():
    content = read_file("input_day8.txt")
    parsed_data = parse_input(content)
    print(seven_segment_display_calculation(parsed_data))


if __name__ == "__main__":
    main()