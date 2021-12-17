def read_file(file_name) -> list[str]:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def parse_input(content):
    input_text = content[0]
    parsed_input = ""

    return parsed_input



def sum_of_versions(content):
    print(content)

def main():
    content = read_file("input_day8.txt")
    parsed_data = parse_input(content)
    print(sum_of_versions(parsed_data))


if __name__ == "__main__":
    main()
