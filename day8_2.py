segments_on_display = 'abcdefg'


def read_file(file_name) -> list[str]:
    with open(file_name, "r") as f:
        content = f.readlines()
    clean_list = [line.strip() for line in content]
    return clean_list


def parse_input(content) -> list[tuple]:
    all_content = []
    for element in content:
        templates_list, values_list = element.split(" | ")
        templates = [x for x in templates_list.split()]
        values = [x for x in values_list.split()]
        all_content.append((templates, values))
    return all_content


def count_occurrence(digits_list) -> dict:
    joined_string = "".join(digits_list)
    segment_occurrence_ratio = {x: joined_string.count(x) for x in segments_on_display}
    return segment_occurrence_ratio


def count_value(segment_occurrence_ratio, values, sums_for_digits) -> int:
    current_value_string = ''
    for value in values:
        current_sum = 0
        for i in value:
            current_sum += segment_occurrence_ratio[i]
        current_value_string += str(sums_for_digits[current_sum])
    return int(current_value_string)


def calculate_sum_for_digits() -> dict:
    digits_on_display = {0: 'abcfeg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6: 'abdefg', 7: 'acf',
                          8: 'abcdefg', 9: 'abcdfg'}

    segment_occurrence_ratio = count_occurrence([y for x, y in digits_on_display.items()])
    sums_for_digits = {}
    for number, segments in digits_on_display.items():
        current_sum = 0
        for i in segments:
            current_sum += segment_occurrence_ratio[i]
        sums_for_digits[current_sum] = number
    return sums_for_digits


def seven_segment_display_calculation_2(content) -> int:

    result = 0
    sums_for_digits = calculate_sum_for_digits()

    for element in content:
        templates, values = element
        letter_occurrence = count_occurrence(templates)
        current_value_string = count_value(letter_occurrence, values, sums_for_digits)
        result += current_value_string

    return result


def main():
    content = read_file("input_day8.txt")
    parsed_data = parse_input(content)
    print(seven_segment_display_calculation_2(parsed_data))


if __name__ == "__main__":
    main()
