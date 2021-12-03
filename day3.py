def read_file(file_name) -> list:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def gamma_epsilon_counter(clean_list, position) -> tuple:
    # ones_counter = 0
    # for line in clean_list:
    #     if line[position] == "1":
    #         ones_counter += 1
    ones_counter = [x[position] for x in clean_list].count("1")

    gamma_epsilon_for_position = ("1", "0") if ones_counter > len(clean_list) - ones_counter else ("0", "1")
    return gamma_epsilon_for_position


def calculate_power_consumption(clean_list) -> int:
    gamma = ""
    epsilon = ""

    for i in range(len(clean_list[0])):
        value_for_gamma, value_for_epsilon = gamma_epsilon_counter(clean_list, i)
        gamma = gamma + value_for_gamma
        epsilon = epsilon + value_for_epsilon

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    power_calculated = gamma * epsilon
    return power_calculated


def main():
    content = read_file("input_day3.txt")
    print(calculate_power_consumption(content))


if __name__ == "__main__":
    main()
