from copy import deepcopy

def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


# oxygen generator rating - if 1 most - stays
# co2scrubber rating - if most 1 - give zero
def oxy_scrub_counter(list_of_values, position, type_name) -> tuple:
    ones_counter = 0
    for line in list_of_values:
        if line[position] == "1":
            ones_counter += 1
    # ones_counter = [x[position] for x in clean_list].count("1")
    print("postition:"+str(position)+"ones_counter"+str(ones_counter)+"zeros"+(str(len(list_of_values)-ones_counter)))
    if type_name == "oxygen":
        value = "1" if ones_counter >= len(list_of_values)/2 else "0"
    elif type_name == "scrubber":
        print(len(list_of_values))
        print(ones_counter)
        value = "0" if ones_counter >= len(list_of_values)/2 else "1"

    return value


def iterate_and_remove(value, position, list_of_values):
    print(value, position)
    list_to_return = []
    for item in list_of_values:
        if item[position] == value:
            # print("item removed: "+str(item[i])+ "whole item"+str(item))
            list_to_return.append(item)
            # print(len(oxy_list))
    print(list_to_return)
    return list_to_return

def calculate_power_consumption(clean_list) -> int:
    oxy_list = deepcopy(clean_list)
    for i in range(len(clean_list[0])):
        # value_for_oxygen, value_for_scrubber = gamma_epsilon_counter(clean_list, i)
        # oxygen = oxygen + value_for_oxygen
        # scrubber = scrubber + value_for_scrubber
        value_for_oxygen = oxy_scrub_counter(oxy_list, i, "oxygen")


        oxy_list = iterate_and_remove(value_for_oxygen, i, oxy_list)
        print(len(oxy_list))
        if len(oxy_list) == 1:
            print("BUM")
            break
        print("len of oxy list"+ str(len(oxy_list)))
    #print(oxy_list)
    scrubber_list = deepcopy(clean_list)
    print(scrubber_list)
    for i in range(len(clean_list[0])):
        # value_for_oxygen, value_for_scrubber = gamma_epsilon_counter(clean_list, i)
        # oxygen = oxygen + value_for_oxygen
        # scrubber = scrubber + value_for_scrubber
        value_for_scrubber = oxy_scrub_counter(scrubber_list, i, "scrubber")

        scrubber_list = iterate_and_remove(value_for_scrubber, i, scrubber_list)
        print(len(scrubber_list))
        if len(scrubber_list) == 1:
            print("BUM")
            break
        print("len of scrubb list" + str(len(scrubber_list)))
    print(scrubber_list)

    # scrubber_list = deepcopy(clean_list)
    # i = 0
    # for element in scrubber:
    #     scrubber_list = iterate_and_remove(element, i, scrubber_list)
    #     print(len(scrubber_list))
    #     if len(scrubber_list) == 1:
    #         print("BUM")
    #         break
    #     i += 1
    #     print("len of scrub list" + str(len(scrubber_list)))

    print(oxy_list)
    print(scrubber_list)

    oxygen_fin = int(oxy_list[0], 2)
    scrubber_fin = int(scrubber_list[0], 2)

    power_calculated = oxygen_fin * scrubber_fin
    return power_calculated


def main():
    content = read_file("input_day3.txt")
    print(calculate_power_consumption(content))


if __name__ == "__main__":
    main()