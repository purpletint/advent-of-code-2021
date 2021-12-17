from timeit import default_timer as timer


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    return [line.strip() for line in content]


def parse_text(content):
    empty_line_index = content.index("")
    dots_list = [(int(n.split(",")[0]), int(n.split(",")[1])) for n in content[:empty_line_index]]
    # for n in content[:empty_line_index]:
    #     dots_list.append(n.split(",")[0], n.split(",")[1])
    folding_instructions = [(n.split()[-1].split("=")[0], int(n.split()[-1].split("=")[1])) for n in content[empty_line_index+1:]]

    return dots_list, folding_instructions


def calculate_first_fold_dots(content):

    dots_list, folding_instructions = content
    print(dots_list)
    print(folding_instructions)
    axis, line = folding_instructions[0][0], folding_instructions[0][1]
    new_dots_diagram = []
    for (x, y) in dots_list:
        if axis == "x":
            # vertical fold
            if x == line:
                continue
            elif x < line:
                print("old", (x,y))
                new_dots_diagram.append((x, y))
            else:
                new_point = (2*line-x, y)
                print(("new",(x,y), new_point))
                new_dots_diagram.append(new_point)

    new_dots_diagram = set(new_dots_diagram)
    how_many_dots = len(new_dots_diagram)
    return how_many_dots


def main():
    start = timer()
    content = read_file("input_day13.txt")
    parsed_data = parse_text(content)
    print(calculate_first_fold_dots(parsed_data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
