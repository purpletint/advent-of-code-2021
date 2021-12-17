from timeit import default_timer as timer
from copy import deepcopy


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    return [line.strip() for line in content]


def parse_text(content):
    empty_line_index = content.index("")
    polymer_template, instructions = content[:empty_line_index], content[empty_line_index+1:]
    # dots_list = [(int(n.split(",")[0]), int(n.split(",")[1])) for n in points]
    # folding_instructions = [(n.split()[-1].split("=")[0], int(n.split()[-1].split("=")[1])) for n in instructions]
    instructions_list = {}
    for element in instructions:
        part, in_between = element.split(" -> ")
        instructions_list[part] = in_between

    return polymer_template[0], instructions_list


def between_min_and_max(content):
    current_polymer, instructions = content
    # print(current_polymer)
    # print(instructions)

    for i in range(10):
        print(i)
        new_polymer = ""
        # print(current_polymer)
        for n in range(len(current_polymer)-1):
            pair = current_polymer[n:n+2] if n+2 <= len(current_polymer) else current_polymer[n:]
            # if pair in instructions:
            #     # print(pair)
            if pair in instructions:
                new_polymer += pair[0] + instructions[pair]
            if n+2 == len(current_polymer):
                new_polymer += pair[1]
        current_polymer = deepcopy(new_polymer)

    elements = set(list(current_polymer))
    min_element = None
    max_element = None
    for item in elements:
        value = current_polymer.count(item)
        if min_element is None:
            min_element = value
            max_element = value
            continue
        if value < min_element:
            min_element = value
        if value > max_element:
            max_element = value

    return max_element - min_element







def main():
    start = timer()
    content = read_file("input_day14.txt")
    parsed_data = parse_text(content)
    print(between_min_and_max(parsed_data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
