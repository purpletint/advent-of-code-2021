from copy import deepcopy


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    content = [int(x) for x in clean_list[0].split(",")]
    return content

def one_la


def lanternfish_create_children(lanternfish_list, days):
    lanternfish_list

    if days == 0:
        return lanternfish_list
    else:



def how_many_lanternfish(content):
    print(content)
    print(len(content))

    for i in range(80):
        additional_list = []
        for n, element in enumerate(content):
            if element > 0:
                content[n] = element - 1
            elif element == 0:
                content[n] = 6
                additional_list.append(8)
        content = content + deepcopy(additional_list)

    return(len(content))



def main():
    content = read_file("input_day6.txt")
    print(how_many_lanternfish(content))


if __name__ == "__main__":
    main()
