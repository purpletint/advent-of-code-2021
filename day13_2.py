from timeit import default_timer as timer
from copy import deepcopy


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    return [line.strip() for line in content]


def parse_text(content):
    empty_line_index = content.index("")
    points, instructions = content[:empty_line_index], content[empty_line_index+1:]
    dots_list = [(int(n.split(",")[0]), int(n.split(",")[1])) for n in points]
    folding_instructions = [(n.split()[-1].split("=")[0], int(n.split()[-1].split("=")[1])) for n in instructions]

    return dots_list, folding_instructions


def draw_code(dots):
    dots_list = list(dots)
    dots_list.sort()
    whole_picture = []
    x_ord = max([m for (m, n) in dots_list])
    y_ord = max([n for (m, n) in dots_list])
    for y in range(y_ord+1):
        current_line = ""
        for x in range(x_ord+1):
            if (x,y) in dots_list:
                current_line += "#"
            else:
                current_line += "."
        whole_picture.append(deepcopy(current_line))
    return whole_picture


def calculate_first_fold_dots(content):
    dots_list, folding_instructions = content

    for item in folding_instructions:
        new_dots_diagram = []
        axis, line = item[0], item[1]
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
            elif axis == "y":
                # horizontal fold
                if y == line:
                    continue
                elif y < line:
                    print("old", (x,y))
                    new_dots_diagram.append((x, y))
                else:
                    new_point = (x, 2*line - y)
                    print(("new",(x,y), new_point))
                    new_dots_diagram.append(new_point)
        new_dots_diagram = set(new_dots_diagram)
        dots_list = deepcopy(new_dots_diagram)

    # new_dots_diagram = set(dots_list)
    drawn_diagram = draw_code(dots_list)
    # how_many_dots = len(new_dots_diagram)
    for element in drawn_diagram:
        print(element)


def main():
    start = timer()
    content = read_file("input_day13.txt")
    parsed_data = parse_text(content)
    print(calculate_first_fold_dots(parsed_data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
