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
    new_polymers = []
    whole_polymer = deepcopy(current_polymer)
    for n in range(len(whole_polymer) - 1): # separate into twos - NN, NC, CB
        main_pair = whole_polymer[n:n + 2] if n + 2 <= len(whole_polymer) else whole_polymer[n:]

        print(main_pair)
        current_polymer = deepcopy(main_pair)

        # print(current_polymer)
        for i in range(40):
            new_polymer = ""
            for j in range(len(current_polymer) - 1):
                pair = current_polymer[j:j + 2] if j + 2 <= len(current_polymer) else current_polymer[j:]
                if pair in instructions:
                    new_polymer += pair[0] + instructions[pair]
                if j+2 == len(current_polymer):
                    new_polymer += pair[1]
            current_polymer = deepcopy(new_polymer)
            print((len(current_polymer)))

    final_string = ""
    for element in new_polymers:
        if new_polymer.index(element) == 0:
            final_string += element[0]
        final_string += element[1:]
    elements = set(list(final_string))
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

    try: return max_element - min_element
    except: return None


def main():
    start = timer()
    content = read_file("test_inputday14.txt")
    parsed_data = parse_text(content)
    print(between_min_and_max(parsed_data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
