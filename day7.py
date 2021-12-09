def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    content = [int(x) for x in clean_list[0].split(",")]
    return content


def calculate_position(content):
    content.sort()
    print(content)
    current_best = None
    for i in range(content[0],content[-1]+1):
        current_sum = 0
        for element in content:
            current_sum += abs(element-i)
        if current_best == None:
            current_best = current_sum
        elif current_best > current_sum:
            current_best = current_sum
    return current_best



def main():
    content = read_file("input_day7.txt")
    print(calculate_position(content))


if __name__ == "__main__":
    main()