def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def parse_data(clean_list):
    parsed_data = []
    for element in clean_list:
        x1, y1 = element.split(" -> ")[0].split(",")
        x2, y2 = element.split(" -> ")[1].split(",")
        parsed_data.append(({"x1": int(x1), "y1": int(y1), "x2": int(x2), "y2": int(y2)}))
    return parsed_data


def clean_data_only_horizontal_vertical(parsed_data):
    only_hor_vert = []
    only_diag = []
    for element in parsed_data:
        if element["x1"] == element["x2"]:
            only_hor_vert.append([element, "x"])
        elif element["y1"] == element["y2"]:
            only_hor_vert.append([element, "y"])
        else:
            only_diag.append(element)

    return only_hor_vert, only_diag


def calculate_lines(only_h_v, only_diag):
    print(only_h_v)
    lines_marked = {}
    for element in only_h_v:
        direction = element[1]
        coordinates = element[0]
        x1 = coordinates["x1"]
        x2 = coordinates["x2"]
        y1 = coordinates["y1"]
        y2 = coordinates["y2"]
        if direction == "x":
            # print(coordinates)
            if y1 > y2:
                for i in range(y2, y1+1):
                    lines_marked[(x1, i)] = lines_marked.get((x1, i), 0) + 1
                    # print(lines_marked)
            else:
                for i in range(y1, y2+1):
                    # print(x1, i)
                    lines_marked[(x1, i)] = lines_marked.get((x1, i), 0) + 1
                    # print(lines_marked)
        else:
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    lines_marked[(i, y1)] = lines_marked.get((i, y1), 0) + 1
                    # print(lines_marked)
            else:
                for i in range(x1, x2 + 1):
                    lines_marked[(i, y1)] = lines_marked.get((i, y1), 0) + 1
                    # print(lines_marked)
    for element in only_diag:
        coordinates = element
        x1 = coordinates["x1"]
        x2 = coordinates["x2"]
        y1 = coordinates["y1"]
        y2 = coordinates["y2"]
        dif = abs(x1 - x2) - 1
        lines_marked[(x2, y2)] = lines_marked.get((x2, y2), 0) + 1
        lines_marked[(x1, y1)] = lines_marked.get((x1, y1), 0) + 1
        if x1 > x2 and y1 > y2:
            for i in range(dif):
                x2 += 1
                y2 += 1
                lines_marked[(x2, y2)] = lines_marked.get((x2, y2), 0) + 1
        elif x1 > x2 and y1 < y2:
            for i in range(dif):
                x2 += 1
                y2 -= 1
                lines_marked[(x2, y2)] = lines_marked.get((x2, y2), 0) + 1
        elif x1 < x2 and y1 > y2:
            for i in range(dif):
                x2 -= 1
                y2 += 1
                lines_marked[(x2, y2)] = lines_marked.get((x2, y2), 0) + 1
        elif x1 < x2 and y1 < y2:
            for i in range(dif):
                x2 -= 1
                y2 -= 1
                lines_marked[(x2, y2)] = lines_marked.get((x2, y2), 0) + 1

    # print(lines_marked)
    counter = 0
    for key, value in lines_marked.items():
        if value >= 2: counter +=1
    return counter


def main():
    content = read_file("input_day5.txt")
    parsed_content = parse_data(content)
    only_h_v, only_diag = clean_data_only_horizontal_vertical(parsed_content)
    print(calculate_lines(only_h_v, only_diag))


if __name__ == "__main__":
    main()