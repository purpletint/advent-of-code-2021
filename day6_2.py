from copy import deepcopy


def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    content = [int(x) for x in clean_list[0].split(",")]
    return content

# def one_la


def lanternfish_create_children(lanternfish_list, days):
    lanternfish_list = []

    if days == 0:
        return lanternfish_list
    else:
        pass



def how_many_lanternfish(content):
    print(content)
    print(len(content))
    content_dict = {}
    for element in content:
        if element not in content_dict:
            content_dict[element] = 1
        else:
            content_dict[element] = content_dict[element] + 1
    print(content_dict)
    whole_sum = 0
    for key, value in content_dict.items():
        content = [key, ]
        for i in range(256):
            print(i)
            additional_list = []
            for n, element in enumerate(content):
                if element > 0:
                    content[n] = element - 1
                elif element == 0:
                    content[n] = 6
                    additional_list.append(8)
            content = content + deepcopy(additional_list)
        whole_sum += len(content) * value
    return whole_sum



    # original_list = deepcopy(content)
    # whole_sum = 0
    # for item in original_list:
    #     content = [item, ]
    #     for i in range(256):
    #         additional_list = []
    #         for n, element in enumerate(content):
    #             if element > 0:
    #                 content[n] = element - 1
    #             elif element == 0:
    #                 content[n] = 6
    #                 additional_list.append(8)
    #         content = content + deepcopy(additional_list)
    #     content_for_one = len(content)
    #     whole_sum += whole_sum
    #     print(whole_sum)



def main():
    content = read_file("input_day6.txt")
    print(how_many_lanternfish(content))


if __name__ == "__main__":
    main()
