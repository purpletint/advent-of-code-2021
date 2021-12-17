def read_file(file_name) -> list[str]:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def parse_input(content):
    parsed_input = ""

    return parsed_input


def total_light_flashes(content):
    print(content)

def main():
    content = read_file("input_day11.txt")
    parsed_data = parse_input(content)
    print(total_light_flashes(parsed_data))


if __name__ == "__main__":
    main()